from ex4.TournamentCard import TournamentCard
from random import choice


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.match_plyed = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner = choice([card1, card2])
        losses = card2 if winner == card1 else card1

        winner.update_wins(1)
        losses.update_losses(1)

        self.match_plyed += 1

        return {
            "winner": winner.card_id,
            "loser": losses.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": losses.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        cards_list = list(self.cards.values())
        Leaderboard = []

        i = 1
        for card in cards_list:
            line = (f"{i}. {card.name} - Rating: {card.calculate_rating()}"
                    f" ({card.get_rank_info()["Record"]})")
            Leaderboard.append(line)

            i += 1
        return Leaderboard

    def generate_tournament_report(self) -> dict:
        total_rating = 0

        for card in self.cards.values():
            total_rating += card.rating

        if len(self.cards) > 0:
            avg_rating = total_rating // len(self.cards)
        else:
            avg_rating = 0
        return {
            "total_cards": len(self.cards),
            "matches_played": self.match_plyed,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
