# from .light_validator import validate_ingredients
import alchemy.grimoire.dark_spellbook
import alchemy.grimoire.dark_validator


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bars", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if ("INVALID" not in
        alchemy.grimoire.dark_validator.validate_ingredients(ingredients)):
        return (f"Spell recorded: {spell_name} ({ingredients} - VALID)")
    else:
        return (f"Spell rejected: {spell_name} ({ingredients} - INVALID)")
