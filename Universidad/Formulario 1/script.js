function registro(){
    const usuario = document.getElementById("usuario").value;
    const password = document.getElementById("password").value;
    

}

function login(){
    const usuario = document.getElementById("usuario").value;
    const password = document.getElementById("password").value;
    
    console.log("Hola Mundo");
    console.log(usuario);
    console.log(password);

    if (usuario == "Hola" && password == 1234 ){
        console.log("Bienvenido");
        alert("Bienvenido");
        window.location.href = "Prueba1.html";
    } else {
        console.log("Usuario no encontrado");
    }
}
  