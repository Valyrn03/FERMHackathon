# API:
    # Expose: Ability Options, Stats
    # Expose as string:
        # Sends: HP(AbilityOne, AbilityTwo, AbilityThree)
        # Returns: Ability
import random
ability_list = ["Attack", "Defend", "Strong Attack", "Debuff Defense", "Debuff Attack", "Buff Defense", "Buff Attack"]

class Player:
    hit_points: int = 50
    # BUFF ATT, BUFF DEF, DEBUFF ATT, DEBUFF DEF
    buffs: list[int] = [0 for i in range(3)]
    def __init__(self):
        self.hit_points = random.randint(40, 60)
        self.buffs = []

    def take_damage(self, damage: int):
        self.hit_points -= damage

    def add_buff(self, buff: str):
        if buff is "Buff Attack":
            self.buffs[0] = 3
        elif buff is "Buff Defense":
            self.buffs[1] = 3
        elif buff is "Debuff Attack":
            self.buffs[2] = 3
        else:
            self.buffs[3] = 3

    def resolve_buffs(self):
        for i in range(len(self.buffs)):
            self.buffs[i] += -1

    def is_dead(self) -> bool:
        return self.hit_points <= 0

    def getAttack(self) -> int:
        buff = 0
        if self.buffs[0] != 0:
            buff += 2
        if self.buffs[2] != 0:
            buff -= 2
        return buff

    def getDefense(self) -> int:
        buff = 0
        if self.buffs[1] != 0:
            buff += 2
        if self.buffs[3] != 0:
            buff -= 2
        return buff

# Returns a list of 3 abilities to choose from
def pull_abilities() -> list[str]:
    return random.sample(ability_list, 3)