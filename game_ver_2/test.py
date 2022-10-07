# thr file is for testing

from main import day, my_warriors, your_warriors
from get_enemy import get_enemy

enemies = get_enemy(day, my_warriors, your_warriors)
print(enemies)
for enemy in enemies:
    print(enemy.name)
    print(enemy.name_ukr)
    print(enemy.number)
    print(enemy.damage_ind)
    print(enemy.loots)
