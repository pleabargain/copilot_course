# create a function that takes user input as an integer
def get_user_input():
    # get user input
    length_of_side = input("Enter an integer: ")
    # call the main function
    main(length_of_side)

# create a function that takes length of side as an argument and draw an asterisk diamond
def main(length_of_side):
    # convert length_of_side to an integer
    length_of_side = int(length_of_side)
    # create a list of integers from 1 to length_of_side
    list_of_integers = list(range(1, length_of_side + 1))
    # create a list of integers from length_of_side - 1 to 1
    list_of_integers2 = list(range(length_of_side - 1, 0, -1))
    # combine the two lists
    list_of_integers = list_of_integers + list_of_integers2
    # create a list of strings
    list_of_strings = []
    # loop through the list of integers
    for i in list_of_integers:
        # create a string of spaces
        spaces = " " * (length_of_side - i)
        # create a string of asterisks
        asterisks = "*" * (2 * i - 1) + "\n"
        # combine the spaces and asterisks
        string = spaces + asterisks
        # add the string to the list of strings
        list_of_strings.append(string)
    # print the list of strings
    print(*list_of_strings, sep = "")
#call the function
get_user_input()