document.addEventListener('DOMContentLoaded', function() {
    const bookButton = document.querySelector('.book-button');
    const notification = document.querySelector('.notification');

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

    function showNotification(message) {
        notification.textContent = message;
        notification.classList.add('show');
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    }
});

// Dropdown menu for user icon
document.addEventListener('DOMContentLoaded', function() {
    const userIcon = document.querySelector('.user-icon img');
    const dropdownMenu = document.querySelector('.dropdown-menu');

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