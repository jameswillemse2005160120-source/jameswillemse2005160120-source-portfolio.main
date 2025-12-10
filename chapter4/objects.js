// objects.js
const project = {
    code: 'PC(103)',
    name: 'First Object Project',
    status: 'Working (Object Data)',
    details: 'This project demonstrates creating and accessing properties of a JavaScript object.',
    link: 'http://xkcd.com'
};

// Create the HTML content
let content = `
    <h1>Project: ${project.name}</h1>
    <p>Code: <strong>${project.code}</strong></p>
    <p>Status: ${project.status}</p>
    <p>${project.details}</p>
    <p>Check the console (F12) for the full object details.</p>
    <p><a href="${project.link}">Reference Comic</a></p>
`;

// Find the placeholder element and insert the HTML
document.getElementById('js-output').innerHTML = content;

// Always good practice: log the object to the console for debugging
console.log("Full Project Object:", project);
