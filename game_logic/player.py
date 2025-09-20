# API:
    # Expose: Ability Options, Stats
    # Expose as string:
        # Sends: HP(AbilityOne, AbilityTwo, AbilityThree)
        # Returns: Ability
import random
ability_list = ["Attack", "Defend", "Strong Attack", "Debuff Defense", "Debuff Attack", "Buff Defense", "Buff Attack"]

class Player:
    hit_points: int = 50
    buffs: list[tuple[str, int]] = []
    def __init__(self):
        self.hit_points = random.randint(40, 60)
        self.buffs = []

    def take_damage(self, damage: int):
        self.hit_points -= damage

    def add_buff(self, buff: str):
        self.buffs.append((buff, 3))

    def resolve_buffs(self):
        new_buffs: list[tuple[str, int]] = []
        for buff in self.buffs:
            if buff[1] > 0:
                new_buffs.append(buff)
        self.buffs = new_buffs

    def is_dead(self) -> bool:
        return self.hit_points <= 0

# Returns a list of 3 abilities to choose from
def pull_abilities() -> list[str]:
    return random.sample(ability_list, 3)