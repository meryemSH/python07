from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    print("Playing Arcane Warrior (Elite Card):\n")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=4,
        rarity="Epic",
        attack=5,
        defense=3,
        mana=7
    )

    print("Combat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(5))

    print("\nMagic phase:")
    print("Spell cast:", elite.cast_spell("Fireball", ['Enemy1', 'Enemy2']))
    print("Mana channel", elite.channel_mana(3))

    print("\nMultiple interface implementation successful!")


main()
