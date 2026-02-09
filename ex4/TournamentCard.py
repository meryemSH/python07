from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        ...

    def defend(self, incoming_damage: int) -> dict:
        ...

    def get_combat_stats(self) -> dict:
        ...

    def calculate_rating(self) -> int:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict:
        pass
