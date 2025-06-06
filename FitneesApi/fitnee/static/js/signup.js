$(document).ready(function () {
    $('.signup-form').on('submit', function (e) {
        let username = $('input[name="username"]').val().trim();
        let email = $('input[name="email"]').val().trim();
        let password = $('input[name="password"]').val();
        let confPassword = $('input[name="conf_password"]').val();

        // Clear any previous error messages
        $('.error-msg').remove();

        let isValid = true;

        if (username === '') {
            $('input[name="username"]').after('<span class="error-msg">Username is required.</span>');
            isValid = false;
        }

        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email === '' || !emailPattern.test(email)) {
            $('input[name="email"]').after('<span class="error-msg">Enter a valid email.</span>');
            isValid = false;
        }

        if (password.length < 6) {
            $('input[name="password"]').after('<span class="error-msg">Password must be at least 6 characters.</span>');
            isValid = false;
        }

        if (password !== confPassword) {
            $('input[name="conf_password"]').after('<span class="error-msg">Passwords do not match.</span>');
            isValid = false;
        }

        if (!isValid) {
            e.preventDefault(); // Stop form submission
        }
    });
});
