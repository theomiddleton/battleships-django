const restartButton = document.getElementById('restart-button');
const cells = document.querySelectorAll('.cell');
const randomCells = document.querySelectorAll('.random');
const showShipsButton = document.getElementById('show-ships-button');
const resetScoreButton = document.getElementById('score-reset');
let foundRandomCells = 0;

function resetScore() {
    fetch('/reset-score/')
        .then(response => response.text())
        .then(data => {
            console.log(data);
            console.log('Score has been reset!');
            const message = document.getElementById('message');
            message.textContent = 'Score has been reset!';
        });
}


function showRestartButton() {
    const foundRandomCells = document.querySelectorAll('.random.found');
    if (foundRandomCells.length === randomCells.length) {
        restartButton.style.display = 'block';
    } else {
        restartButton.style.display = 'none';
    }
}

let shown = false;
function showShips() {
    if (shown === false) {
        randomCells.forEach(cell => {
            cell.style.backgroundColor = 'lightblue';
        });
        showShipsButton.textContent = 'Hide Ships';
        shown = true;
    } else {
        randomCells.forEach(cell => {
            cell.style.backgroundColor = '';
        });
        showShipsButton.textContent = 'Show Ships';
        shown = false;
    }
}

function resetGame() {
    cells.forEach(cell => {
        cell.style.backgroundColor = '';
        cell.classList.remove('found');
    });
    foundRandomCells = 0;
    hits = 0;
    const message = document.getElementById('message');
    message.textContent = ''; // hide message
    showRestartButton();
}

let hits = 0; // initialize hits variable outside of forEach loop
cells.forEach(cell => {
    cell.addEventListener('click', function() {
        if (foundRandomCells === randomCells.length) {
            return;
        }
        const idParts = this.id.split('_');
        const row = idParts[1];
        const column = idParts[2];
        const is_random = this.classList.contains('random');
        //fetch(`/clicked/${row}/${column}/${isRandom}/`)
        const is_random_int = is_random ? 1 : 0;
        fetch(`/clicked/${row}/${column}/${is_random_int}/`)
            .then(response => response.text())
            .then(data => {
                console.log(data);
                if (is_random) {
                    this.style.backgroundColor = 'green';
                    const message = document.getElementById('message');
                    hits++; // increment hits variable
                    message.textContent = 'You hit a ship! Total hits: ' + hits;
                    this.classList.add('found');
                    foundRandomCells++;
                    showRestartButton();
                } else {
                    this.style.backgroundColor = 'red';
                }
            });
    });
});
restartButton.addEventListener('click', resetGame);
showShipsButton.addEventListener('click', showShips);
resetScoreButton.addEventListener('click', resetScore);

