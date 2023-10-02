// document.querySelectorAll('.cell').forEach(cell => {
//     cell.addEventListener('click', function() {
//         this.style.backgroundColor = 'red';
//         const idParts = this.id.split('_');
//         const row = idParts[1];
//         const column = idParts[2];
//         fetch(`/clicked/${row}/${column}/`)
//             .then(response => response.text())
//             .then(data => {
//                 console.log(data);
//             });
//     });
// });

// const randomCell = document.querySelector('.random');
// randomCell.addEventListener('click', function() {
//     this.style.backgroundColor = 'green';
// });

document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('click', function() {
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
            });
        if (is_random) {
            this.style.backgroundColor = 'green';
        } else {
            this.style.backgroundColor = 'red';
        }
    });
});