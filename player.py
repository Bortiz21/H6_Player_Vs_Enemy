from project_enemy import Enemy


class Player():
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
        name = input("Input a Name :")
        health = input("Input your health: ")
        damage = input("Input your damage: ")
        defense = input("Input your defense: ")

        print(f"\nYour name is: {name}")
        print(f"Your health is: {health}")
        print(f"Your damage is: {damage}")
        print(f"your defense is: {defense}")

        return name, health, damage, defense

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_defense(self):
        return self.defense

    def attack(self, Enemy):
        enemy_health = Enemy.HP - (self.damage - Enemy.defense)
        print(f"{Enemy.name}'s health is now {enemy_health}!")