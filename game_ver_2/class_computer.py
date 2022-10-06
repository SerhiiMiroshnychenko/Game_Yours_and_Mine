# definition of computer troops (Mine) class

from random import randint
from class_enemies import Enemies
from main import my_warriors, my_gold


class Computer(Enemies):
    """Definition of computer troops class."""

    name = "computer"
    name_ukr = "мої"
    number = my_warriors
    damage_ind = randint(1, 6)
    loots = my_gold

