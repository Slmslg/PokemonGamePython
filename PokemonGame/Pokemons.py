class Pokemons():
    PokeList = {
        1: "Magmar",
        2: "Bulbasaur",
        3: "Squirtle",
        4: "Pidgeotto",
        5: "Zapdos",
        6: "Sandshrew",
        7: "Mew",
        8: "Moltres",
        9: "Psyduck",
        10: "Butterfree",
        11: "Exeggutor",
        12: "Electabuzz",
        13: "Cubone",
        14: "Hunter",
        15: "Charmendar",
        16: "Gloom",
        17: "Krabby",
        18: "Spearow",
        19: "Pikachu",
        20: "Golem",
        21: "Abra",
        22: "Vulpix",
        23: "Paras",
        24: "Staryu",
        25: "Golbat",
        26: "Electrode",
        27: "Diglet",
        28: "Drowzee"
    }
    liste = []

    def showPokemons(self):
        print(self.PokeList)

    def pokemon_listem(self):
        print("Pokemon Listesi : ")
        for key,value in self.PokeList.items():
            print(key,value)