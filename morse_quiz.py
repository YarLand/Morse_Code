from morse_dict import MorseDict
from morse_parser import MorseParser
import random

morse_dict = MorseDict()
morse_parser = MorseParser()

class MorseQuiz:

    def __init__(self):
        self.m_quiz = morse_dict.MorseInit("morse_quiz_debug.tsv")


    def morse_quiz_run(self):
        score_max = len(list(self.m_quiz.items()))
        score_user = 0
        for answer, question in random.sample(list(self.m_quiz.items()),score_max):
            player = input(f"Decode the following Morse Code:\n{question}\nenter (X) to exit\n")
            if player.lower() == answer:
                print(f"Correct! It was: '{answer}'!")
                score_user += 1
            elif player.lower == "x":
                break
            else:
                print(f"Incorrect, It was: '{answer}'.")
            print(f"Current Score: {score_user}\n")
        print("Quiz Over!\n"
              f"You got {score_user} out of {score_max} correct!")
        if score_user == score_max:
            print("A perfect score! Good job!\n")
        elif score_user < score_max:
            print("Try aiming for a perfect score, Good luck!\n")
