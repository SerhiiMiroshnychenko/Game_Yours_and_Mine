# definition of warriors class

from random import randint
from main import your_gold


class Warriors:
    """Common warriors class."""

    """Class attributes."""
    name: str = "yours"
    name_ukr: str = "твої"
    price: int = 10
    loots: int = 0
    damage_ind: int = randint(0, 6)
    index = 0
    gold = your_gold

    def __init__(self, squad_name, squad_number, squad_damage_ind):
        self.squad_name = squad_name
        self.warriors_number = squad_number * 100
        self.squad_damage_ind = squad_damage_ind

    @classmethod
    def buy_warriors(cls, squad_number):
        required_gold = cls.price * squad_number
        Warriors.index += 1
        squad_name = f"Squad {cls.index}"
        cls.gold -= required_gold
        warriors = Warriors(squad_name, squad_number, cls.damage_ind)
        return warriors
