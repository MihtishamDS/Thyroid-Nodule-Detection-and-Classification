const fileInput = document.getElementById("fileInput");
const preview = document.getElementById("preview");
const form = document.querySelector("form");
const button = document.getElementById("predictBtn");

// Preview Image
fileInput.addEventListener("change", function () {

    const file = this.files[0];

    if (!file) return;

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";

});

// Loading Animation
form.addEventListener("submit", function () {

    button.disabled = true;

    button.innerHTML = `
        <span class="spinner-border spinner-border-sm me-2"></span>
        Analyzing...
    `;

});