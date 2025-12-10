// objectarray1.js

const teamMembers = [
    { name: 'Alice', role: 'Developer', active: true },
    { name: 'Bob', role: 'Designer', active: false },
    { name: 'Charlie', role: 'Project Lead', active: true }
];

// Start building the HTML output
let teamHTML = '<h2>Team Members and Roles</h2>';

// Use forEach to iterate and build the display logic
teamMembers.forEach(member => {
    let statusIcon = member.active ? '🟢' : '🔴';
    let statusStyle = member.active ? 'font-weight: bold;' : 'color: grey;';
    
    // Append a paragraph for each member using template literals
    teamHTML += `
        <p style="${statusStyle}">
            ${statusIcon} 
            **${member.name}** - *${member.role}*
        </p>
    `;
});

// Output the content to the HTML page
document.getElementById('js-output').innerHTML = teamHTML;

console.log("Team Member Array Loaded:", teamMembers);
