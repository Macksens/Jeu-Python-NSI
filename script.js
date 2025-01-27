document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
    
    // Example function to display an alert
    function showAlert() {
        alert('Hello, World!');
    }

    // Add event listener to a button
    const button = document.getElementById('myButton');
    if (button) {
        button.addEventListener('click', showAlert);
    }
});