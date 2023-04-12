class Enemy(object):

    def __init__(self, species, HP, attack, defense):
        self.species = species
        self.HP = HP
        self.attack = attack
        self.defense = defense




class Minion(Enemy):

    def __init__(self):
        super(Minion, self).__init__("Minion", 10, 2, 1)

class Brawler(Enemy):

    def __init__(self):
        super(Brawler, self).__init__("Brawler", 30, 10, 5)

class Elite(Enemy):

    def __init__(self):
        super(Elite, self).__init__("Elite", 100, 20, 20)


#input("Choose what species you want to fight:\n1: Minion\n2: Brawler\n3: Elite\nSelection: ")