# definition of my warriors class (Мої)

class Warriors:
    """Common my warriors class."""

    """Class attributes."""
    name: str = ""
    name_ukr: str = ""
    price: int = 0
    loots: int = 0
    damage_ind: int = 0

    @classmethod
    def buy_warrior(cls, squad_number):
        required_gold = cls.price * squad_number
        warriors = Warriors(squad_number)

    def __init__(self, squad_number):
        self.squad_number = squad_number








