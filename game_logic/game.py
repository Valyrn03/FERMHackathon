# Handles the game loop
import json
import random
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

import requests
from requests import Response

from game_logic.player import Player, pull_abilities
from writer import write_file, read_file

port = 8080

player = Player()
ai_player = Player()
def initialize():
    r: Response = requests.post("localhost:8080", data={"tester": 0})
    print("Printing: ")
    print(r.status_code)
    print("Code :)")
def initializeRound():
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
    message = {}
    message["player_hp"] = player.hit_points
    message["abilities"] = pull_abilities()
    message["player_buffs"] = [buff[0] for buff in player.buffs]
    message["ai_action"] = previous_action
    message["ai_buffs"] = [buff[0] for buff in ai_player.buffs]

    r = requests.post("localhost:" + str(port), message)

def receive_from_frontend(ai_action: str):
    r = requests.get("localhost:" + str(port))
    if(r == 200):
        print("ERROR IN ACCESSING PORT")
        return
    text = r.text
    chosen_ability = text["ability"]
    if previous_action.startswith("Buff") or previous_action.startswith("Debuff"):
        process_input_from_ai(previous_action)
    if chosen_ability[0].starts_with("Buff") or chosen_ability[0].starts_with("Debuff"):
        process_input_from_player(chosen_ability[0])
    elif previous_action is "Attack" and chosen_ability[0] is "Defend":
        # AI is attacking player
        ai_roll = roll() + ai_player.getAttack()
        player_roll = roll() + player.getDefense()
        if ai_roll > player_roll:
            player.take_damage(ai_roll - player_roll)
    elif previous_action is "Defend" and chosen_ability[0] is "Attack":
        # Player is attacking AI
        ai_roll = roll() + ai_player.getDefense()
        player_roll = roll() + player.getAttack()
        if player_roll > ai_roll:
            ai_player.take_damage(player_roll - ai_roll)
    elif previous_action is "Attack" and chosen_ability[0] is "Attack":
        player.take_damage(roll() + ai_player.getAttack())
        ai_player.take_damage(roll() + player.getAttack())
    player.resolve_buffs()
    ai_player.resolve_buffs()

def process_input_from_player(input: str):
    if input.startswith("Buff"):
        player.add_buff(input.split(" ")[1])
    elif input.startswith("Debuff"):
        ai_player.add_buff(input.split(" ")[1])

def process_input_from_ai(input: str):
    if input.startswith("Buff")\
            :
        ai_player.add_buff(input.split(" ")[1])
    elif input.startswith("Debuff"):
        player.add_buff(input.split(" ")[1])

def get_ai_action(action: str):
    previous_action = action
    #temporary while I work on the learning
    return random.sample(pull_abilities())

def roll():
    return random.randint(1, 10)

initialize()