import os


def createNew():
    file_keyword = "file"
    directory_keyword = ("folder" or "directory")
    new_keywords = (file_keyword or directory_keyword)
    while True:
        print("Would you like to create a directory or text file?")
        choice = input("You: ")
        if choice.lower() != new_keywords:
            print("That is an invalid response!")
            continue
        elif choice.lower() == new_keywords:
            for file_keyword in choice.lower():
                print("What would you like to call the file?")
                file = input("You: ")
                if os.path.exists(file):
                    print("File already exists!")
                    continue
                else:
                    with open(file, 'w') as fp:
                        fp.write(input("What would you like to write into the text file? Don't use enter until you "
                                       "decide to finish, instead use '/n': "))
            for directory_keyword in choice.lower():
                print("What would you like the directory to be called?")
                dir_name = input("You: ")
                os.mkdir(dir_name)


createNew()
