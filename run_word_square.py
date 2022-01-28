import sys  # to allow sys.exit()
import requests  # to allow reading text from URL


def main():  # main function - runs menu load function
    load_menu()


def load_menu():  # takes users choice and either runs, gives instructions or quits
    while True:
        print("\nMain Menu\n", "1. Instructions\n", "2. Run word square\n", "3. Quit\n")
        user_selection = input()
        if user_selection == "1":
            instructions()
        elif user_selection == "2":
            run_word_square()
        elif user_selection == "3":
            exit_program()
        else:
            print("\ninvalid input\n")


def instructions():  # prints instructions on how program functions
    print("This program creates a word square.")
    print("You must provide an integer to specify how many rows and columns the square will have.")
    print("This must be followed by a string of letters, the amount totalling to the integer squared.")
    print(" Example input: 4 aaccdeeeemmnnnoo\n")


def run_word_square():  # function to take user input and output a word square
    valid_user_input = get_user_input()  # call func to get valid user input to create word square with
    reference_dictionary = create_dictionary()  # call func to create a reference dictionary
    valid_words = get_valid_words(valid_user_input, reference_dictionary)  # call func to sort user input into valid words
    word_squares = create_word_squares(valid_words, valid_user_input[0])  # call func to take all valid words and return all possible word squares
    print(word_squares)


def get_user_input():  # asks user for user input and formats it
    while True:  # Loop until input valid
        print("Enter value to create word square:\n")
        user_input = str(input().replace(" ", "").lower())  # format to string, strip whitespace, set to lowercase
        str_length = len(user_input)  # set variable to length of inputted string
        if validate_user_input(user_input, str_length):  # if func returns true input is valid and returns value
            return user_input


def validate_user_input(user_input, str_length):  # validates if user input is usable
    if not user_input[0].isdigit():  # checks if first character of string is a number
        print("\nInvalid input - the first character must be a number\n")
        return False
    elif int(user_input[0]) == 0:  # checks if first character of string is greater than zero
        print("\nInvalid input - the first character can not be zero\n")
        return False
    elif (int(user_input[0]) ** 2) != str_length - 1:  # int value at index[0] of user_input squared must equal str_length
        print("\nInvalid input - input length must equal first character (number) squared\n")
        return False
    for current_char in user_input[1:str_length:1]:  # [start:end:step] iterates through input string from index[1]
        if not current_char.isalpha():  # evaluates if current char is alphabetical
            print("\nInvalid input - all characters after initial number must be letters\n")
            return False
        elif current_char == user_input[str_length - 1]:  # if all chars are alphabetical, returns valid input
            return True


def create_dictionary():  # creates reference dictionary for word square
    try:
        file = requests.get("http://norvig.com/ngrams/enable1.txt")  # gets online english dictionary file
    except requests.exceptions.RequestException as error:  # if error when getting file, exit
        sys.exit(error)
    dictionary = {}  # assign to a dictionary variable
    for line in file:  # loop through each line of the file
        decoded_line = line.decode("utf-8")  # decode each line into valid readable format
        for word in decoded_line.split():  # splits each line into individual words
            dictionary[word] = len(word)  # assigns each word to a key and length of the word to the value
    return dictionary  # return filled dictionary variable


def get_valid_words(valid_letters, dictionary):
    word_length = int(valid_letters[0])  # variable for specified word length
    valid_words = []  # variable to store all valid words to return
    for reference_word in dictionary:  # iterates through each word in reference dictionary
        if dictionary[reference_word] == word_length:  # test if current reference word length is equal to user specified word length
            valid_letter_list = []  # instantiates list to store the valid user inputted letters in
            for index in range(len(valid_letters)):  # loops through valid user letter string to assign each letter to a list element
                if not valid_letters[index].isdigit():  # if the current index is not a digit
                    valid_letter_list.append(valid_letters[index])  # add the letter to the list
            for reference_letter_index in range(len(reference_word)):  # iterates through each letter in valid reference word
                for current_letter_index in range(len(valid_letter_list)):  # iterates through each letter from user's inputted letters
                    if reference_word[reference_letter_index] == valid_letter_list[current_letter_index]:  # tests if letters in reference word are only letters in the valid letter list
                        valid_letter_list.remove(valid_letter_list[current_letter_index])  # removes the valid letter from list if they match to ensure only reference words using only one of each valid letter are returned
                        break  # break the loop and move to the next reference word
            if len(valid_letter_list) == ((len(valid_letters) - 1) - word_length):  # if all the letters from the reference word match the valid letter list it can be returned
                valid_words.append(reference_word)  # add the valid reference word to the valid words list to return
    return valid_words  # returns list of all valid words that can be made from the letters provided


def create_word_squares(word_list, word_length):

    def get_prefixes(prefix):
        nonlocal prefixes  # refers to prefix dictionary from outside function e.i. e.i. prefixes:{'c':[w1, w2, w3, w4]}
        if prefix in prefixes:  # if the current prefix is any key in the prefixes dictionary
            return prefixes[prefix]  # return the dictionary values (a word list) at the key the prefix value currently is i.e. prefix = c prefixes:{'c':[w1, w2, w3, w4]} returns [w1,w2,w3,w4]
        prefixes[prefix] = []  # sets prefix to dictionary key and value to a list e.i. prefixes:{'c':[]}
        for word in word_list:  # loops through every word in the master word list
            if word.startswith(prefix):  # if the current word starts with the current prefix e.i. word = 'aced, prefix = 'c' would be false
                prefixes[prefix].append(word)  # add the current word to the prefixes dictionary as a value in a list where the prefix is the key i.e. prefix = c, word = call , prefixes{'c':[call <- appends word here]}
        return prefixes[prefix]  # return the dictionary values (a word list) at the key the prefix value currently is i.e. prefix = c prefixes:{'c':[w1, w2, w3, w4]} returns [w1,w2,w3,w4]

    def backtracking(index, current_word_list, word_size):
        nonlocal full_squares  # allow reference to the full squares variable from outside function
        if len(current_word_list) == word_size:  # if length of list is equal to length of word return as full square
            full_squares.append(list(current_word_list))  # add the complete square as a list in the full_squares list fullsqr[[w1,w2,w3,w4]]
            return  # exit function back to next word in word_list given

        for word in current_word_list:  # loop through every word in the current list
            prefix = ''.join(word[index])  # sets prefix to the letter at the index of the current word in the list i.e. word:"aced" index:1 prefix = "c"

        # generator function
        for candidate in get_prefixes(prefix):  #
            current_word_list.append(candidate)
            backtracking(index + 1, current_word_list, word_size)
            current_word_list.pop()

    prefixes = {}  # create dictionary to store word prefixes in
    full_squares = []  # create list to store completed word squares in
    for words in word_list:  # loop through all words in the master word list
        backtracking(1, [words], word_length)  # passes current word as a 1 item list
    return full_squares  # return successful squares


def exit_program():  # Quits program
    sys.exit()


main()  # Calls main function
