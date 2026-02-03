from ex0.CreatureCard import CreatureCard


def main():

    fire_info = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    mana_available = 6
    mana_insufficient = 3

    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    print(
        "CreatureCard Info:\n", fire_info.get_card_info()
        )
    print(f"\nPlaying Fire Dragon with {mana_available} mana available:")
    print("Playable:", fire_info.is_playable(mana_available))
    print("Play result:", fire_info.play({}))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", fire_info.attack_target("Goblin Warrior"))

    print(f"\nTesting insufficient mana ({mana_insufficient} available):")
    print("Playable:", fire_info.is_playable(mana_insufficient))

    print("\nAbstract pattern successfully demonstrated!")


main()
