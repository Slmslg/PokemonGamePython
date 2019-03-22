from random import randint

from PokemonGame.Computer import Computer
from PokemonGame.Pokemons import Pokemons
from PokemonGame.User import User
from PokemonGame.Vs import Vs


class Start():
    print("Start")
    user = User()
    user.showPokemons()
    pokemons = Pokemons()
    pc = Computer()
    versus = Vs()
    secim_indexi = 0

    while(secim_indexi < 4):
        secim = int( input( "Lütfen bir pokemon seçiniz (1-28): " ) )
        user.myList( pokemons.PokeList[secim] )
        randomPoke = randint(1,28)
        randomPokemon = pokemons.PokeList[randomPoke]
        pc.PCListAdd(randomPokemon)
        secim_indexi +=1
    print("\n\n")
    secim_indexi = 0

    while(secim_indexi<4):
        print("Sizin Pokemonlarınız : ")
        user.showMyPokemons()
        print("Rakip Pokemonlar : ")
        pc.showComputerPokemons()
        print("\n")
        secim = int(input( "Lütfen bir pokemon seçiniz (1-28): " ))
        user.secim_kontrol(secim)
        if(user.kontrol == False):
            pc_secim = pc.computerlist[pc.pc_secim_index_list[secim-1]-1]
            user_secim = user.liste[secim-1]
            print(user_secim," vs ",pc_secim)
            user_index = versus.getKeysByValues(user_secim)
            pc_index = versus.getKeysByValues(pc_secim)
            versus.versus(user_index[0],pc_index[0],user_secim,pc_secim)
            secim_indexi +=1
        else:
            print(user_secim, " Pokemonunu daha önce seçtiniz... \n")
            user.kontrol = False


    versus.winner()

