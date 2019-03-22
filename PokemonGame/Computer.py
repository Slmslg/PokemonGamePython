import random

from PokemonGame.Pokemons import Pokemons


class Computer(Pokemons):
    computerlist =[]
    pc_secim_index_list = [1,2,3,4]

    def showPCPokemons(self):
        print(Pokemons.PokeList)

    def showComputerPokemons(self):
        print(self.computerlist)

    def PCListAdd(self,pokes):
        self.computerlist.append(pokes)

    def randomPokeList(self):
        random.shuffle(self.pc_secim_index_list)
        print(self.pc_secim_index_list)
