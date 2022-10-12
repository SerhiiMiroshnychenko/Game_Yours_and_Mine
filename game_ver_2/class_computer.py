# definition of computer troops (Mine) class

from random import randint
from class_enemies import Enemies
from class_your_warriors import Warriors
from main import my_warriors, my_gold


class Computer(Enemies):
    """Definition of computer troops class."""

    name = "computer"
    name_ukr = "мої"
    price = 20
    number = my_warriors
    damage_ind = randint(1, 6)
    loots = my_gold

