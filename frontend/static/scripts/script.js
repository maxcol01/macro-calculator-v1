document.addEventListener("DOMContentLoaded", () => {

    // change dynamically the date to the page bottom
    const dateSpan = document.getElementById("date-footer");
    const date = new Date();
    dateSpan.innerText = String(date.getFullYear());
})