from morse_parser import MorseParser
from morse_quiz import MorseQuiz

morse_parser = MorseParser()
morse_quiz = MorseQuiz()

def define_message():
    message_text = input("Please enter the message:\n")
    return message_text

while True:
    menu_main_choice = input("Would you like to (E)ncode or (D)ecode Morse Code?\n"
                             "Please press the key relating to the first letter of the command.\n"
                             "Additional: e(X)it, (V)iew supported characters,(C)hange format\n"
                             "(Q)uiz\n")

    match menu_main_choice.upper():
        case "D":
            morse_parser.message_proof(morse_parser.decode,define_message())
        case "E":
            morse_parser.message_proof(morse_parser.encode,define_message())
        case "V":
            morse_parser.debug_show_dict()
        case "C":
            morse_parser.format_change()
        case "Q":
            morse_quiz.morse_quiz_run()
        case "X":
            break
        case _:
            print("Invalid Choice, please try again.\n")


# morse_parser.encode("hi lol")
#
# morse_parser.decode(".... .. / .-.. --- .-..")