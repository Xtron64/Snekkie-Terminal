import socket
import getpass
import os


def userInput():
    _ = input("You: ")
    return _


CURR_DIRR = os.getcwd()
PARENT_DIRR = os.path.dirname(CURR_DIRR)
if CURR_DIRR == PARENT_DIRR:
    path = CURR_DIRR
elif CURR_DIRR == '~':
    path = '~'
else:
    path = CURR_DIRR.replace(PARENT_DIRR, '')
open_keyword = "open"
exit_keyword = ("exit" or "leave")
calculate_keyword = ("calculate" or "calculator")
create_keyword = ("create" or "new")
keywords = (exit_keyword or calculate_keyword or create_keyword or open_keyword)


def main():
    global path, keywords, exit_keyword, calculate_keyword, create_keyword, open_keyword
    while True:
        print("What would you like to do?")
        choice: str = input("[" + getpass.getuser() + "@" + socket.gethostname() + " " + path + "]$ ")
        for keywords in choice.lower():
            for exit_keyword in choice.lower():
                exit()
            for calculate_keyword in choice.lower():
                import calculate
                continue
            for create_keyword in choice.lower():
                import createNew
                continue
            for open_keyword in choice.lower():
                import openFileOrFolder
                continue
        if keywords != choice.lower():
            print("That is not a valid command!")
            continue


if __name__ == '__main__':
    main()
