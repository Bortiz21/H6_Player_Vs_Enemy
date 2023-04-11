class Player:

    """
    name = None
    health = None
    damage = None
    defense = None
    """

    def __init__(self, name, health, damage, defense):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

    def character_create(self):
        self.name = input("Input a Name :")  # WIP - working on character create, REMBER to upload to github!


