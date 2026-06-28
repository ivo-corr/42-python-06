# from .light_spellbook import light_spell_allowed_ingredients
import alchemy.grimoire.dark_spellbook


def validate_ingredients(ingredients: str) -> str:
    for i in alchemy.grimoire.dark_spellbook.dark_spell_allowed_ingredients():
        if (i in ingredients):
            return (ingredients + "VALID")
    return ingredients + "INVALID"
