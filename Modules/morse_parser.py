from Modules.morse_dict import MorseDict


morse_dict = MorseDict()

class MorseParser:

    # Prompts the user to input the message,
    # and returns as a string
    def define_message(self,settings):
        print(f"Current Morse format: {settings}")
        message_text = input("Please enter the message:\n")
        return message_text

    # If the input is not valid for this selection,
    # Then prompt the user to try again and restart the loop
    def __init__(self):
        self.m_dict = morse_dict.MorseInit("Data/morse_dict.tsv")
        self.dot = "."
        self.dash = "-"


    # Check the function's arguments for invalid input
    # This is used as a decorator in other functions within this module.
    def invalid_check(func):
        def character_check(self, settings):
            # Prompt the user to input a message
            message = self.define_message(settings)
            # Store invalid characters / morse codes
            invalids = []
            # Match the detected function by name
            match func.__name__:
                # If Encode, then check per character if it appears
                # in the "Character" column in "morse_dict.tsv"
                case "encode":
                    for character in message:
                        # If the character does not appear,
                        # then store the incorrect character in the invalids list
                        if character not in self.m_dict:
                            invalids.append(character)
                    # If the "invalids" list has an entry
                    if len(invalids) > 0:
                        # Then display the error
                        # and cancel running the scheduled function
                        print(f"Message contains invalid character/s: {list(set(invalids))}.\n"
                              f"Please remove these characters from the message")
                    else:
                        # If no error detected,
                        # run the scheduled function
                        func(self, message,settings)

                # If Decode, then check per block of morse code
                # if it exists the "MorseCode" column in "morse_dict.tsv"
                case "decode":
                    # Swap columns of the characters and morse codes
                    # to compare blocks to morse code from the dictionary file
                    flipped_dict = {value: key for key, value in self.m_dict.items()}
                    # Apply the current character format
                    flipped_dict = {
                        key.translate(
                            str.maketrans(".-/",
                                          f"{settings["dot"]}"
                                          f"{settings["dash"]}"
                                          f"{settings["space"]}")):
                                          value for key, value in flipped_dict.items()}
                    # For each block of morse code
                    for block in message.split(" "):
                        # If the block does not appear,
                        # then store the incorrect block in the invalids list
                        if block not in flipped_dict:
                            invalids.append(block)
                    # If the "invalids" list has an entry
                    if len(invalids) > 0:
                        # Then display the error
                        # and cancel running the scheduled function
                        print(f"Message contains invalid morse codes: {list(set(invalids))}.\n"
                              f"Please remove these morse codes from the message")
                    else:
                        # If no error detected,
                        # run the scheduled function
                        func(self, message,settings)

        return character_check


    # Decorator: Checks for invalid input
    @invalid_check
    # Turns a message into morse code
    def encode(self,message, current_morse_settings):
        # Converts each letter (lower cased)
        # to its morse equivalent, and cleans extra spaces
        encoded = " ".join([self.m_dict[letter.lower()]
                            for letter in message]).strip()
        # Apply the current character format
        encoded = encoded.translate(
                          str.maketrans(".-/",
                          f"{current_morse_settings["dot"]}"
                          f"{current_morse_settings["dash"]}"
                          f"{current_morse_settings["space"]}"))
        # Displays the encoded message
        print(f"Encoded message: {encoded}")

    @invalid_check
    # Turns morse code into english
    def decode(self, message, current_morse_settings):
        # Swap columns of the characters and morse codes
        flipped_dict = {value: key for key, value in self.m_dict.items()}
        # Apply the current character format
        flipped_dict = {key.translate(
                            str.maketrans(".-/",
                                          f"{current_morse_settings["dot"]}"
                                          f"{current_morse_settings["dash"]}"
                                          f"{current_morse_settings["space"]}")):
                                          value for key, value in flipped_dict.items()}
        # Converts each block of morse code from the input
        # to english, and cleans extra spaces
        decoded = "".join([flipped_dict[block] for
                           block in message.split(" ")]).strip()
        # Displays the decoded message
        print(f"Decoded message: {decoded}")


    # Displays the available characters
    # and morse codes of the program
    def show_dict(self,current_morse_settings):
        # Displays the current formats
        print("Dot: ",current_morse_settings["dot"],"\n"
              "Dash: ", current_morse_settings["dash"],"\n"
              "Space: ", current_morse_settings["space"],"\n"
              "Supported characters:")

        # Converts each morse code to the current format,
        # and display each morse code and translation per line.
        for key, value in self.m_dict.items():
            translated_value = value.translate(str.maketrans(".-/",
                                               f"{current_morse_settings["dot"]}"
                                               f"{current_morse_settings["dash"]}"
                                               f"{current_morse_settings["space"]}"))
            print(f"'{key}': '{translated_value}'")