
names: list = []

def load() -> list:
    global names
    if len(names) > 0:
        return names
    with open("names.txt", 'r') as f:
        for line in f:
            names.append(line.strip())
    return names