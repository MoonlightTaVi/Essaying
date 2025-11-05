from util.decryptor import Decryptor
import util.app_runner as app_runner
import util.essay as essay
import util.nametags as nametags

import util.wdir as wdir

essay_file: str = "essay.txt"
essay_text: str
tags: list = []


def setup():
    global essay_text, tags, essay_file
    essay_file = wdir.abs(essay_file)
    if not wdir.exists(essay_file):
        essay.write_essay(essay_file)
        print("Your essay has been written.")
    else:
        print('Essay already exists.')
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

