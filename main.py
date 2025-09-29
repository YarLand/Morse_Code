# Imports libraries
from Modules.morse_parser import MorseParser
from Modules.morse_quiz import MorseQuiz
from Modules.morse_format import MorseFormat

# Assigns classes to variables
morse_parser = MorseParser()
morse_quiz = MorseQuiz()
morse_format = MorseFormat()

default_characters = {"dot": ".",
                      "dash": "-"}

morse_settings = {"dot": default_characters["dot"],
                  "dash": default_characters["dash"]}

morse_settings = morse_format.load_format(morse_settings)



def define_message():
    print(f"Current writing format: {morse_settings}")
    message_text = input("Please enter the message:\n")
    return message_text

print("Welcome to the Python Morse Code Project!")

while True:
    menu_main_choice = input("Would you like to?: \n"
                             "- (E)ncode\n"
                             "- (D)ecode\n"
                             "- (Q)uiz\n"
                             "- (V)iew supported characters\n"
                             "- (C)hange format\n"
                             "- e(X)it"
                             "\n")

    match menu_main_choice.upper():
        case "D":
            morse_parser.message_proof(
                morse_parser.decode,
                define_message(),
                morse_settings)
        case "E":
            morse_parser.message_proof(
                morse_parser.encode,
                define_message(),
                morse_settings)
        case "V":
            morse_parser.show_dict()
        case "C":
            morse_format.format_change(default_characters,morse_settings)
        case "Q":
            morse_quiz.morse_quiz_run(morse_settings)
        case "X":
            break
        case _:
            print("Invalid Choice, please try again.\n")
