# This file is a blank for a pretty output

from prettytable import PrettyTable
from main import your_gold, my_gold, your_farms, my_farms, your_warriors, my_warriors

table = PrettyTable()
table.field_names = ['    Name    ', '     Yours (Твої)     ', '   Mine (Комп\'ютер)  ']
table.add_row(['    Gold (Золото)    ', your_gold, my_gold])
table.add_row(['    Farms (Ферми)    ', your_farms, my_farms])
table.add_row(['    Warriors (Воїни)    ', your_warriors, my_warriors])

print(table)

