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


def run_word_square():  # creates word square
    valid_user_input = get_user_input()  # call func to get valid user input to create word square with


def get_user_input():  # asks user for user input and formats it
    while True:  # Loop until input valid
        print("Enter value to create word square:\n")
        user_input = str(input().replace(" ", "").lower())  # format to string, strip whitespace, set to lowercase
        str_length = len(user_input) - 1  # set variable to length of inputted string
        user_input = validate_user_input(user_input, str_length)  # call func to validate input
        if user_input:  # if func returns true input is valid and returns value
            return user_input


def validate_user_input(user_input, str_length):  # validates if user input is usable
    if not user_input[0].isdigit():  # checks if first character of string is a number
        print("Invalid input - the first character must be a number")
        return False
    elif int(user_input[0]) == 0:  # checks if first character of string is greater than zero
        print("Invalid input - the first character can not be zero")
        return False
    elif (int(user_input[0]) ** 2) != str_length:  # int value at index[0] of user_input squared must equal str_length
        print("Invalid input - input length must equal first character (number) squared")
        return False
    for current_char in user_input[1:str_length:1]:  # [start:end:step] iterates through input string from index[1]
        if not current_char.isalpha():  # evaluates if current char is alphabetical
            print("Invalid input - all characters after initial number must be letters")
            return False
        elif current_char == user_input[str_length]:  # if all chars are alphabetical, returns valid input
            return True


def exit_program():  # Quits program
    sys.exit()


main()  # Calls main function
