# Imports libraries
from Modules.morse_parser import MorseParser
from Modules.morse_quiz import MorseQuiz
from Modules.morse_format import MorseFormat

# Assigns classes to variables
morse_parser = MorseParser()
morse_quiz = MorseQuiz()
morse_format = MorseFormat()

# Settings Variables
default_characters = {"dot": ".",
                      "dash": "-",
                      "slash": "/"}

# Set the morse settings to the default values
morse_settings = {"dot": default_characters["dot"],
                  "dash": default_characters["dash"],
                  "slash": default_characters["slash"]}

# Set the morse settings from a file,
# If the file didn't exist,
# Then the default values will be used
morse_settings = morse_format.load_format(morse_settings)


# Prompts the user to input the message,
# and returns as a string
def define_message():
    print(f"Current writing format: {morse_settings}")
    message_text = input("Please enter the message:\n")
    return message_text

print("Welcome to the Python Morse Code Project!")

# Menu Loop: As long as the user doesn't exit,
#            This will keep them inside the program
#            whenever they finish with a module.
while True:
    # Prompt and display choices
    # for the user to choose
    menu_main_choice = input("Would you like to?: \n"
                             "- (E)ncode\n"
                             "- (D)ecode\n"
                             "- (Q)uiz\n"
                             "- (V)iew supported characters\n"
                             "- (C)hange format\n"
                             "- e(X)it"
                             "\n")

    # Converts the user's choice
    # and turns the input into upper case
    # which makes the choice case-insensitive,
    # And matches the input to expected cases.
    match menu_main_choice.upper():

        # Decode
        case "D":
            morse_parser.message_proof(morse_parser.decode,
                                       define_message(),
                                       morse_settings)

        # Encode
        case "E":
            morse_parser.message_proof(morse_parser.encode,
                                       define_message(),
                                       morse_settings)

        # View supported characters
        case "V":
            morse_parser.show_dict(morse_settings)

        # Change format
        case "C":
            morse_format.format_change(
                default_characters,
                morse_settings)

        # Quiz
        case "Q":
            morse_quiz.morse_quiz_run(morse_settings)

        # Exit the program
        case "X":
            break

        # If the input doesn't match the cases above,
        # Then catch the odd input and prompt the user to try again.
        case _:
            print("Invalid Choice, please try again.\n")
