document.addEventListener("DOMContentLoaded", () => {
    cargarReacciones();

    document.querySelectorAll('.seccion-reaccion').forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            const reaccionesOcultas = btn.querySelector('.reacciones-ocultas');
            reaccionesOcultas.style.display = 'flex';
        });

        btn.addEventListener('mouseleave', function() {
            const reaccionesOcultas = btn.querySelector('.reacciones-ocultas');
            reaccionesOcultas.style.display = 'none';
        });
    });

    document.querySelectorAll('.opcion-reaccion').forEach(option => {
        option.addEventListener('click', function() {
            const emoji = option.getAttribute('emoji-id');
            const btnReaccion = option.closest('.seccion-reaccion');
            const btnReaccionSelect = btnReaccion.querySelector('.btn-reaccion');
            const reaccionesOcultas = btnReaccion.querySelector('.reacciones-ocultas');

            const nombreEmoji = option.querySelector('.nombre-emoji').textContent;
            btnReaccionSelect.textContent = `${emoji} ${nombreEmoji}`;

            btnReaccion.classList.add('selected');
            reaccionesOcultas.style.display = 'none';
            guardarReaccion(btnReaccion.getAttribute('tutorial-id'), emoji);
        });
    });
});

function cargarReacciones() {
    const reaccionesGuardadas = JSON.parse(localStorage.getItem('reacciones')) || {};

    document.querySelectorAll('.seccion-reaccion').forEach(btn => {
        const publicacion = btn.getAttribute('tutorial-id');
        const btnReaccionSelect = btn.querySelector('.btn-reaccion');

        if (reaccionesGuardadas[publicacion]) {
            const emoji = reaccionesGuardadas[publicacion];
            const nombreEmoji = {
                '👍': 'Me gusta',
                '😲': 'Me asombra',
                '❤️': 'Me encanta'
            };
            btnReaccionSelect.textContent = `${emoji} ${nombreEmoji[emoji]}`;
            btn.classList.add('selected');
        }
    });
}