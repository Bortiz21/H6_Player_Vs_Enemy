from player import Player
from project_enemy import Enemy

"""
player_1 = Player("pandalf", 100, 25, 78)
print(player_1.name)
print(player_1.health)
print(player_1.damage)
print(player_1.defense)
"""


def main():
    p_1 = Player("juan", 100, 20,80)
    p_1.attack(Enemy)


if __name__ == '__main__':
    main()
