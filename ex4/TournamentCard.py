from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self, card_id: str, name: str, cost: int, attack: int, defense: int
    ):

        super().__init__(name, cost, "Tournament")
        self.card_id = card_id
        self.attack_power = attack
        self.defense = defense

        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return {"played": self.name}

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "dammage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "incoming_damage": incoming_damage
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> dict:
        pass
