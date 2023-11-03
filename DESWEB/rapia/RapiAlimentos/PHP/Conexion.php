<?php


$sqli = mysqli_connect("localhost", "root", "", "RapiA");


if (
    isset($_POST["Nombre"], $_POST["Usuario"], $_POST["Apellido"], $_POST["Con"], $_POST["Direccion"], $_POST["ID_ciu"])
) {

    $Nombre = $_POST["Nombre"];
    $Usuario = $_POST["Usuario"];
    $Apellido = $_POST["Apellido"];
    $Contra = $_POST["Con"];
    $Direccion = $_POST["Direccion"];
    $ID_ciu = $_POST["ID_ciu"];


    $query = "SELECT * FROM cliente WHERE Usuario='$Usuario'";
    $result = mysqli_query($sqli, $query);

    if (!$result) {
        die("Query failed: " . mysqli_error($sqli));
    }

    if (mysqli_num_rows($result) > 0) {
        echo "Usuario ya existe";
    } else {
        
        $query = "INSERT INTO cliente(Nombre, Apellido, Usuario, passwd, Direccion, ID_ciu) VALUES ('$Nombre', '$Apellido', '$Usuario','$Contra' , '$Direccion', '$ID_ciu');";

        $response = mysqli_query($sqli, $query);

        if ($response) {
            echo "Bienvenido $Usuario";
        } else {
            echo "Ocurrió un error al registrar el usuario.";
        }
    }
}


if(isset($_POST["UsuarioLog"]) && isset($_POST["ConLog"])) {
    $UsuarioLog = $_POST["UsuarioLog"];
    $ConLog = $_POST["ConLog"];

    $resul3 = mysqli_query($sqli, "SELECT * FROM cliente WHERE Usuario='$UsuarioLog' AND passwd='$ConLog'");

    if (mysqli_num_rows($resul3) > 0) {
        
        echo "sesion iniciada"; 
    } else {
        echo "Error de inicio de sesión"; 
    }
}



mysqli_close($sqli);


?>
    




