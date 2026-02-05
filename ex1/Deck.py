from typing import List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import shuffle


class Deck():
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) == 0:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self.cards)

        creatures = sum(isinstance(card, CreatureCard) for card in self.cards)
        spells = sum(isinstance(card, SpellCard) for card in self.cards)
        artifacts = sum(isinstance(card, ArtifactCard) for card in self.cards)

        avg_cost = (
            sum(card.cost for card in self.cards) / total if total > 0 else 0
            )

        avg_cost = round(avg_cost, 1)
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
