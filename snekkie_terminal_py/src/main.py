import socket
import getpass
import os


def userInput():
    _ = input("You: ")
    return _


def getShell(): 
    shell = os.environ['SHELL']
    return shell


def getShellSymbol():
    user = getpass.getuser()
    shell = getShell()
    if user.lower() == "root":
        if shell.lower == "/bin/bash":
            shellSymbol = "#"
        else:
            raise Exception("Lack of alternative shell support (only supports BASH)")
    else:
        if shell.lower() == "/bin/bash":
            shellSymbol = "$"
        else:
            raise Exception("Lack of alternative shell support (only supports BASH)")
    return shellSymbol
            

def getPath():
    curr_dirr = os.getcwd()
    if curr_dirr == '~':
        path = '~'
    else:
        path = curr_dirr
    return path


def main():
    while True:
        path = getPath()
        shellSymbol = getShellSymbol()
        print("What would you like to do?")
        command: str = input(f"[{getpass.getuser()}@{socket.gethostname()} {path}]{shellSymbol} ")
        if command == "exit":
            exit()
        else:
            os.system(command)


if __name__ == '__main__':
    main()
