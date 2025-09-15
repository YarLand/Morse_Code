from morse_dict import MorseDict

morse_dict = MorseDict()

class MorseParser:

    def __init__(self):
        self.m_dict = morse_dict.MorseInit("morse_dict.tsv")
        self.dot = "."
        self.dash = "-"

    def invalid_check(func):
        def character_check(self, message, settings):
            # print(args)
            # message = args[0]
            invalid_chars = []
            for character in message:
                if character not in self.m_dict:
                    invalid_chars.append(character)
            if len(invalid_chars) > 0:
                print(f"Message contains invalid character/s: {list(set(invalid_chars))}.\n"
                      f"Please remove the characters from the message")
            else:
                func(self, message,settings)
        return character_check


    def message_proof(self, func, message, morse_settings):
        return func(message.strip(), morse_settings)

    @invalid_check
    def encode(self, message,morse_settings):
        encoded = " ".join([self.m_dict[letter.lower()] for letter in message]).strip()
        encoded = encoded.translate(str.maketrans(".-",f"{morse_settings["dot"]}{morse_settings["dash"]}"))
        print(f"Encoded message: {encoded}")

    def decode(self, message, morse_settings):
        flipped_dict = {value: key for key, value in self.m_dict.items()}
        flipped_dict = {key.translate(str.maketrans(".-",f"{morse_settings["dot"]}{morse_settings["dash"]}")): value for key, value in flipped_dict.items()}
        decoded = "".join([flipped_dict[block] for block in message.split(" ")]).strip()
        print(f"Decoded message: {decoded}")



    def debug_show_dict(self):
        print("Dot: ",self.dot,"\nDash: ", self.dash,"\nSupported characters: ", self.m_dict,"\n")