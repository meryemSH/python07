from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main():

    deck = Deck()

    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(ArtifactCard
                  ("Mana Crystal", 2, "Rare", 5, "Permanent: +1 mana per turn")
                  )
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))

    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    print("Deck stats:", deck.get_deck_stats())

    deck.shuffle()

    print("Drawing and playing cards:\n")
    while True:
        card = deck.draw_card()
        if card is None:
            break

        print(f"Drew: {card.name} ({card.get_type()})")
        print("Play result:", card.play({}))
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


main()
