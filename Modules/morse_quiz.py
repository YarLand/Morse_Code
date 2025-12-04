import random

from Modules.morse_quiz_assist import MorseQuizAssist


class MorseQuiz:
    def __init__(self):
        # Dictionary that stores the quiz files per difficulty name
        self.level_dict = {'Easy': 'morse_quiz_easy.tsv',
                           'Medium': 'morse_quiz_medium.tsv',
                           'Hard': 'morse_quiz_hard.tsv',
                           'Expert': 'morse_quiz_expert.tsv'}

    def morse_quiz_run(self,morse_settings):
        # Runs the quiz program
        bool_loop_diff = True
        while bool_loop_diff:
            # Displays the difficulty levels
            print("Please select difficulty level:")
            # Since ranges are 0-index,
            # We start with 1 for easier selection
            # in the number row on the keyboard
            i = 1
            # For each level,
            # display the selection number
            # and associated difficulty
            for key in self.level_dict:
                print(f"({i}) {key}")
                i += 1
            # Prompt difficulty selection
            difficulty = input("\nType the number corresponding to the level:\n")
            # Check if input is a number,
            # since we want to convert string to integer for comparison
            if difficulty.isnumeric():
                # Convert string to integer number
                difficulty = int(difficulty)
                # If the input is in range,
                # exit the loop process and proceed
                if 1 <= difficulty <= len(self.level_dict):
                    bool_loop_diff = False
            # If the input is incorrect,
            # display error and repeat loop
            print("Incorrect input, Please try again:")

        bool_loop_style = True
        while bool_loop_style:
            # Quiz style selection
            quiz_style= input("Choose answer format:\n"
                              "(1) Options\n"
                              "(2) Input\n")
            match quiz_style:
                # Options Style
                case "1":
                    quiz_options(self,difficulty,morse_settings)
                    bool_loop_style = False
                # Input Style
                case "2":
                    quiz_input(self, difficulty, morse_settings)
                    bool_loop_style = False
                # Invalid Input
                case _:
                    print("Invalid input, Try again.")

def quiz_options(self,difficulty,morse_settings):
    # Initiates the quiz assist module,
    # which facilitates common quiz functions.
    quiz_assist = MorseQuizAssist(difficulty,self.level_dict)
    # Randomly pick a question and answer
    # from the selected difficulty dictionary
    for answer, question in random.sample(list(quiz_assist.m_quiz.items()),
                                          quiz_assist.score_max):
        # Loads 4 random answers to the guesses
        options_list = [item[0] for item
                        in random.sample(list(quiz_assist.m_quiz.items()),4)]
        # If none of the 4 answers loaded
        # relates to the current question,
        # Then replace the first guess with
        # the correct answer
        if not answer in options_list:
            options_list[0] = answer
        # Randomize the list
        random.shuffle(options_list)
        # Question Loop
        bool_loop_question = True
        while bool_loop_question:
            # Converts morse question into the current format
            # and displays to the user
            question = question.translate(str.maketrans(".-/",
                                                        f"{morse_settings["dot"]}"
                                                        f"{morse_settings["dash"]}"
                                                        f"{morse_settings["slash"]}"))
            print(question)

            # Since ranges are 0-index,
            # We start with 1 for easier selection
            # in the number row on the keyboard
            i = 1
            # For each option,
            # display the selection number
            # and associated answer
            for key in options_list:
                print(f"({i}) {key}")
                i += 1
            print(f"Enter (exit) to exit.\n")
            # Prompt the user for option selection
            user_guess = input("Please select an answer:\n")
            # if the input is "exit" then quit the quiz.
            if user_guess == "exit":
                bool_loop_question = False
            # Check if input is a number,
            # since we want to convert string to integer for comparison
            if user_guess.isnumeric():
                # Convert string to integer number
                user_guess = int(user_guess)
                # Check if the input is in range
                if 1 <= user_guess <= len(options_list):
                    # If the option was the correct answer
                    if options_list[user_guess-1] == answer:
                        # Then the player is rewarded a point
                        quiz_assist.correct(answer)
                        bool_loop_question = False
                    # If it was incorrect
                    else:
                        # Then the user will be shown the correct answer
                        # and the error is added to a list of wrong answers
                        quiz_assist.incorrect(answer,question)
                        bool_loop_question = False
            # If the input was invalid, restart the current loop
            print("Incorrect input, Please try again:")
        # if the input is "exit" then quit the quiz.
        if user_guess == "exit":
            break
        # Displays the current score
        quiz_assist.current_score()
    # Displays that the quiz is done
    # and shows the score and errors of the player.
    quiz_assist.quiz_finish()


def quiz_input(self, difficulty, morse_settings):
    # Initiates the quiz assist module,
    # which facilitates common quiz functions.
    quiz_assist = MorseQuizAssist(difficulty,self.level_dict)
    # Randomly pick a question and answer
    # from the selected difficulty dictionary
    for answer, question in random.sample(
            list(quiz_assist.m_quiz.items()),
            quiz_assist.score_max):
        # Question Loop
        bool_loop_question = True
        while bool_loop_question:
            # Converts morse question into the current format
            # and displays to the user
            question = question.translate(str.maketrans(".-/",
                                          f"{morse_settings["dot"]}"
                                          f"{morse_settings["dash"]}"
                                          f"{morse_settings["slash"]}"))
            # Prompt the user for decoding input
            player = input(f"Decode the following Morse Code\n"
                           f"(Letters, Numbers and Spaces only):\n"
                           f"{question}\n"
                           f"Enter (exit) to exit.\n").lower()
            # Potential list of invalid characters.
            error_chars = []
            # For each character in input
            for char in player:
                # check if it isn't a character,
                # number or space
                if not (char.isalnum() or char.isspace()):
                    # If it isn't add to the error characters list
                    error_chars.append(char)
            # If the entire input message
            # passed the check, proceed with the quiz.
            if not error_chars:
                bool_loop_question = False
            # If there was one or more invalid characters,
            # Then show the user these characters and repeat the loop
            else:
                print(f"The following character/s are invalid:\n"
                      f"{set(error_chars)}\n"
                      f"Try again.")
        # If the input was the correct answer
        if player == answer:
            # Then the player is rewarded a point
            quiz_assist.correct(answer)
        # if the input is "exit" then quit the quiz.
        elif player == "exit":
            break
        # If it was incorrect
        else:
            # Then the user will be shown the correct answer
            # and the error is added to a list of wrong answers
            quiz_assist.incorrect(answer, question)
        # Displays the current score
        quiz_assist.current_score()
    # Displays that the quiz is done
    # and shows the score and errors of the player.
    quiz_assist.quiz_finish()