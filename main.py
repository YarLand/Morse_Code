# Imports libraries
from Modules.morse_parser import MorseParser
from Modules.morse_quiz import MorseQuiz
from Modules.morse_format import MorseFormat
from Modules.morse_settings import MorseSettings

# Assigns classes to variables
morse_parser = MorseParser()
morse_quiz = MorseQuiz()
morse_format = MorseFormat()
morse_settings = MorseSettings()

# Set the morse settings from a file,
# If the file didn't exist,
# Then the default values will be used
current_morse_settings = morse_format.load_format()

print("Welcome to the Python Morse Code Project!")


# Dictionary of Menu functions,
# Each letter holds an inner dictionary,
# Which consists of the relevant function, and the arguments needed to pass
dict_menu_func = {
    # Decode
    "D": {"function":morse_parser.decode,"arguments":(current_morse_settings,)},
    # Encode
    "E": {"function":morse_parser.encode,"arguments":(current_morse_settings,)},
    # View supported characters
    "V": {"function":morse_parser.show_dict,"arguments":(current_morse_settings,)},
    # Change format
    "C": {"function":morse_format.format_change,"arguments":(current_morse_settings,)},
    # Quiz
    "Q": {"function":morse_quiz.morse_quiz_run,"arguments":(current_morse_settings,)},
}

# Menu Loop: As long as the user doesn't exit,
#            This will keep them inside the program
#            whenever they finish with a module.
bool_loop_menu = True

while bool_loop_menu:
    # Prompt and display choices
    # for the user to choose,
    # The result will be converted to upper case
    menu_main_choice = input("Would you like to?: \n"
                             "- (E)ncode\n"
                             "- (D)ecode\n"
                             "- (Q)uiz\n"
                             "- (V)iew supported characters\n"
                             "- (C)hange format\n"
                             "- e(X)it"
                             "\n").upper()

    # Exit the program
    if menu_main_choice == "X":
        bool_loop_menu = False
        break

    # Matches the input to keys in a dictionary.
    dict_selection = dict_menu_func.get(menu_main_choice)

    # Checks if the option exists in the dictionary
    if dict_selection is not None:
        # Defines the arguments needed
        dict_selection_args = dict_selection["arguments"]

        # Calls the function with arguments, based on user choice
        dict_selection["function"](*dict_selection_args)

    else:
        # If the input doesn't match an entry in the dictionary,
        # Then catch the odd input and prompt the user to try again.
        print("Invalid Choice, please try again.")
