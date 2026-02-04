from typing import Dict, List
from enum import Enum
from ex0.Card import Card
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
        ...

    def get_deck_stats(self) -> dict:
        ...
