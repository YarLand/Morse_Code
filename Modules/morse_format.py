import os
import pickle
from Modules.morse_settings import MorseSettings

class MorseFormat:

    def __init__(self):
        morse_settings = MorseSettings()
        # Sets the default characters for reference
        self.default_characters = morse_settings.SettingsInit()

    # Saves the format settings into a pickle file
    def save_format(self,changes):
        with open('data.pickle', 'wb') as file:
            pickle.dump(changes, file)
        return changes

    # Loads the format settings from a pickle file
    def load_format(self):
        # Sets the current Morse settings
        current_morse_settings = {}
        # Checks if file exists.
        if os.path.isfile("./data.pickle"):
            with open('data.pickle', 'rb') as file:
                current_morse_settings = pickle.load(file)
        # If file does not exist,
        # Create one from the default settings
        else:
            current_morse_settings = self.save_format(self.default_characters)
        return current_morse_settings



    # Change the format of the dots and dashes
    def format_change(self,current_morse_settings):

        # Repeat for the dots and dashes
        for char, value in self.default_characters.items():
            bool_loop_format_change = True
            while bool_loop_format_change:
                # Prompt the user to input a new character
                # for the displayed type
                char_change = input(f"Please input the new {char} character: \n"
                                    f"(Current: '{current_morse_settings[char]}',\n"
                                    f"Default: '{value}',\n"
                                    f"leave blank to cancel)\n")
                # If detected more than 1 character,
                # Restart the process for the current type.
                if len(char_change) > 1:
                    print("Expected only 1 character, Restarting...")
                # If prompt is empty,
                # don't change the settings of the displayed type.
                elif char_change == "":
                    bool_loop_format_change = False
                else:
                    # If Input is applicable,
                    # Then change according to the displayed type.
                    if char == "dot":
                        current_morse_settings["dot"] = char_change
                    if char == "dash":
                        current_morse_settings["dash"] = char_change
                    if char == "slash":
                        current_morse_settings["slash"] = char_change
                    bool_loop_format_change = False
        bool_loop_save_format_change = True
        while bool_loop_save_format_change:
            # Prompt the user to save as a file
            # that can be loaded in future runs.
            input_save = input("Save changes for future use?\n"
                               "(Y)es\n"
                               "(N)o\n")
            match input_save.upper():
                case "Y":
                    # If Yes, Saves the file
                    self.save_format(current_morse_settings)
                    bool_loop_save_format_change = False
                case "N":
                    # If No, then just exit the loop
                    bool_loop_save_format_change = False
            # If the input is not valid for this selection,
            # Then prompt the user to try again and restart the loop
            print("Invalid input, please try again")
        return current_morse_settings