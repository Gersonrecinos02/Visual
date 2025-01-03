// Personaje de Tv

let nombre = 'Tanjiro';
let anime = 'Demon player';
let edad = 16;

let personaje = {
    nombre: 'Tanjiro',
    anime: 'Demon player',
    edad: 16,
};
console.log(personaje);
console.log(personaje.nombre);
console.log(personaje['anime']);


personaje.edad = 13;

let llave = 'edad';
personaje['llave'] = 16;

delete personaje.anime;

console.log(personaje)
