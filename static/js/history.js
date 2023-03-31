// ------------------------------------- History Page Functionality ---------------------------------------------
// -----------------------------------------------------------------------------------------------------------


// Sort by Button

function sortNames() {
    var sortOption = document.getElementById("sortbyBtn").value;
    var rows = document.querySelectorAll('tr:not(:first-child)');
    
    // Sort the rows based on the name column
    var sortedRows = Array.from(rows)
      .sort((a, b) => {
        var nameA = a.querySelector('.name').textContent.toLowerCase();
        var nameB = b.querySelector('.name').textContent.toLowerCase();
        return sortOption === 'asc' ? nameA.localeCompare(nameB) : nameB.localeCompare(nameA);
      });
    
    // Append the sorted rows to the table body
    var tableBody = rows[0].parentNode;
    sortedRows.forEach(row => tableBody.appendChild(row));
    
    // Update the delete buttons to match the new row order
    var deleteButtons = document.getElementsByClassName('deleteBtn');
    Array.from(deleteButtons).forEach(button => {
      var rowIndex = button.closest('tr').rowIndex - 1; // Subtract 1 to account for the header row
      button.className = 'deleteBtn';
      button.setAttribute('onclick', `DeleteRowFunction(this, ${rowIndex})`);
    });
  }
  
  