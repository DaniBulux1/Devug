//Reacciones disponibles
const simbolos = {
  'like': '👍',
  'wow': '😲',
  'love': '❤️'
};

document.addEventListener("DOMContentLoaded", () => {
  cargarReacciones();

  //Seleccionar opciones
  document.querySelectorAll('.opcion-reaccion').forEach(option => {
    option.addEventListener('click', () => {
      const emoji = option.getAttribute('emoji-id');
      const seccionReaccion = option.closest('.seccion-reaccion');
      const btnReaccion = seccionReaccion.querySelector('.btn-reaccion');
      const tutorialID = seccionReaccion.getAttribute('tutorial-id');
      const nombreEmoji = option.querySelector('.nombre-emoji').textContent;
      const randomUID = 'UID' + Math.random().toString(36).substring(2, 15);

      //Cambiar a texto
      btnReaccion.textContent = `${simbolos[emoji]} ${nombreEmoji}`;
      seccionReaccion.classList.add('selected');
      seccionReaccion.querySelector('.reacciones-ocultas').style.display = 'none';

      //Guardar la reacción
      fetch('/api/reaccion/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          tutorial_id: tutorialID,
          emoji: emoji,
          usuario_uid: randomUID
        })
      })
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          console.log('Reacción guardada o eliminada:', data.message);
          cargarContadoresBackend(tutorialID);
        } else {
          console.error('Error guardando reacción:', data.error);
        }
      })
      .catch(error => {
        console.error('Error en fetch:', error);
      });

      const reaccionesGuardadas = JSON.parse(localStorage.getItem('reacciones')) || {};
      reaccionesGuardadas[tutorialID] = emoji;
      localStorage.setItem('reacciones', JSON.stringify(reaccionesGuardadas));

      mostrarContadores(tutorialID, reaccionesGuardadas);
    });
  });
});

function cargarReacciones() {
  const reaccionesGuardadas = JSON.parse(localStorage.getItem('reacciones')) || {};

  //Cargar reaciones
  document.querySelectorAll('.seccion-reaccion').forEach(seccion => {
    const tutorialID = seccion.getAttribute('tutorial-id');
    const btnReaccion = seccion.querySelector('.btn-reaccion');

    //Solicitar reacciones
    fetch(`/api/reaccion/${tutorialID}/`)
      .then(res => res.json())
      .then(data => {
        const reacciones = data.reacciones || {};

        for (const emoji in reacciones) {
          const count = reacciones[emoji];
          if (count > 0) {
            const nombreEmoji = {
              'like': 'Me gusta',
              'wow': 'Me asombra',
              'love': 'Me encanta'
            }[emoji] || emoji;

            btnReaccion.textContent = `${simbolos[emoji]} ${nombreEmoji}`;
            seccion.classList.add('selected');
            break;
          }
        }
      })
      .catch(err => console.error('Error cargando reacciones del backend:', err));

    //Verificación con en el localStorage
    if (reaccionesGuardadas[tutorialID]) {
      const emoji = reaccionesGuardadas[tutorialID];
      const nombres = {
        'like': 'Me gusta',
        'wow': 'Me asombra',
        'love': 'Me encanta'
      };
      btnReaccion.textContent = `${simbolos[emoji]} ${nombres[emoji]}`;
      seccion.classList.add('selected');
    }
  });

  //Mostrar reacciones guardadas
  mostrarContadores(null, reaccionesGuardadas);
}

function cargarContadoresBackend(tutorialID) {
  fetch(`/api/reaccion/${tutorialID}/`)
    .then(res => res.json())
    .then(data => {
      const contenedor = document.getElementById(`conteo-${tutorialID}`);
      if (contenedor) {
        contenedor.innerHTML = '';
        for (const e in data.reacciones) {
          const count = data.reacciones[e];
          if (count > 0) {
            contenedor.innerHTML += `<span style="margin-right: 10px;">${simbolos[e]} ${count}</span>`;
          }
        }
      }
    })
    .catch(err => console.error('Error cargando contadores:', err));
}

function mostrarContadores(tutorialID, reaccionesGuardadas) {
  //Para el conteo
  const conteos = { 'like': 0, 'wow': 0, 'love': 0 };

  for (const key in reaccionesGuardadas) {
    const r = reaccionesGuardadas[key];
    if (conteos[r] !== undefined) {
      conteos[r]++;
    }
  }

  //Actualizar conteo
  if (!tutorialID) {
    document.querySelectorAll('.conteo-reacciones').forEach(conteoDiv => {
      conteoDiv.innerHTML = '';
      for (const e in conteos) {
        if (conteos[e] > 0) {
          conteoDiv.innerHTML += `<span style="margin-right: 10px;">${simbolos[e]} ${conteos[e]}</span>`;
        }
      }
    });
  } else {
    const contenedor = document.getElementById(`conteo-${tutorialID}`);
    if (contenedor) {
      contenedor.innerHTML = '';
      for (const e in conteos) {
        if (conteos[e] > 0) {
          contenedor.innerHTML += `<span style="margin-right: 10px;">${simbolos[e]} ${conteos[e]}</span>`;
        }
      }
    }
  }
}