const BTNok = document.getElementById("Btn");

BTNok.addEventListener("click", function () {
    const Nombre = document.getElementById("Nombre").value;
    const Usuario = document.getElementById("Usuario").value;
    const Apellido = document.getElementById("Apellido").value;
    const contra = document.getElementById("Con").value;
    const Direccion = document.getElementById("Direccion").value;v$Direccion = $_POST["Direccion"];
    const ID_ciu = document.getElementById("ID_ciu").value;


    const formData = new FormData();
    formData.append("Nombre", Nombre);
    formData.append("Usuario", Usuario);
    formData.append("Apellido", Apellido);
    formData.append("Con", contra);
    formData.append("Direccion", Direccion);

    fetch('../PHP/Conexion.php', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.text())
    .then(data =>{
        const responseMessage = document.getElementById("respuesta");
        responseMessage.textContent = data;})
    .catch(error => console.error('Error:', error));

    
});