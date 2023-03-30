// ------------------------------------- Home Page Functionality ---------------------------------------------
// -----------------------------------------------------------------------------------------------------------

// Global variables ------------------------------------------------------------------------------------------ 

// DOM Objects ---------------------------------------------------------------------------------------------
let homeBtn = document.getElementById('homeBtn');
let historyBtn = document.getElementById('historyBtn');

// Event Listeners ------------------------------------------------------------------------------------------

// Goes to home page when user clicks home button
homeBtn.addEventListener('click', (_event) => {
    window.location.href = '/';
})

// Goes to history page when user clicks history button
historyBtn.addEventListener('click', (_event) => {
    window.location.href = '/history';
})