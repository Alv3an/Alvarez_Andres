//Funciones Superiores

// const mayorQue = (a, b) => { return a > b }
// console.log(mayorQue(3, 2))
// const mayorQue10 = (n) => { mayorQue(n, 10) }
// console.log(mayorQue(3))

//JS tiene funciones de orden superior integradas

//Foreach
const numeros = [1, 2, 3, 4, 5];
numeros.forEach((item) => console.log(item * item));

//find
const arrayObject = [
    { id: 1, nombre: 'Ana', edad: 30 },
    { id: 2, nombre: 'Pedro', edad: 20 },
    { id: 3, nombre: 'Jose', edad: 45 }
];
//find
const salida_01 = arrayObject.find((item) => item.id === 3);
console.log(salida_01);
//filter
const salida_02 = arrayObject.filter((item) => item.edad > 25);
console.log(salida_02);
//some
const salida_03 = arrayObject.some((item) => item.edad < 20);
console.log(salida_04);
//every
const salida_04 = arrayObject.every((item) => item.edad > 20);
console.log(salida_04);
//map
const salida_05 = arrayObject.map((item) => item.nombre > 20);
console.log(salida_05);
//reduce
const salida_06 = arrayObject.reduce((total, item) => total + item.nombre > 20);
console.log(salida_06);
//sort
const salida_07 = arrayObject.sort((a, b) => a.edad - b.edad);
console.log(salida_07);
const salida_08 = arrayObject.sort((a, b) => b.edad - a.edad);
console.log(salida_08);
