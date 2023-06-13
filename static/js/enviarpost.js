function enviarPost(idForm, csrftoken, url, funcion) {
  const form = document.getElementById(idForm);

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
        },
        body: formData,
      });
      const data = await response.json();
      if (response.ok) {
        form.reset();
      }
      funcion(data); //ejecutar funcion si la respuesta es correcta
    } catch (error) {
      console.error("Error:", error);
    }
  });
}
