// ------------------------------------- Home Page Functionality ---------------------------------------------
// -----------------------------------------------------------------------------------------------------------

// Global variables ------------------------------------------------------------------------------------------ 



// DOM Objects ---------------------------------------------------------------------------------------------
let uploadBtn = document.getElementById('uploadDataBtn');
let accData = document.getElementById('accData');
let audioData = document.getElementById('audioData');
let loadingDialog = document.getElementById('loadingDialog');
let coughCountDialog = document.getElementById('coughCountDialog');
let coughCountVal = document.getElementById('coughCountVal');
let coughDataHeadingName = document.getElementById('coughDataName');
let backHomeBtn = document.getElementById('backHome');
let toHistoryBtn = document.getElementById('toHistory')

// Setup ------------------------------------------------------------------------------------------



// Event Listeners ------------------------------------------------------------------------------------------

// --------- When user clicks upload button
uploadBtn.addEventListener('click', (_event) => {
    initializeAnalysis();
});

// --------- When user clicks back button on dialog
backHomeBtn.addEventListener('click', (_event) => {
    window.location.href = '/';
})

// --------- When user clicks history button on dialog
toHistoryBtn.addEventListener('click', (_event) => {
    window.location.href = '/history';
})

// Helper Functions ------------------------------------------------------------------------------------------

// --------- Checking if files are selected or not - users can't upload until 2 files are selected
setInterval(checkFileInput, 500); // checks every 500ms if files are selected

function checkFileInput() {
    // if (accData.files.length <= 0 || audioData.files.length <= 0 ) {
    //     uploadBtn.disabled = true;
    // } else {
    //     uploadBtn.disabled = false;
    // }
}

function initializeAnalysis() {
    loadingDialog.showModal();

    setTimeout(showResults, 3000);
}

function showResults() {
    loadingDialog.close();
    coughCountDialog.showModal();
    coughCountDialog.style.display = 'flex';
    
    let coughCount = 13; // replace with a function that returns algorithm results
    let coughDataName = 'Cough Count' // replace with a function that returns default name
    
    coughDataHeadingName.innerHTML = coughDataName;
    coughCountVal.innerHTML = coughCount;
}