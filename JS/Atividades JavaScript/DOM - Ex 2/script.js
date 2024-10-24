const botao1 = document.getElementById('b2')
var contador = 0
botao1.addEventListener('click',function(){
    contador++;
    document.getElementById('num').innerHTML =`Cliques : ${contador}`})


const botao2 = document.getElementById('b3')
botao2.addEventListener('click',function(){
    document.getElementById('num').innerHTML = `Cliques : ${contador}`
    if(contador > 0){
        contador--;
    }

    else if(contador == 0){
        alert("Número ZERO é o limite")
    }
})