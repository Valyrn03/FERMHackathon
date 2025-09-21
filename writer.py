import json


def write_file(result: dict) -> int:
    file = open("state.txt", "r+")
    state: dict = json.loads(file.read())
    if state[0] == 1:
        file.close()
        return 1

    result["lock"] = 1
    file.write(json.dumps(result))
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