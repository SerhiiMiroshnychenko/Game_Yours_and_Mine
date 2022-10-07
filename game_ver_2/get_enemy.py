# function that creates an army of enemies
from random import randint
from class_computer import Computer
from class_nomads import Nomads
from class_hunters import Hunters
from class_barbarians import Barbarians


def get_enemy(day: int, my_warriors: int, your_warriors: int):
    """Create an army of enemies."""

    list_of_enemies = []

    if day % 50 == 0 and day > 0:  # умова
        black_hunters = Hunters()  # визначення хто вороги
        list_of_enemies.append(black_hunters)
    if day % 10 == 0 and day > 0:  # умова
        barbarians = Barbarians()  # визначення хто вороги
        list_of_enemies.append(barbarians)
    if randint(0, 10) == 0 and day > 0:  # умова
        nomads = Nomads()  # визначення хто вороги
        list_of_enemies.append(nomads)
    if my_warriors > your_warriors:  # умова
        computer = Computer()  # визначення хто вороги
        list_of_enemies.append(computer)

    return list_of_enemies
