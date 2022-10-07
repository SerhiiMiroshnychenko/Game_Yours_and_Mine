# thr file is for testing

from prettytable import PrettyTable
from main import day, my_warriors, your_warriors
from get_enemy import get_enemy

enemies = get_enemy(day, my_warriors, your_warriors)

enemies_table = PrettyTable()
enemies_table.field_names = ['       Enemy       ',
                             '       Ворог       ',
                             'Number (Кількість)',
                             '   Power (Сила)   ',
                             '  Gold (Золото)  ']
for enemy in enemies:
    enemies_table.add_row([enemy.name.title(), enemy.name_ukr.title(), enemy.number, enemy.damage_ind, enemy.loots])

print(enemies_table)
