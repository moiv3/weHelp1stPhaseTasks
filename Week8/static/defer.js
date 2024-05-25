console.log("Script started.");

addEventListener("DOMContentLoaded", function(event){
    console.log("DOMContentLoaded event happened!")
});

setTimeout(() => {
    console.log("Script completed after 2 seconds.");
}, 2000);

// Try to access and modify a DOM element before it's available
console.log("Trying to change 'content' div.");
const contentDiv = document.getElementById("content");
if (contentDiv) {
    contentDiv.textContent = "Content modified by script.";
} else {
    console.log("Content div not found.");
}
console.log("Script finished loading.");