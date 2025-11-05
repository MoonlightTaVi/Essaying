import random


WIDTH: int = 120
HEIGHT: int = 60


a_min: int = ord('A')
a_max: int = ord('a')
alph_len: int = 26
allowed_symbols: str = "!#$%&()*+,-./:;<=>?@[\\]^_{|}~"


def write_essay(filepath: str):
    essay: str = generate_essay()
    with open(filepath, 'w') as f:
        f.write(essay)

def read_essay(filepath: str) -> str:
    essay: str
    with open(filepath, 'r') as f:
        essay = f.read()
    return essay.replace('\n', '')


def generate_essay() -> str:
    essay: list = []
    for _ in range(HEIGHT):
        essay.append(generate_line())
    return "\n".join(essay)


def generate_line() -> str:
    line: str = ""
    for _ in range(WIDTH):
        line += random_character()
    return line


def random_character() -> str:
    return random.choice([random_letter, random_digit, random_symbol])()

def random_letter() -> str:
    start: int = random.choice([a_min, a_max])
    offset: int = random.randint(0, alph_len)
    return chr(start + offset)

def random_digit() -> str:
    return str(random.randint(0, 9))

def random_symbol() -> str:
    return allowed_symbols[random.randint(0, len(allowed_symbols)-1)]