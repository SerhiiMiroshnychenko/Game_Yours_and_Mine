# definition of warriors class

from random import randint
#from main import your_gold


class YourWarriors:
    """Common your warriors class."""

    """Class attributes."""
    name: str = "yours"
    name_ukr: str = "твої"
    price: int = 10
    loots: int = 0
    damage_ind: int = randint(0, 6)
    index = 0

    @classmethod
    def set_index(cls):
        cls.index = YourWarriors.index + 1
        YourWarriors.index = cls.index





