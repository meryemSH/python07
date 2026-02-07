from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy
            ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        hand = [
            self.factory.create_creature(),
            self.factory.create_creature(),
            self.factory.create_spell(),
        ]

        self.cards_created += len(hand)

        result = self.strategy.execute_turn(hand, [])
    def get_engine_status(self) -> dict:
        pass
fuck you