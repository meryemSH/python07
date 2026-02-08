from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return ["Enemy Player"]

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        for card in hand:
            if len(cards_played) < 2:
                cards_played.append(card["name"])
                mana_used += card["cost"]

            if "attack" in card:
                damage_dealt += card["attack"]

        return {
            "Strategy": self.get_strategy_name(),
            "Actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": self.prioritize_targets([]),
                "damage_dealt": damage_dealt
            }
        }
