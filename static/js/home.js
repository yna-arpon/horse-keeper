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
let toHistoryBtn = document.getElementById('toHistory');
let audioFileName = document.getElementById('audioDataSelectedFile');
let accFileName = document.getElementById('accDataSelectedFile');
let filesStateInfo = document.getElementById('filesStateInfo');
let seeTimestampsBtn = document.getElementById('seeTimestamps');
let timeStampsDiv = document.getElementById('timeStampsDiv');
let resultsDiv = document.getElementById('resultsDiv');
let seeCoughCountBtn = document.getElementById('seeCoughCount');

// Setup ------------------------------------------------------------------------------------------



// Event Listeners ------------------------------------------------------------------------------------------

// --------- When user clicks selects audio data
audioData.addEventListener("change", (_event) => {
    let selectedAudioFile = document.querySelector("#audioData").files[0];
    audioFileName.innerText = "Audio File: " + selectedAudioFile.name;
    filesStateInfo.style.display = "none";
})

// --------- When user clicks selects acc data
accData.addEventListener("change", (_event) => {
    let selectedAccFile = document.querySelector("#accData").files[0];
    accFileName.innerText = "Acceleration File: " + selectedAccFile.name;
    filesStateInfo.style.display = "none";
})

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

// --------- When user wants to see timestamps dialog
seeTimestampsBtn.addEventListener('click', (_event)=>{
    resultsDiv.style.display = "none"; 
    timeStampsDiv.style.display = "flex";
})

seeCoughCountBtn.addEventListener('click', (_event)=> {
    resultsDiv.style.display = "flex";
    timeStampsDiv.style.display = "none"
})

// Helper Functions ------------------------------------------------------------------------------------------

// --------- Checking if files are selected or not - users can't upload until 2 files are selected
setInterval(checkFileInput, 500); // checks every 500ms if files are selected

function checkFileInput() {
    if (accData.files.length <= 0 || audioData.files.length <= 0 ) {
        uploadBtn.disabled = true;
    } else {
        uploadBtn.disabled = false;
    }
}

function initializeAnalysis() {
    loadingDialog.showModal();
}

function showResults() {
    console.log('showing results')
    loadingDialog.close();
    coughCountDialog.showModal();
    coughCountDialog.style.display = 'flex';
}