$(document).ready(function () {
    let today = new Date().toISOString().split('T')[0];
    $("input[name='date']").attr('min', today);

    $(".form-book").on("submit", function (e) {
        let valid = true;

        let nameInput = $("input[name='client_name']");
        let emailInput = $("input[name='client_email']");
        let traineeInput = $("select[name='trainee']");
        let dateInput = $("input[name='date']");
        let timeInput = $("input[name='time']");

        let name = nameInput.val().trim();
        let email = emailInput.val().trim();
        let trainee = traineeInput.val();
        let date = dateInput.val();
        let time = timeInput.val();

        // Clear old messages
        $(".error-msg").remove();

        // Validate fields
        if (name === "") {
            nameInput.after("<span class='error-msg' style='color:red;'>Name is required</span>");
            valid = false;
        }

        let emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
        if (email === "") {
            emailInput.after("<span class='error-msg' style='color:red;'>Email is required</span>");
            valid = false;
        } else if (!emailPattern.test(email)) {
            emailInput.after(
                "<span class='error-msg' style='color:red;'>Enter a valid email</span>");
            valid = false;
        }

        if (!trainee) {
            traineeInput.after(
                "<span class='error-msg' style='color:red;'>Please select a coach</span>");
            valid = false;
        }

        if (date === "") {
            dateInput.after("<span class='error-msg' style='color:red;'>Date is required</span>");
            valid = false;
        }

        if (time === "") {
            timeInput.after("<span class='error-msg' style='color:red;'>Time is required</span>");
            valid = false;
        }

        // Prevent submission if validation fails
        if (!valid) {
            e.preventDefault();
        }
    });
});