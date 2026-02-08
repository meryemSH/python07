from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")

    result = engine.simulate_turn()

    hand = [
        factory.create_creature(),
        factory.create_creature(),
        factory.create_spell(),
    ]

    formatted_hand = [
        f"{card["name"]} ({card["cost"]})"
        for card in hand
    ]
    print("Hand:", formatted_hand)

    print("\nTurn execution:")

    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", result["Actions"])

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
        )


main()
