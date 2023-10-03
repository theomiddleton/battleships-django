const restartButton = document.getElementById('restart-button');
const cells = document.querySelectorAll('.cell');
const randomCells = document.querySelectorAll('.random');
let foundRandomCells = 0;

function showRestartButton() {
    const foundRandomCells = document.querySelectorAll('.random.found');
    if (foundRandomCells.length === randomCells.length) {
        restartButton.style.display = 'block';
    } else {
        restartButton.style.display = 'none';
    }
}

function resetGame() {
    cells.forEach(cell => {
        cell.style.backgroundColor = '';
        cell.classList.remove('found');
    });
    foundRandomCells = 0;
    showRestartButton();
}

cells.forEach(cell => {
    cell.addEventListener('click', function() {
        // this breaks it all for some reason
        //it checks if the number of random cells found is equal to the number of random cells
        //if it is, it returns, and stops all code from running
        //this is bad
        //if (foundRandomCells === randomCells.length) {
        //    return;
        //}
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
                    message.textContent = 'You hit a ship!';
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