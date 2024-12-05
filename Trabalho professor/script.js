const htp = document.getElementById('htp')
const baixo = document.getElementById('baixo')
const acertou = document.getElementById('acertou')
const nomepokemon = document.getElementById('nomepokemon')






async function Pokemonid(){
    try{
        const imagempk = document.getElementById('imagempk')
        const imagempk2 = document.getElementById('imagempk2')
        const tipo1 = document.getElementById('tipo1')
        const tipo2 = document.getElementById('tipo2')
        const hab1 = document.getElementById('hab1')
        const hab2 = document.getElementById('hab2')
        

        function idpoke(){
            return Math.floor(Math.random() * (807 - 1 + 1)) +1;
        }

        let pokedex = idpoke()
        console.log(pokedex)

        
        const pokemon = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokedex}`);
        const data = await pokemon.json();
        console.log(data.name)

        imagempk.src = data.sprites.other.home.front_default
        

        document.addEventListener('keydown',function(event){
            if(event.key === 'Enter'){
                if(htp.value === data.name){
                    imagempk.className = 'imagempk-on'
                    nomepokemon.innerText = data.name.charAt(0).toUpperCase() + data.name.slice(1);
                    imagempk2.src = data.sprites.other.showdown.front_default
                    console.log(data.abilities.length)
                    if(data.types.length == 1){
                        tipo1.innerHTML = data.types['0'].type.name                     
                        tipo2.style.color = 'transparent' 

                        }else if(data.types.length == 2){
                        tipo1.innerHTML = data.types['0'].type.name
                        tipo2.innerHTML = data.types['1'].type.name

                        switch(data.types['1'].type.name){
                            case 'normal':
                                tipo2.style.backgroundColor = '#A4ACAF'
                                tipo2.style.color = 'white'
                                break
                            
                            case 'fairy':
                                tipo2.style.backgroundColor = '#FDB9E9'
                                tipo2.style.color = 'white'
                                break

                            case 'dark':
                                tipo2.style.backgroundColor = '#707070'
                                tipo2.style.color = 'white'
                                break
                            
                            case 'psychic':
                                tipo2.style.backgroundColor = '#F366B9'
                                tipo2.style.color = 'white'
                                break
                            
                            case 'fire':
                                tipo2.style.backgroundColor = '#FD7D24'
                                tipo2.style.color = 'white'
                                break

                            case 'ghost':
                                tipo2.style.backgroundColor = '#7B62A3'
                                tipo2.style.color = 'white'
                                break

                            case 'steel':
                                tipo2.style.backgroundColor = '#9EB7B8'
                                tipo2.style.color = 'black'
                                break

                            case 'electric':
                                tipo2.style.backgroundColor = '#EED535'
                                tipo2.style.color = 'black'
                                break

                            case 'bug':
                                tipo2.style.backgroundColor = '#729F3F'
                                tipo2.style.color = 'white'
                                break
                            
                            case 'dragon':
                                tipo2.style.backgroundColor = '#53A3CF'
                                tipo2.style.color = 'white'
                                break

                            case 'ground':
                                tipo2.style.backgroundColor = '#F7DE3F'
                                tipo2.style.color = 'black'
                                break

                            case 'fighting':
                                tipo2.style.backgroundColor = '#D56723'
                                tipo2.style.color = 'white'
                                break
                            
                            case 'flying':
                                tipo2.style.backgroundColor = '#BDB9B8'
                                tipo2.style.color = 'black'
                                break
                        
                            case 'grass':
                                tipo2.style.backgroundColor = '#9BCC50'
                                tipo2.style.color = 'black'
                                break
                            
                            case 'poison':
                                tipo2.style.backgroundColor = '#B97FC9'
                                tipo2.style.color = 'white'
                                break
                            
                            case 'ice':
                                tipo2.style.backgroundColor = '#51C4E7'
                                tipo2.style.color = 'black'
                                break
                            
                            case 'rock':
                                tipo2.style.backgroundColor = '#A38C21'
                                tipo2.style.color = 'white'
                                break
                            
                            case 'water':
                                tipo2.style.backgroundColor = '#4592C4'
                                tipo2.style.color = 'white'
                                break

                        }

                    }

                    switch(data.types['0'].type.name){
                        case 'normal':
                            tipo1.style.backgroundColor = '#A4ACAF'
                            tipo1.style.color = 'white'
                            break
                        
                        case 'fairy':
                            tipo1.style.backgroundColor = '#FDB9E9'
                            tipo1.style.color = 'white'
                            break

                        case 'dark':
                            tipo1.style.backgroundColor = '#707070'
                            tipo1.style.color = 'white'
                            break
                        
                        case 'pysichic':
                            tipo1.style.backgroundColor = '#F366B9'
                            tipo1.style.color = 'white'
                            break
                        
                        case 'Fire':
                            tipo1.style.backgroundColor = '#FD7D24'
                            tipo1.style.color = 'white'
                            break

                        case 'ghost':
                            tipo1.style.backgroundColor = '#7B62A3'
                            tipo1.style.color = 'white'
                            break

                        case 'steel':
                            tipo1.style.backgroundColor = '#9EB7B8'
                            tipo1.style.color = 'black'
                            break

                        case 'electric':
                            tipo1.style.backgroundColor = '#EED535'
                            tipo1.style.color = 'black'
                            break

                        case 'bug':
                            tipo1.style.backgroundColor = '#729F3F'
                            tipo1.style.color = 'white'
                            break
                        
                        case 'dragon':
                            tipo1.style.backgroundColor = '#53A3CF'
                            tipo1.style.color = 'white'
                            break

                        case 'ground':
                            tipo1.style.backgroundColor = '#F7DE3F'
                            tipo1.style.color = 'black'
                            break

                        case 'fighting':
                            tipo1.style.backgroundColor = '#D56723'
                            tipo1.style.color = 'white'
                            break
                        
                        case 'flying':
                            tipo1.style.backgroundColor = '#BDB9B8'
                            tipo1.style.color = 'black'
                            break
                    
                        case 'grass':
                            tipo1.style.backgroundColor = '#9BCC50'
                            tipo1.style.color = 'black'
                            break
                        
                        case 'poison':
                            tipo1.style.backgroundColor = '#B97FC9'
                            tipo1.style.color = 'white'
                            break
                        
                        case 'ice':
                            tipo1.style.backgroundColor = '#51C4E7'
                            tipo1.style.color = 'black'
                            break
                        
                        case 'rock':
                            tipo1.style.backgroundColor = '#A38C21'
                            tipo1.style.color = 'white'
                            break
                        
                        case 'water':
                            tipo1.style.backgroundColor = '#4592C4'
                            tipo1.style.color = 'white'
                            break

                    }

                    

                    
                    setTimeout(() => {
                       baixo.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }, 1200);
                    acertou.innerHTML = data.name
                    
                    
                }
            }
        })

        

    } catch(error){
        console.log('Sei la');
    }


}

Pokemonid()









