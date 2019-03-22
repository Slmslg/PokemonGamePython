from PokemonGame.Pokemons import Pokemons


class Vs():
    savunma = [70, 71, 88, 79, 83, 85, 79, 77, 62, 67, 72, 81, 80, 91, 71, 69, 88, 75, 70, 94, 79, 66, 60, 63, 73, 89, 93, 63]
    saldiri = [94, 83, 80, 75, 86, 76, 92, 84, 93, 80, 75, 84, 87, 80, 84, 78, 73, 75, 90, 78, 78, 82, 77, 79, 70, 73, 64, 89]
    user_puan = 100
    pc_puan = 100
    poke = Pokemons()

    def versus(self,user_index,pc_index,user_pokemon,pc_pokemon):
        print(user_index)
        print(pc_index)
        savunma_vs = int(self.savunma[user_index-1]) - int(self.savunma[pc_index-1])
        print(savunma_vs)
        saldiri_vs = int(self.saldiri[user_index-1]) - int(self.saldiri[pc_index-1])
        print(saldiri_vs)
        self.user_puan = self.user_puan + (savunma_vs + saldiri_vs)
        self.pc_puan = self.pc_puan - (savunma_vs + saldiri_vs)
        fark  = savunma_vs+ savunma_vs
        self.kim_kazandi(fark,user_pokemon,pc_pokemon)

    def kim_kazandi(self,fark,user_pokemon,pc_pokemon):
        if(fark < 0):
            print("Kazanan : ",pc_pokemon)
        elif(fark == 0):
            print("Bu el berabere bitti....")
        else:
            print("Kazanan : ",user_pokemon)

    def winner(self):
        print("Skor : \nYou : ",self.user_puan,"\nPC : ",self.pc_puan)
        if(self.user_puan < self.pc_puan):
            print("Kazanan PC \n kendini geliştirmen gerekir dostum... Buralarda loser'lara yer yok. Defol git buradan...")
        elif(self.user_puan == self.pc_puan):
            print("Berabere kaldınız. \n Hadi yine şanslı günündesin dostum! Zorlayacak kıvama geldin.")
        else:
            print("Aferin lan kazandın hele şükür....")

    def getKeysByValues(self,listOfValues):
        listOfKeys = list()
        listOfItems = self.poke.PokeList.items()
        for item in listOfItems:
            if item[1] in listOfValues:
                listOfKeys.append(item[0])
        return listOfKeys