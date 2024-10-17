const lista1 = [1,2,3,4,5]
const lista2 = [5,6,7,8,9,10]
var lista3 = []

for(i=0; i < lista1.length;i++){
    lista3.push(lista1[i])
}

for(j = 0; j < lista2.length; j++){
    lista3.push(lista2[j])
}

const lista4 = [...new Set(lista3)]

console.log(lista4)

