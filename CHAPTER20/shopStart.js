/**************************
 * 1. GLOBAL DATA
 **************************/
var nums = [1, 2, 3, 4];
var items = ["Coke", "Kit Kat", "Bar One", "Fanta"];
var prices = [7.5, 9.5, 8.5, 7.5];
var quantities = [0, 0, 0, 0];
var totals = [0.0, 0.0, 0.0, 0.0];


/**************************
 * 2. MODIFY DATA
 **************************/

// Add item
function add_selection(index) {
    quantities[index]++;
    totals[index] = prices[index] * quantities[index];
    display_all();
}

// Remove item (prevents negatives)
function remove_selection(index) {
    if (quantities[index] > 0) {
        quantities[index]--;
        totals[index] = prices[index] * quantities[index];
    }
    display_all();
}


/**************************
 * 3. CALCULATIONS
 **************************/

// Checkout total
function checkout() {
    let grandTotal = 0;

    for (let i = 0; i < totals.length; i++) {
        grandTotal += totals[i];
    }

    document.getElementById("grandTotal").innerHTML =
        "Total Order Amount: R " + grandTotal.toFixed(2);
}


/**************************
 * 4. DISPLAY
 **************************/

function display_all() {

    let myTable = "<table border='1'>";
    myTable += "<tr>";
    myTable += "<th>Num</th>";
    myTable += "<th>Item</th>";
    myTable += "<th>Price</th>";
    myTable += "<th>Quantity</th>";
    myTable += "<th>Total</th>";
    myTable += "<th>Add</th>";
    myTable += "<th>Remove</th>";
    myTable += "</tr>";

    for (let i = 0; i < items.length; i++) {
        myTable += "<tr>";
        myTable += "<td>" + nums[i] + "</td>";
        myTable += "<td>" + items[i] + "</td>";
        myTable += "<td>R " + prices[i].toFixed(2) + "</td>";
        myTable += "<td>" + quantities[i] + "</td>";
        myTable += "<td>R " + totals[i].toFixed(2) + "</td>";
        myTable += "<td><button onclick='add_selection(" + i + ")'>Add</button></td>";
        myTable += "<td><button onclick='remove_selection(" + i + ")'>Remove</button></td>";
        myTable += "</tr>";
    }

    myTable += "</table>";

    document.getElementById("demo").innerHTML = myTable;
}


/**************************
 * 5. INITIAL LOAD
 **************************/

window.onload = function () {
    display_all();
};
