// script.js
document.addEventListener('scroll', () => {
    const image = document.querySelector('.animated-image');
    const container = document.querySelector('.image-container');

    // Get the scroll position relative to the image container
    const containerPosition = container.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;

    // Trigger animation when container enters viewport
    if (containerPosition < windowHeight && containerPosition > 0) {
        const offset = windowHeight - containerPosition; // How far the image moves
        const maxOffset = windowHeight / 2; // Limit the movement to the center

        const percentage = Math.min(offset / maxOffset, 1); // Limit to 100%
        const moveToCenter = (1 - percentage) * 50; // Calculate movement percentage

        image.style.transform = `translateX(-${moveToCenter}%)`;
    }
});
