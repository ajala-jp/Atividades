function aniversario(){
        var hoje = new Date()
        var dataAlvo = new Date("2005/06/07")
        var idade = hoje.getFullYear() - dataAlvo.getFullYear()
        if (hoje.getMonth()-1 < dataAlvo.getMonth()-1 || hoje.getMonth() == dataAlvo.getMonth() && hoje.getDate() < dataAlvo.getDate()){
            idade--;
        }return idade < 0 ? "idade errada" : idade
   
}
console.log(aniversario())



/* Professor, é o mesmo código mas eu quis encurtar ele */

function aniversario2(){var hoje = new Date(), dataAlvo = new Date("2005/06/07"), idade = hoje.getFullYear() - dataAlvo.getFullYear()
        if (hoje.getMonth()-1 < dataAlvo.getMonth()-1 || hoje.getMonth() == dataAlvo.getMonth() && hoje.getDate() < dataAlvo.getDate()){
            idade--;}return idade < 0 ? "idade errada" : idade}console.log(aniversario())

