# definition of nomads class

from random import randint
from class_enemies import Enemies
from main import day


class Nomads(Enemies):
    """Definition of nomads class."""

    name = "nomads"
    name_ukr = "кочівники"
    number = (10 + randint(0, 21)) * day  # треба збільшити
    damage_ind = randint(1, 4)
    loots = number // 15
