from Modules.morse_quiz_assist import MorseQuizAssist
import random

class MorseQuiz:
    def __init__(self):
        self.level_dict = {'Easy': 'morse_quiz_easy.tsv',
                           'Medium': 'morse_quiz_medium.tsv',
                           'Hard': 'morse_quiz_hard.tsv',
                           'Expert': 'morse_quiz_expert.tsv'}

    def morse_quiz_run(self,morse_settings):
        while True:
            print("Please select difficulty level:")
            i = 1
            for key in self.level_dict:
                print(f"({i}) {key}")
                i += 1
            difficulty = input("\nType the number corresponding to the level:\n")
            if difficulty.isnumeric():
                difficulty = int(difficulty)
                if 1 <= difficulty <= len(self.level_dict):
                    break
            print("Incorrect input, Please try again:")

        while True:
            quiz_style= input("Would you like the questions to:\n"
                              "(1) have options.\n"
                              "(2) guess directly?\n")
            match quiz_style:
                case "1":
                    quiz_options(self,difficulty,morse_settings)
                    break
                case "2":
                    quiz_guess(self,difficulty,morse_settings)
                    break
                case _:
                    print("Invalid input, Try again.")

def quiz_options(self,difficulty,morse_settings):
    quiz_assist = MorseQuizAssist(difficulty,self.level_dict)
    for answer, question in random.sample(
            list(quiz_assist.m_quiz.items()),
            quiz_assist.score_max):
        options_list = [item[0] for item in random.sample(
            list(quiz_assist.m_quiz.items()),
            4)]
        if not answer in options_list:
            options_list[0] = answer
        while True:
            question = question.translate(str.maketrans(
                ".-",
                f"{morse_settings["dot"]}{morse_settings["dash"]}"))
            print(question)
            i = 1
            for key in options_list:
                print(f"({i}) {key}")
                i += 1
            print(f"Enter (exit) to exit.\n")
            user_guess = input("Please select an answer:\n")
            if user_guess == "exit":
                break
            if user_guess.isnumeric():
                user_guess = int(user_guess)
                if 1 <= user_guess <= len(options_list):
                    if options_list[user_guess-1] == answer:
                        quiz_assist.correct(answer)
                        break
                    else:
                        quiz_assist.incorrect(answer,question)
                        break
            print("Incorrect input, Please try again:")
        if user_guess == "exit":
            break
        quiz_assist.current_score()
    quiz_assist.quiz_finish()


def quiz_guess(self,difficulty,morse_settings):
    quiz_assist = MorseQuizAssist(difficulty,self.level_dict)
    for answer, question in random.sample(
            list(quiz_assist.m_quiz.items()),
            quiz_assist.score_max):
        while True:
            question = question.translate(str.maketrans(
                ".-",
                f"{morse_settings["dot"]}{morse_settings["dash"]}"))
            player = input(f"Decode the following Morse Code\n"
                           f"(Letters, Numbers and Spaces only):\n"
                           f"{question}\n"
                           f"Enter (exit) to exit.\n").lower()
            error_chars = []
            for char in player:
                if not (char.isalnum() or char.isspace()):
                    error_chars.append(char)
            if not error_chars:
                break
            else:
                print(f"The following character/s are invalid:\n"
                      f"{set(error_chars)}\n"
                      f"Try again.")
        if player == answer:
            quiz_assist.correct(answer)
        elif player == "exit":
            break
        else:
            quiz_assist.incorrect(answer, question)
        quiz_assist.current_score()
    quiz_assist.quiz_finish()