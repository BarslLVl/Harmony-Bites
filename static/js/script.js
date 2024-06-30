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
