document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('click', function() {
        this.style.backgroundColor = 'red';
        const idParts = this.id.split('_');
        const row = idParts[1];
        const column = idParts[2];
        fetch(`/clicked/${row}/${column}/`)
            .then(response => response.text())
            .then(data => {
                console.log(data);
            });
    });
});
