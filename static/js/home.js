// ------------------------------------- Home Page Functionality ---------------------------------------------
// -----------------------------------------------------------------------------------------------------------

// Global variables ------------------------------------------------------------------------------------------ 

fileSelected = false;

// DOM Objects ---------------------------------------------------------------------------------------------
let selectBtn = document.getElementById('selectFileBtn');
let uploadBtn = document.getElementById('uploadDataBtn');

// Setup ------------------------------------------------------------------------------------------

// --------- Checking if file is selected or not
if (fileSelected) { // If we have a file selected, disable select btn
    selectBtn.disabled = true;
} else { // If we don't have a file selected, disable upload btn 
    uploadBtn.disabled = true;
}

// Event Listeners ------------------------------------------------------------------------------------------

// --------- When user clicks upload button
uploadBtn.addEventListener('click', (_event) => {
    // If file has been selected upload it
    if (fileSelected) {
        console.log('hello')
        uploadReminder.style.display = 'flex'
    // Otherwise show the reminder    
    }
})