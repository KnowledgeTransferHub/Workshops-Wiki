// Function to handle registration form submission
document.getElementById("registration-form").addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("reg-username").value;
    const password = document.getElementById("reg-password").value;

    fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            // Clear the form
            document.getElementById("registration-form").reset();
        });
});

// Function to handle login form submission
document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    fetch(`http://localhost:5000/login?username=${username}&password=${password}`)
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            // Clear the form
            document.getElementById("login-form").reset();
        });
});
