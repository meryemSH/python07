import random
from ex3.CardFactory import CardFactory
from ex0.Card import Card


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creatures = [
            {"name": "Fire Dragon", "cost": 5, "attack": 5},
            {"name": "Goblin Warrior", "cost": 2, "attack": 3}
        ]
        return random.choice(creatures)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return {"name": "Lightning Bolt", "cost": 3}

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return {"name": "Mana Ring"}

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for _ in range(size):
            deck.append(self.create_creature())

        return {"deck": deck}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
