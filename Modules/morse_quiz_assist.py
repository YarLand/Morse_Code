from Modules.morse_dict import MorseDict

class MorseQuizAssist:
    def __init__(self,difficulty,level_dict):
        morse_dict = MorseDict()
        self.m_quiz = morse_dict.MorseInit(f"Data/Quiz/"
                                           f"{list(level_dict.values())[difficulty - 1]}")
        self.score_max = len(self.m_quiz)
        self.score_user = 0
        self.dict_incorrect = {}

    def correct(self, answer):
        print(f"Correct! It was: '{answer}'!")
        self.score_user += 1

    def incorrect(self, answer, question):
        print(f"Incorrect, It was: '{answer}'.")
        self.dict_incorrect[answer] = question

    def current_score(self):
        print(f"Current Score: {self.score_user}\n")

    def quiz_finish(self):
        print("Quiz Over!\n"
              f"You got {self.score_user} out of {self.score_max} correct!")
        if self.score_user == self.score_max:
            print("A perfect score! Good job!\n")
        elif self.score_user < self.score_max:
            print("Here are the answers for the incorrect guesses:")
            for answer, question in self.dict_incorrect.items():
                print(f"- '{answer}' = '{question}'")
            print("Try aiming for a perfect score, Good luck!\n")
