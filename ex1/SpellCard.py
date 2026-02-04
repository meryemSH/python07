from enum import Enum
from ex0.Card import Card


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super.__init__(name, cost, rarity)
        self.effect_type = EffectType(effect_type)

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.resolve_effect([])

        }

    def resolve_effect(self, targets: list) -> dict:
        if self.effect_type == EffectType.DAMAGE:
            return "Deal 3 damage to target"

        if self.effect_type == EffectType.HEAL:
            return "Restore 5 health"

        if self.effect_type == EffectType.BUFF:
            return "Increase attack by 2"

        if self.effect_type == EffectType.DEBUFF:
            return "Reduce enemy attack by 2"

        return "Unknown effect"
