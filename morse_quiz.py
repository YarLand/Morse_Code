from morse_dict import MorseDict
from morse_parser import MorseParser
import random

morse_dict = MorseDict()
morse_parser = MorseParser()

class MorseQuiz:

    def __init__(self):
        ### Todo: Replace the "morse_quiz_debug.tsv" with "morse_quiz_easy.tsv"
        self.level_dict = {'Easy': 'morse_quiz_debug.tsv',
                           'Medium': 'morse_quiz_medium.tsv',
                           'Hard': 'morse_quiz_hard.tsv',
                           'Expert': 'morse_quiz_expert.tsv'}


    def morse_quiz_run(self):
        while True:
            print("Please select difficulty level:")
            i = 1
            for key in self.level_dict:
                print(f"({i}) {key}")
                i += 1
            difficulty = input("\nType the number corresponding to the level:\n")
            if difficulty.isnumeric():
                difficulty = int(difficulty)
                if difficulty >= 1 and difficulty <= len((self.level_dict)):
                    break
            print("Incorrect input, Please try again:")

        while True:
            quiz_style= input("Would you like the questions to:\n"
                              "(1) have options\n"
                              "(2) guess directly?\n")
            match quiz_style:
                case "1":
                    quiz_options(difficulty)
                    break
                case "2":
                    quiz_guess(difficulty)
                    break
                case _:
                    print("Invalid input, Try again.")

def quiz_options(self,difficulty):
    pass


def quiz_guess(self,difficulty):
    m_quiz = morse_dict.MorseInit(list(self.level_dict.values())[difficulty - 1])
    score_max = len(m_quiz)
    score_user = 0
    dict_incorrect = {}
    for answer, question in random.sample(list(m_quiz.items()),score_max):
        while True:
            player = input(f"Decode the following Morse Code\n"
                           f"(Letters, Numbers and Spaces only):\n"
                           f"{question}\n"
                           f"Enter (exit) to exit\n").lower()
            error_chars = []
            for char in player:
                if not (char.isalnum() or char.isspace()):
                    error_chars.append(char)
            if error_chars == []:
                break
            else:
                print(f"The following character\s are invalid:\n"
                      f"{set(error_chars)}\n"
                      f"Try again.")
        if player == answer:
            print(f"Correct! It was: '{answer}'!")
            score_user += 1
        elif player == "exit":
            break
        else:
            print(f"Incorrect, It was: '{answer}'.")
            dict_incorrect[answer] = question
        print(f"Current Score: {score_user}\n")
    print("Quiz Over!\n"
          f"You got {score_user} out of {score_max} correct!")
    if score_user == score_max:
        print("A perfect score! Good job!\n")
    elif score_user < score_max:
        print("Here are the answers for the incorrect guesses:")
        for answer, question in dict_incorrect.items():
            print(f"- '{answer}' = '{question}'")
        print("Try aiming for a perfect score, Good luck!\n")
