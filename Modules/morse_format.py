import os
import pickle


class MorseFormat:
    # Loads the format settings from a pickle file
    def load_format(self,morse_settings):
        # Checks if file exists.
        if os.path.isfile("./data.pickle"):
            with open('data.pickle', 'rb') as file:
                morse_settings = pickle.load(file)
        # If file does not exist,
        # Create one from the default settings
        else:
            with open('data.pickle', 'wb') as file:
                pickle.dump(morse_settings, file)
        return morse_settings

    # Change the format of the dots and dashes
    def format_change(self,default_characters,morse_settings):
        # Repeat for the dots and dashes
        for char, value in default_characters.items():
            while True:
                # Prompt the user to input a new character
                # for the displayed type
                char_change = input(f"Please input the new {char} character: \n"
                                    f"(Default: '{value}', leave blank to cancel)\n")
                # If detected more than 1 character,
                # Restart the process for the current type.
                if len(char_change) > 1:
                    print("Expected only 1 character, Restarting...")
                # If prompt is empty,
                # don't change the settings of the displayed type.
                elif char_change == "":
                    break
                else:
                    # If Input is applicable,
                    # Then change according to the displayed type.
                    if char == "dot":
                        morse_settings["dot"] = char_change
                    if char == "dash":
                        morse_settings["dash"] = char_change
                    if char == "slash":
                        morse_settings["slash"] = char_change
                    break
        while True:
            # Prompt the user to save as a file
            # that can be loaded in future runs.
            input_save = input("Save changes for future use?\n"
                               "(Y)es\n"
                               "(N)o\n")
            match input_save.upper():
                case "Y":
                    # If Yes, Saves the file
                    with open('data.pickle', 'wb') as file:
                        pickle.dump(morse_settings, file)
                    break
                case "N":
                    # If No, then just exit the loop
                    break
            # If the input is not valid for this selection,
            # Then prompt the user to try again and restart the loop
            print("Invalid input, please try again")
        return morse_settings