document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger"); // Selects the hamburger icon
    const nav = document.querySelector("nav"); // Selects the navigation bar

    hamburger.addEventListener("click", function () {
        nav.classList.toggle("open"); // Toggles the "open" class on the navigation bar
    });
});
