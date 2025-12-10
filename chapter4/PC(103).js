// PC(103).js
const message = "SUCCESS! The JavaScript file PC(103).js loaded and wrote this message to the page.";
const footer = "This confirms the connection between your HTML and your JS is working!";

// Create a small block of HTML
let confirmationHTML = `
    <hr>
    <h3>PC(103) File Status:</h3>
    <p style="background-color: #e0ffe0; padding: 10px; border: 1px solid green;">
        ${message}
    </p>
    <p>${footer}</p>
    <hr>
`;

// Find the placeholder element and insert the HTML
document.getElementById('js-output').innerHTML = confirmationHTML;
