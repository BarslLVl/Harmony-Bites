document.addEventListener('DOMContentLoaded', function() {
    const bookButton = document.querySelector('.book-button');
    const notification = document.querySelector('.notification');
    const navMenuIcon = document.querySelector('.nav-menu-icon');

    if (bookButton) {
        bookButton.addEventListener('click', function(event) {
            event.preventDefault();
            const userAuthenticated = document.body.getAttribute('data-authenticated') === 'true';

            if (!userAuthenticated) {
                showNotification('Please log in or sign up to book a table.');
            } else {
                window.location.href = bookButton.getAttribute('href');
            }
        });
    }
    // Dropdown menu for user icon
    function showNotification(message) {
        notification.textContent = message;
        notification.classList.add('show');
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    }

    if (navMenuIcon) {
        navMenuIcon.addEventListener('click', function() {
            const navMenu = document.getElementById('nav-menu');
            navMenu.classList.toggle('show');
        });
    }
    // Mobile menu
    const userIcon = document.getElementById('userIcon');
    const dropdownMenu = document.getElementById('dropdownMenu');

    if (userIcon && dropdownMenu) {
        userIcon.addEventListener('click', function() {
            dropdownMenu.classList.toggle('show');
        });

        document.addEventListener('click', function(event) {
            if (!userIcon.contains(event.target) && !dropdownMenu.contains(event.target)) {
                dropdownMenu.classList.remove('show');
            }
        });
    }
});
