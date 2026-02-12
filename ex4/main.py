from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")

    platform = TournamentPlatform()

    cards = [
        TournamentCard("dragon_001", "Fire Dragon", 5, 8, 5),
        TournamentCard("wizard_001", "Ice Wizard", 4, 6, 4)
    ]

    for card in cards:
        print(f"{card.name} (ID: {card.card_id})")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.get_rank_info()["Record"]}")
        print()

    print("Creating tournament match...")
    for card in cards:
        platform.register_card(card)

    print("Match result:", platform.create_match("dragon_001", "wizard_001"))

    print("\nTournament Leaderboard:")
    for line in platform.get_leaderboard():
        print(line)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


main()
