from main import userInput, PARENT_DIRR


def openFileOrFolder():
    read = ('read' or 'r')
    write = ('write' or 'w')
    change = ('append' or 'a')
    file = 'file'
    folder = 'folder'
    print("What is the path to the file or folder you want to open?")
    dirr_path = userInput()
    print("Is it a file or folder?")
    file_folder = userInput()
    for file in file_folder.lower():
        print("What would you like to do with the file?")
        wantsToDo = userInput()
        for read in wantsToDo.lower():
            with open(dirr_path, 'r') as f:
                f.read()
                f.close()
        for write in wantsToDo.lower():
            with open(dirr_path, 'w') as f:
                print("What do you want to write in the file? Please use '/n' instead of enter to create newlines. "
                      "Press 'enter' to finish.")
                writtenText = userInput()
                f.write(writtenText)
                f.close()
        for append in wantsToDo.lower():
            with open(dirr_path, 'a') as f:
                f.writable()
                f.close()
    for folder in file_folder:
        with open(dirr_path) as opened_directory:
            CURR_DIRR = str(opened_directory)
            if CURR_DIRR == PARENT_DIRR:
                path = CURR_DIRR
            elif CURR_DIRR == '~':
                path = '~'
            else:
                path = CURR_DIRR.replace(PARENT_DIRR, '')
        return path


openFileOrFolder()
