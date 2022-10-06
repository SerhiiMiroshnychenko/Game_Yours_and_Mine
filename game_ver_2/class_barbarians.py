# definition of barbarians class

from random import randint
from class_enemies import Enemies
from main import day


class Barbarians(Enemies):
    """Definition of barbarians class."""

    name = "barbarians"
    name_ukr = "варвари"
    number = (day // 10) * (100 + 10 * randint(0, 11))  # треба трохи збільшити
    damage_ind = randint(1, 7)  # треба трохи збільшити
    loots = number // 20

