import os
from util.decryptor import Decryptor
import util.app_runner as app_runner
import util.essay as essay
import util.nametags as nametags

essay_file: str = "essay.txt"
essay_text: str
tags: list = []


def setup():
    global essay_text, tags
    if not os.path.exists(essay_file):
        essay.write_essay(essay_file)
        print("Your essay has been written.")
    essay_text = essay.read_essay(essay_file)
    tags = nametags.load()

def main():
    inp = input(">: ")
    decrypt = Decryptor(inp)
    decrypt.tags = tags
    password = decrypt.get_portion(essay_text)
    tag = decrypt.current_tag
    app_runner.clear()
    print(f"{tag} - {password}")


if __name__ == "__main__":
    setup()
    app_runner.run(main)

