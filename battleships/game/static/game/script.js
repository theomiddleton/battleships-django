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

//let randomCell = null;
//
//document.querySelectorAll('.cell').forEach(cell => {
//    cell.addEventListener('click', function() {
//        const idParts = this.id.split('_');
//        const row = idParts[1];
//        const column = idParts[2];
//        fetch(`/clicked/${row}/${column}/`)
//            .then(response => response.text())
//            .then(data => {
//                if (this === randomCell) {
//                    this.style.backgroundColor = 'orange';
//                } else {
//                    this.style.backgroundColor = 'red';
//                }
//            });
//    });
//});
//
//function selectRandomCell() {
//    const cells = document.querySelectorAll('.cell');
//    randomCell = cells[Math.floor(Math.random() * cells.length)];
//}
//selectRandomCell();