// ------------------------------------- History Page Functionality ---------------------------------------------
// -----------------------------------------------------------------------------------------------------------


// Sort by Button
document.getElementById('sortbyBtn').addEventListener('click', tableSort, false)
function tableSort()    {
    // this function will sort the history table in the following ways:
    // Ascending cough
    // Descending cough
    // time 
    // data size 
    alert("Sorted by Date")
    
}

function sortNames() {
    var sortOption = document.getElementById("sortbyBtn").value;
    var nameList = document.getElementsByClassName("name");
  
    var namesArray = Array.prototype.slice.call(nameList);
    namesArray.sort(function(a, b) {
      var nameA = a.innerText.toLowerCase();
      var nameB = b.innerText.toLowerCase();
  
      if (sortOption === "asc") {
        return nameA.localeCompare(nameB);
      } else {
        return nameB.localeCompare(nameA);
      }
    });
  
    var parent = nameList[0].parentNode;
    for (var i = 0; i < namesArray.length; i++) {
      parent.appendChild(namesArray[i]);
    }
  }
  