const joysk = document.getElementById('joy')
const botaoo = document.getElementById('botaoum')
const botao2 = document.getElementById('botaodois')

document.addEventListener('keydown',function(event){
    if(event.key == 'ArrowDown'){
        joysk.src='midia/frame2tras.png'
        setTimeout(function() {
            joysk.src='midia/frame1normal.png'
        }, 100);
    }

    if(event.key =='ArrowUp'){
        joysk.src='midia/frame3frente.png'
        setTimeout(function() {
            joysk.src='midia/frame1normal.png'
        }, 100);
    }

    if(event.key == '1'){
        botaoo.src='midia/botao2.png'
        setTimeout(function(){
            botaoo.src='midia/botao1.png'
        }, 100);
    }

    if(event.key == '2'){
        botao2.src='midia/botao4.png'
        setTimeout(function(){
            botao2.src='midia/botao3.png'
        }, 100);
    }
})




