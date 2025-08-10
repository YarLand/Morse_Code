from morse_dict import MorseDict
from morse_parser import MorseParser
import random

morse_dict = MorseDict()
morse_parser = MorseParser()

class MorseQuiz:

    def __init__(self):
        self.m_quiz = morse_dict.MorseInit("morse_quiz.tsv")


    def morse_quiz_run(self):
        for answer, question in random.sample(list(self.m_quiz.items()),len(list(self.m_quiz.items()))):
            player = input(f"Decode the following Morse Code:\n{question}\nenter (X) to exit\n")
            if player.lower() == answer:
                print(f"Correct! It was: '{answer}'!\n")
            elif player.lower == "x":
                break
            else:
                print(f"Incorrect, It was: '{answer}'.\n")
