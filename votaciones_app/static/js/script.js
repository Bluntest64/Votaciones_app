// Navegación entre páginas

function irRegistro() {
    window.location.href = "/registro";
}

function irConsulta() {
    window.location.href = "/consulta";
}

function volverInicio() {
    window.location.href = "/";
}


// Validación de formulario de registro

function validarRegistro() {

    let documento = document.getElementById("documento").value;
    let nombre = document.getElementById("nombre").value;

    if(documento === "" || nombre === ""){
        alert("Todos los campos son obligatorios");
        return false;
    }

    if(documento.length < 5){
        alert("El documento no es válido");
        return false;
    }

    return true;
}


// Validación de consulta

function validarConsulta(){

    let documento = document.getElementById("documento").value;

    if(documento === ""){
        alert("Ingrese su documento");
        return false;
    }

    return true;
}