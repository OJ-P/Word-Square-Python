import sys  # to allow sys.exit()
import isdigit


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
            exit_program()
        else:
            print("\ninvalid input")


def instructions():  # prints instructions on how program functions
    print("This program creates a word square.\n")
    print("You must provide an integer to specify how many rows and columns the square will have.\n")
    print("This must be followed by a string of letters, the amount totalling to the integer squared\n.")
    print(" Example input: 4 aaccdeeeemmnnnoo\n")


def run_word_square():
    sanitised_input = get_user_input()
    print("sanitised", sanitised_input)


def get_user_input():
    while True:
        print("Enter value to create word square:\n")
        user_input = str(input().replace(" ", "").lower())
        str_length = len(user_input) - 1
        if not user_input[0].isdigit():
            print("Invalid input - the first character must be a number")
            break
        elif int(user_input[0]) == 0:
            print("Invalid input - the first character can not be zero")
            break
        elif (int(user_input[0]) ** 2) != str_length:
            print("Invalid input - input length must equal first character (number) squared")
            break
        for current_char in user_input[1:str_length:1]:
            if not current_char.isalpha():
                print("Invalid input - all characters after initial number must be letters")
                break
            elif current_char == user_input[str_length]:
                return user_input


def exit_program():
    sys.exit()


main()
