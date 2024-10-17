lista = [1,2,3,4,5,6]
var soma = 0

function somaDosPares(lista){
    for(i = 0; i <= lista.length; i++){

        if (lista[i] % 2 == 0){
            soma += lista[i]
            
        }
    
    }
    return soma
}


const Resultado = somaDosPares(lista)

console.log(Resultado) 