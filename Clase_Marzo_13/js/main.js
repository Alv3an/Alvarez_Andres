let opcion;
let nota_n = 0;
const notas = [];
do {
    opcion = prompt("Desea agregar alguna nota: ").toLowerCase();
    switch (opcion) {
        case "si":
            nota_n = parseFloat(prompt("Ingrese la nota: "));
            notas.push(nota_n);
            break;
        case "no":
            const sumar_notas = () => {
                let prom = 0;
                for (let i = 0; i < notas.length; i++) {
                    prom += notas[i];
                }
                return prom;
            }
            const prom_notas = () => {
                return notas.length > 0 ? sumar_notas(notas) / notas.length : 0;
            }
            alert(`La nota promedio es: ${prom_notas()}`);
            break;
        default:
            break;
    }
    for (const element of notas) {
        console.log(typeof(element));
    }
    
} while (opcion != "no");