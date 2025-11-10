import random

a_min: int = ord('A')
a_max: int = ord('a')
limit: int = 1114112


def encrypt(source: str, keyword: str, skip_chance: float = 0) -> str:
    encrypted: str = ""
    source = source.replace(" ", "")
    for i in range(len(source)):
        skip_roll: float = random.random()
        if skip_roll < skip_chance:
            continue
        ord1 = ord(source[i])
        start = 0#a_min if ord1 < a_max else a_max
        ord2 = ord(keyword[i % len(keyword)])
        ord3 = (ord1 + ord2 - start) % limit + start
        encrypted += chr(ord3)
    return encrypted

def decrypt(source: str, keyword: str) -> str:
    decrypted: str = ""
    for i in range(len(source)):
        ord1 = ord(source[i])
        start = 0#a_min if ord1 < a_max else a_max
        ord2 = ord(keyword[i % len(keyword)])
        ord3 = (ord1 - ord2 - start + limit) % limit + start
        decrypted += chr(ord3)
    return decrypted