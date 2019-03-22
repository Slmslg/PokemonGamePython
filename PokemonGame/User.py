from PokemonGame.Pokemons import Pokemons


class User(Pokemons):
    liste = []
    user_secim_index_list = []
    kontrol = False
    def showPokemons(self):
        print(Pokemons.PokeList)

    def showMyPokemons(self):
        print(self.liste)

    def myList(self,pokes):
        self.liste.append(pokes)

    def choose_poke_list(self,secim):
        self.user_secim_index_list.append(secim)

    def secim_kontrol(self,secim):
        for i in self.user_secim_index_list:
            if(i == secim):
                self.kontrol = True
                break
        if(len(self.user_secim_index_list) == 0):
            self.user_secim_index_list.append(secim)
        elif(self.kontrol == False):
            self.user_secim_index_list.append( secim )