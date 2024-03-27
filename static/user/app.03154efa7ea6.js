
document.getElementById('horizontalList').scrollLeft = document.querySelector('.list-item').offsetLeft;
// Function to toggle classes for the "slide" and "display" elements
function toggleClasses() {
// Find the element with ID "slide"
var slideElement = document.getElementById("slide");

// Find the element with ID "display"
var displayElement = document.getElementById("display");
var searchElement = document.getElementById("search");
var ItemElement = document.getElementById("horizontalList");
// Toggle the classes for the "slide" element
if (slideElement.classList.contains("h-0")) {
    // If "h-0" is present, remove it and add "h-56"
    slideElement.classList.remove("h-0");
    slideElement.classList.add("h-52");
    searchElement.classList.remove("z-10");
    searchElement.classList.add('-z-10');
} else {
    // If "h-0" is not present, remove "h-56" and add "h-0"
    slideElement.classList.remove("h-52");
    slideElement.classList.add("h-0");
    searchElement.classList.remove("-z-10");
    searchElement.classList.add('z-10');
}

// Toggle the classes for the "display" element
if (displayElement.classList.contains("hidden")) {
    // If "hidden" is present, remove it and add "hd"
    displayElement.classList.remove("hidden");
    displayElement.classList.add("flex");
} else {
    // If "hidden" is not present, remove "hd" and add "hidden"
    displayElement.classList.remove("hd");
    displayElement.classList.add("hidden");
}


if (ItemElement.classList.contains("z-10")) {
    // If "hidden" is present, remove it and add "hd"
    ItemElement.classList.remove("z-10");
    ItemElement.classList.add("-z-10");
} else {
    // If "hidden" is not present, remove "hd" and add "hidden"
    ItemElement.classList.remove("-z-10");
    ItemElement.classList.add("z-10");
}

}

// Add a click event listener to the element with ID "menu"
document.getElementById("menu").addEventListener("click", toggleClasses);


// Select the element by ID
var preElement = document.getElementById("pre");

// Function to fade out the element and remove it from the DOM after a delay
function fadeOutAndRemove() {
preElement.style.transition = "opacity 1s ease-out"; // You can adjust the duration and timing function
preElement.style.opacity = 0;

// Set a timeout to remove the element from the DOM after the fade-out animation
setTimeout(function () {
    preElement.parentNode.removeChild(preElement);
}, 1000); // Adjust the delay to match the transition duration
}

// Set a timeout to execute the function after 4 seconds (4000 milliseconds)
setTimeout(fadeOutAndRemove, 1000);
