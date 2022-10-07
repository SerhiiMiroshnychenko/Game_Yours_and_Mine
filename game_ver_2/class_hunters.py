# definition of black hunters class

from random import randint
from class_enemies import Enemies
from main import day


class Hunters(Enemies):
    """Definition of black hunters class."""

    name = "black hunters"
    name_ukr = "Чорні Мисливці"
    number = 1000 * day // 50
    damage_ind = randint(5, 21)  # зробити більше шкоду
    loots = 1000
