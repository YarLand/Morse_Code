from morse_parser import MorseParser
from morse_quiz import MorseQuiz

morse_parser = MorseParser()
morse_quiz = MorseQuiz()

default_characters = {"dot": ".",
                      "dash": "-"}

morse_settings = {"dot": default_characters["dot"],
                  "dash": default_characters["dash"]}


def format_change(default_characters):
    global morse_settings

    for char, value in default_characters.items():
        while True:
            char_change = input(f"Please input the new {char} character: \n"
                                f"(Default: '{value}', leave blank to cancel)\n")
            if len(char_change) > 1:
                print("Expected only 1 character, Restarting...")
            elif char_change == "":
                break
            else:
                if char == "dot":
                    morse_settings["dot"] = char_change
                if char == "dash":
                    morse_settings["dash"] = char_change
                break

def define_message():
    message_text = input("Please enter the message:\n")
    return message_text

while True:
    menu_main_choice = input("Welcome to the Python Morse Code Project!\n"
                             "Would you like to?: \n"
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
            morse_parser.debug_show_dict()
        case "C":
            format_change(default_characters)
        case "Q":
            morse_quiz.morse_quiz_run(morse_settings)
        case "X":
            break
        case _:
            print("Invalid Choice, please try again.\n")


# morse_parser.encode("hi lol")
#
# morse_parser.decode(".... .. / .-.. --- .-..")