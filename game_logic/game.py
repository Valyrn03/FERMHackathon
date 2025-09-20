# Handles the game loop
from game_logic.player import Player

player = Player()
aiPlayer = Player()
def initialize():
    player = Player()
    aiPlayer = Player()

'''
    HP\n
    \tAbility (Text Descriptor)\n
    \tAbility (Text Descriptor)\n
    \tAbility (Text Descriptor)\n
    \tActive Buffs <- list of strings
    AI Ability (Text Descriptor)
    \tActive AI Buffs <- list of strings
'''
def send_to_frontend() -> str:


def receive_from_frontend(json_input: str) -> str: