from elements import create_fire, create_water
from .elements import create_air, create_earth


def healing_potion():
    return ("Healing potion brewed with "
            f"'{create_earth()}' and '{create_air()}'")


def strenght_potion():
    return ("Strenght potion brewed with "
            f"'{create_fire()}' and '{create_water()}'")
