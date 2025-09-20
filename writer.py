import json

from game_logic.game import send_to_frontend


def write_file(string_input: dict) -> int:
    file = open("state.txt", "r+")
    state: dict = json.loads(file.read())
    if state[0] == 1:
        file.close()
        return 1

    output = send_to_frontend()
    output["lock"] = 1
    file.write(json.dumps(output))
    file.close()
    return 0

def read_file() -> str | None:
    file = open("state.txt", "r+")
    state: dict = json.loads(file.read())
    if state[0] == 0:
        file.close()
        return None

    file.close()
    return state["action"]