let user = {
    id: 1,
    name: 'Chanchito Feliz',
    age: 25,
};

for (let propiedad in user) {
    console.log(propiedad, user[propiedad]);
}


let animales = ['Chanchito Feliz', 'Dragon', 'Canguro'];
for (let indice in animales) {
    console.log(indice, animales[indice]);
}
