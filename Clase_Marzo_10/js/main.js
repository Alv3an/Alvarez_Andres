// const PI= 4.1416;

// const persona={nombre: "Juan", apellido: "paramo", edad: 18};
// const arreglo=[1,234,"ddfsd",[23,343],{nombre:"juan", apellido:"algo"}];

//-------------------------------------------------------------------------

// let nombre= prompt("Ingrese su nombre"); //jOptionPane.showInputDialog()
// let edad= prompt("Ingrese su edad"); //jOptionPane.showInputDialog()
// alert("Edad  "+Number(edad)); // jOptionPane.showMessageDialog()

// console.log("Hola "+nombre);  // SOUT
//'_' "_" `_`
// console.log(arreglo);

// let nombre="wilmer";
// console.log(`hola ${nombre}`);
// console.log('"hola mundo"');
// console.log("'hola mundo'");
// let varA=3;
// let varB="3";
// for (let index = 0; index < 10; index++) {
//     console.log(index);
// }

//----------------------------------------------------------------------------

// if(varA===varB){
//     console.log("Son iguales");
// }else{
//     console.log("Diferentes");

// }
// console.log(typeof(varA));
// console.log(typeof(varB));
// console.log(varB);

//----------------------------------------------------------------------------

// for (let index = 0; index < 10; index++) {
//     if(index===5){
//         continue
//     }
//     console.log(index);
// }

// const object ={nombre: "Wilmer", apellido: "patiño", edad:37};
// for (const key in object) {
//     console.log(object[key]);
// }

// const array =["Patiño", "Wilmer", 37];
// for (const index of array) {
//     console.log(index);
// }

//----------------------------------------------------------------------------

// let pass=123;
// let dato=1;
// while(dato!=pass){
//     dato=prompt("Ingrese la contraseña")
// }
// let password=123;
// let ingresado=1;

// do{
//     ingresado=prompt("Ingrese la contraseña con do-while")
// }while(ingresado!=password)

// let elemento=document.g.getElementById("texto");
// elemento.innerHTML+="Hola mundo desde JS"
// const array = ["Patiño", "Wilmer", 37];
// console.log(array.reverse());
// console.log(array);

//------------------------------------Ejercicio-------------------------------------------------------

// let edad_01 = prompt("ingrese la edad 1: ")
// let edad_02 = prompt("ingrese la edad 2: ")
// const Persona_01 = { nombre: "Andres", apellido: "Alvarez", edad_01 }
// const Persona_02 = { nombre: "Andrea", apellido: "Vera", edad_02 }
// console.log("Persona 1 - " + Persona_01.nombre + " " + Persona_01.apellido + " " + Persona_01.edad_01)
// console.log("Persona 2 - " + Persona_02.nombre + " " + Persona_02.apellido + " " + Persona_02.edad_02)
// if (Persona_01.edad_01 > Persona_02.edad_02) {
//     alert("La persona mayor es " + Persona_01.nombre + " " + Persona_01.apellido)
// } else if (Persona_02.edad_02 > Persona_01.edad_01) {
//     alert("La persona mayor es " + Persona_02.nombre + " " + Persona_02.apellido)
// } else {
//     alert("Ambos tienen la misma edad")
// }

//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<FUNCIONES>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

function suma(a, b) {
    return a + b;
}

//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<FUNCIONES ANONIMAS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

const resta = function (a, b) {
    return a - b;
}

//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ArrowFuntions>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
//()=>{}
//1. con un solo parametro
const tablaDel7 = (a) => { return a * 7 };
console.log(tablaDel7(5));
//2. Sin parametros necesita parentesis
const tablaDel7_v2 = () => {
    for (let i = 1; i <= 10; i++)
        console.log(" 7 x " + i + " = " + (7 * i));
}
tablaDel7_v2();
//3. Con una sola linea de cuerpo
//const resta_v3 = (a, b) => a - b ----------------- Sin llaves, se considera automaticamente que tiene return;
const resta_v3 = (a, b) => { return a - b };
console.log(resta_v3(5, 2))
