let obj = {};
let obj2 = new Object();

/**
 * New array ();
 * new string ();
 * new Number ();
 * new Boolean ();
 */

function Usuario() {
    this.name = 'Chanchito Feliz';
}
let user = new Usuario();
console.log(user.name.constructor);

const s1 = " 1 + 1";
const s2 = new String("1+1");

// console.log(eval(s1), eval(s2));
console.log(s2.valueOf());