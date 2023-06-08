const currentScript = document.currentScript;
const csrftoken = currentScript.dataset.token;
const url = currentScript.dataset.url;
const idForm = currentScript.dataset.id;

const form = document.getElementById(idForm);

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(form);

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrftoken, // Asegúrate de incluir el token CSRF de Django
      },
      body: formData,
    });
    const data = await response.json();
    if (response.ok) {
      form.reset();
    }
    console.log(data); // Muestra el arreglo en la consola
  } catch (error) {
    console.error("Error:", error);
  }
});
