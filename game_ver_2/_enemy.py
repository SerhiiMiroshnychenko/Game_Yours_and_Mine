# definition of enemy class

from random import randint
from main import my_warriors, your_warriors


class AnArmyOfEnemies:
    """Common enemy class."""

    def __init__(self, day):
        self.day = day

    def get_name_of_enemy(self):
        """Determine the name of the enemies."""
        if self.day % 50 == 0 and self.day > 0:
            name_of_enemy = "black_hunters"
        elif self.day % 10 == 0 and self.day > 0:
            name_of_enemy = "barbarians"
        elif randint(0, 10) == 0 and self.day > 0:
            name_of_enemy = "nomads"
        elif my_warriors > your_warriors:
            name_of_enemy = "computer"

    number = 0
    damage_ind = 0
    loots = 0
