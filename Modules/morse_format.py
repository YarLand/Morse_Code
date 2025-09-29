import os
import pickle


class MorseFormat:
    def load_format(self,morse_settings):
        if os.path.isfile("./data.pickle"):
            with open('data.pickle', 'rb') as file:
                morse_settings = pickle.load(file)
        else:
            with open('data.pickle', 'wb') as file:
                pickle.dump(morse_settings, file)
        return morse_settings

    def format_change(self,default_characters,morse_settings):
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
        while True:
            input_save = input("Save changes for future use?\n"
                               "(Y)es\n"
                               "(N)o\n")
            match input_save.upper():
                case "Y":
                    # print("save")
                    with open('data.pickle', 'wb') as file:
                        pickle.dump(morse_settings, file)
                    break
                case "N":
                    break
            print("Invalid input, please try again")
        return morse_settings