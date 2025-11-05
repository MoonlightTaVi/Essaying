import os


def run(runnable):
    try:
        while True:
            runnable()
    except KeyboardInterrupt:
        print("\n[Quit]")
    except Exception as e:
        print('\nUnhandled exception' + str(e))
    input("Press any key to exit...")


def clear():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')