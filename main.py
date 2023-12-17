import os

def print_yellow(text):
    print("\033[33m {}" .format(text))

def print_red(text):
    print("\033[31m {}" .format(text))

def print_blue(text):
    print("\033[34m {}" .format(text))

def clean():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def resetColour():
    print("\033[0m")

def main():
    clean()
    resetColour()
    print(" _________  _______   ________  _____ ______   ___  ________   ________  ___               ________  ________  ________    ")
    print("|\___   ___\\  ___ \ |\   __  \|\   _ \  _   \|\  \|\   ___  \|\   __  \|\  \             |\   __  \|\   __  \|\   __  \   ")
    print("\|___ \  \_\ \   __/|\ \  \|\  \ \  \\\__\ \  \ \  \ \  \\ \  \ \  \|\  \ \  \            \ \  \|\  \ \  \|\  \ \  \|\  \  ")
    print("     \ \  \ \ \  \_|/_\ \   _  _\ \  \\|__| \  \ \  \ \  \\ \  \ \   __  \ \  \            \ \   __  \ \   ____\ \   ____\ ")
    print("      \ \  \ \ \  \_|\ \ \  \\  \\ \  \    \ \  \ \  \ \  \\ \  \ \  \ \  \ \  \____        \ \  \ \  \ \  \___|\ \  \___| ")
    print("       \ \__\ \ \_______\ \__\\ _\\ \__\    \ \__\ \__\ \__\\ \__\ \__\ \__\ \_______\       \ \__\ \__\ \__\    \ \__\    ")
    print("        \|__|  \|_______|\|__|\|__|\|__|     \|__|\|__|\|__| \|__|\|__|\|__|\|_______|        \|__|\|__|\|__|     \|__|    ")
    print("                                                                                                                           ")
    print("                                                                                                        -by @AlmartDev     ")
    print("                                                                                                                           ")

    print_yellow("1. About")
    print_yellow("2. Progress Bar test")
    print_yellow("3. Install dependencies")
    print_yellow("4. Exit")

    print_blue("")

    user_input = input("Enter your choice: ")

    if user_input == "1":
        clean()
        print_red("ABOUT")
        print("")
        print_yellow("Basic terminal app for general purposes.")
        print_yellow("Version 1.0")


        input()
        main()
    elif user_input == "2":
        pass
    elif user_input == "3":
        clean()
        print_red("INSTALLING DEPENDENCIES")
        resetColour()
        os.system("pip install requirements.txt")

        main()
    elif user_input == "4":
        clean()
        exit()
    else:
        clean()
        print_red("Invalid option, please try again.")
        input()
        main()
            

main()
input()