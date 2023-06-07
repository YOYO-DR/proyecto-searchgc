const formulario = document.querySelector("form");
const correoInput = formulario.querySelector("#correo");
const correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

formulario.addEventListener("submit", function (event) {
  if (!correoRegex.test(correoInput.value)) {
    event.preventDefault();
    alert("La dirección de correo electrónico no es válida");
  }
});
