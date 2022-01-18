import sys  # to allow sys.exit()


def main():  # main function - runs menu load function
    load_menu()


def load_menu():  # takes users choice and either runs, gives instructions or quits
    while True:
        print("Main Menu\n", "1. Instructions\n", "2. Run word square\n", "3. Quit\n")
        user_selection = input()
        if user_selection == "1":
            instructions()
        elif user_selection == "2":
            run_word_square()
        elif user_selection == "3":
            sys.exit()
        else:
            print("\ninvalid input")


def instructions():  # prints instructions on how program functions
    print("This program creates a word square.\n")
    print("You must provide an integer to specify how many rows and columns the square will have.\n")
    print("This must be followed by a string of letters, the amount totalling to the integer squared\n.")
    print(" Example input: 4 aaccdeeeemmnnnoo\n")


def run_word_square():
    print("")


main()
