# from .light_spellbook import light_spell_allowed_ingredients
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    for i in dark_spell_allowed_ingredients():
        if (i in ingredients):
            return (ingredients + "VALID")
    return ingredients + "INVALID"
