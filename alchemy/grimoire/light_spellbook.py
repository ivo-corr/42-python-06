# from .light_validator import validate_ingredients
import alchemy.grimoire as grimoire


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    if ("INVALID" not in grimoire.validate_ingredients(ingredients)):
        return (f"Spell recorded: {spell_name} ({ingredients} - VALID)")
    else:
        return (f"Spell rejected: {spell_name} ({ingredients} - INVALID)")
