// {id: 1, recuperar clave: function (){}}
function Usuario() {
    this.id = 1;
    this.recuperarClave = function () {
        console.log('recuperando clave...');
    }
}

let usuario = new Usuario(); //cuando se utiliza new, se crea un vinvulo en el aire y se vincula con el objetivo vacio.
console.log(usuario);