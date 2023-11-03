document.getElementById("miFormulario").addEventListener("submit", function (event) {
    event.preventDefault(); 
    var mensaje = document.getElementById("mensaje");
    mensaje.style.display = "block";
});