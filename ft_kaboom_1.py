import alchemy.grimoire.dark_spellbook


def main():
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print(alchemy.grimoire.dark_spellbook.dark_spell_record(
        "Fantasy", "Earth, wind, and fire"))


if __name__ == "__main__":
    main()
