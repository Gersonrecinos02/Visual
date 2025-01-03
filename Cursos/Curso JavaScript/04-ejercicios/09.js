/**
 * Crear algoritmo que devuelva un 
 * array de objetos en base a pares
 */

let pairs = [
    [1, { name: "Nicolas" }],
    [2, { name: "Felipe" }],
    [3, { name: "Chanchito" }]
];

let array = [{
    id: 1,
    name: 'Nicolas',
}, {
    id: 2,
    name: 'Felipe',
}, {
    id: 3,
    name: 'Chanchito',
}];


function toColletion(arr) {
    let colletion = [];
    for (idx in arr) {
        let elemento = arr[idx];
        colletion[idx] = elemento[1];
        colletion[idx].id = elemento[0];
    }
    return colletion;

}
let resultado = toColletion(pairs);
console.log(resultado);
