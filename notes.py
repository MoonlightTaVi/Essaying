import os
from datetime import datetime

import util.vigenere as vigenere
import util.app_runner as app_runner


raw_name = "note.txt"
encrypted_name = "secret.txt"


def read(filename) -> str:
    content: str
    with open(filename, 'r') as f:
        content = f.read()
    return content

def write(filename, content):
    with open(filename, 'w') as f:
        f.write(content)


def main():
    keyword = input("Enter password: ")
    content: str = ""
    if os.path.exists(encrypted_name):
        content = read(encrypted_name)
        encrypt = vigenere.decrypt(content, keyword)
        write(raw_name, encrypt)
        os.remove(encrypted_name)
    elif os.path.exists(raw_name):
        content = read(raw_name)
        encrypt = vigenere.encrypt(content, keyword)
        write(encrypted_name, encrypt)
        os.remove(raw_name)
    else:
        lines = [
            "Type your secret text here!",
            "Then perform the operation again."
        ]
        write(raw_name, "\n".join(lines))
        print("Look at you directory!")

    print("# Operation complete")


if __name__ == "__main__":
    app_runner.run(main)


