// objectarray.js

const features = [
    "Responsive Design Check",
    "JavaScript Functionality Test",
    "CSS Styling Review",
    "Accessibility Audit"
];

// Start building the list HTML
let listTitle = '<h2>Project Features to Implement</h2>';
let listItems = '';

// Use the map function to create an array of HTML list items
// and then join them into a single string.
listItems = features.map(feature => {
    // Add a checkmark and the feature name to a list item
    return `<li>✅ ${feature}</li>`;
}).join(''); // join('') concatenates the array items into one long string

const content = listTitle + '<ul>' + listItems + '</ul>';

// Output the content to the HTML page
document.getElementById('js-output').innerHTML = content;

console.log("Feature Array Loaded:", features);
