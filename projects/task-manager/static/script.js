const text = "Hi, I'm Laetetia ";
let i = 0;

function typeEffect() {
    if (i < text.length) {
        document.querySelector(".hero h1").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeEffect, 80);
    }
}

window.onload = typeEffect;
const toggleBtn = document.getElementById("themeToggle");

toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
});
const form = document.querySelector(".contact-form");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    alert("Message sent successfully! 🚀");
});