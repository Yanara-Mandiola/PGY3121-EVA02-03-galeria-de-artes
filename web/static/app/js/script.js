// Función para alternar la clase "active" en el menú de navegación
const navLinks = document.querySelectorAll('nav ul li a');

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.forEach(link => link.classList.remove('active'));
        link.classList.add('active');
    });
});

// Función para mostrar un mensaje de confirmación al suscribirse al boletín
const subscribeForm = document.querySelector('footer form');

subscribeForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.querySelector('footer form input').value;
    if (email) {
        alert(`¡Gracias por suscribirte con el email ${email}!`);
        subscribeForm.reset();
    } else {
        alert('Por favor, ingresa un email válido.');
    }
});
