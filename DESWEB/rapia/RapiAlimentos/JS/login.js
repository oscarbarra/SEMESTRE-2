const BTNlog = document.getElementById("BtnLog");

BTNlog.addEventListener("click", function () {
    const Usuario = document.getElementById("UsuarioLog").value;
    const contra = document.getElementById("ConLog").value;

    const formData = new FormData();
    formData.append("UsuarioLog", Usuario);
    formData.append("ConLog", contra);

    fetch('../PHP/Conexion.php', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.text())
    .then(data => {const responseMessage = document.getElementById("respuesta1");
        responseMessage.textContent = data;})
        
    .catch(error => console.error('Error:', error));
});