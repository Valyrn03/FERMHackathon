# Handles the game loop
import json

from game_logic.player import Player, pull_abilities
from writer import write_file

player = Player()
ai_player = Player()
def initialize():
    player = Player()
    ai_player = Player()

previous_action: str = ""
'''
    HP\n
    \tAbility (Text Descriptor)\n
    \tAbility (Text Descriptor)\n
    \tAbility (Text Descriptor)\n
    \tActive Buffs <- list of strings
    AI Ability (Text Descriptor)
    \tActive AI Buffs <- list of strings
'''
def send_to_frontend():
    message = []
    message.append(str(player.hit_points))
    message.append(str(pull_abilities()))
    message.append(str([buff[0] for buff in player.buffs]))
    message.append(previous_action)
    message.append(str([buff[0] for buff in ai_player.buffs]))

    state: int = write_file(json.dumps(message))
    while state == 1:
        write_file(json.dumps(message))

def receive_from_frontend(ai_action: str, json_user_input: str):
    chosen_ability = json.loads(json_user_input)[0]
    action: str = get_ai_action("")
    if chosen_ability[0].starts_with("Buff") or chosen_ability[0].starts_with("Debuff"):
        process_input(chosen_ability[0])
    elif action is "Attack" and chosen_ability[0] is "Defend":
        # Handle
    elif action is "Defend" and chosen_ability[0] is "Attack":
        # Handle
    elif action is "Attack" and chosen_ability[0] is "Attack":
        # Handle

def process_input(input: str):
    if input.startswith("Buff"):
        player.add_buff(input.split(" ")[1])
    elif input.startswith("Debuff"):
        ai_player.add_buff(input.split(" ")[1])

def get_ai_action(action: str):
    previous_action = action

print(send_to_frontend())