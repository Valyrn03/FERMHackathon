def write_file(string_input: str) -> int:
    file = open("state.txt", "r+")
    state = file.read()
    if state[0] == 1:
        return 1

    file.write(str(1) + "\n")
    file.write(string_input)
    return 0