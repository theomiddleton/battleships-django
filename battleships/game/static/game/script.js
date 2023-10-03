const restartButton = document.getElementById('restart-button');
const cells = document.querySelectorAll('.cell');
const randomCells = document.querySelectorAll('.random');
let foundRandomCells = 0;

function showRestartButton() {
    const foundRandomCells = document.querySelectorAll('.random.found');
    if (foundRandomCells.length === randomCells.length) {
        if (restartButton) {
            restartButton.style.display = 'block';
        }
    } else {
        if (restartButton) {
            restartButton.style.display = 'none';
        }
    }
}

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