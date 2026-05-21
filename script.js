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