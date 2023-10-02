const restartButton = document.getElementById('restart-button');
const randomCells = document.querySelectorAll('.random');

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
document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('click', function() {
        const idParts = this.id.split('_');
        const row = idParts[1];
        const column = idParts[2];
        const is_random = this.classList.contains('random');
        const is_random_int = is_random ? 1 : 0;
        fetch(`/clicked/${row}/${column}/${is_random_int}/`)
            .then(response => response.text())
            .then(data => {
                console.log(data);
                showRestartButton();
            });
        if (is_random) {
            this.style.backgroundColor = 'green';
            const message = document.getElementById('message');
            message.textContent = 'You hit a ship!';
            this.classList.add('found');
            showRestartButton();
        } else {
            this.style.backgroundColor = 'red';
        }
    });
});