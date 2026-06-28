# from .light_spellbook import light_spell_allowed_ingredients
import alchemy.grimoire as grimoire


def validate_ingredients(ingredients: str) -> str:
    for i in grimoire.light_spell_allowed_ingredients():
        if (i in ingredients):
            return (ingredients + "VALID")
    return ingredients + "INVALID"
