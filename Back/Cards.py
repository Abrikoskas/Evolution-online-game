from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Habitat(Enum):
    water = auto()
    ground = auto()


@dataclass
class Property:
    def __init__(self, name: str, hunger_increase: int = 0, is_active: bool = False):
        self.name = name
        self.hunger = hunger_increase
        self.is_active = is_active


@dataclass
class Properties:
    def __init__(self):
        # Predator properties
        self.predator = Property(name="Хищник", hunger_increase=1)
        self.big_boy = Property(name="Большой", hunger_increase=1)
        self.sharp_vision = Property(name="Острое зрение")

        # None-predator properties
        self.fast = Property(name="Быстрый")
        self.scavenger = Property(name="Падальщик")
        self.camouflage = Property(name="Камуфляж")


class Card:
    """
    Class of card
    """
    def __init__(self, habitat: Habitat, *properties: Properties):
        """

        :param Habitat habitat: habitat of the card e.g. Habitat.water or Habitat.ground
        :param Properties properties: one or two properties from Properties dataclass
        """
        self.habitat = habitat
        self.properties = properties


class Animal(Card):
    """
    Class of animal card
    """
    def __init__(self, habitat: Habitat):
        super().__init__(habitat=habitat)
        self.hunger = 1
        self.properties = Properties()
