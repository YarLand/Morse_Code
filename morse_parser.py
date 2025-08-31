from morse_dict import MorseDict

morse_dict = MorseDict()

class MorseParser:

    def __init__(self):
        self.m_dict = morse_dict.MorseInit("morse_dict.tsv")
        self.dot = "."
        self.dash = "-"

    def invalid_check(func):
        def character_check(self, message):
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
                func(self, message)
        return character_check


    def message_proof(self, func, message):
        return func(message.strip())

    @invalid_check
    def encode(self, message):
        encoded = " ".join([self.m_dict[letter.lower()] for letter in message]).strip()
        encoded = encoded.translate(str.maketrans(".-",f"{self.dot}{self.dash}"))
        print(encoded)

    def decode(self, message):
        flipped_dict = {value: key for key, value in self.m_dict.items()}
        flipped_dict = {key.translate(str.maketrans(".-",f"{self.dot}{self.dash}")): value for key, value in flipped_dict.items()}
        decoded = "".join([flipped_dict[block] for block in message.split(" ")]).strip()
        print(decoded)

    def format_change(self):
        characters = {"dot": ".", "dash": "-"}

        for char, value in characters.items():
            while True:
                char_change = input(f"Please input the new {char} character: \n"
                               f"(Default: '{value}', leave blank to cancel)\n")
                if len(char_change) > 1:
                    print("Expected only 1 character, Restarting...")
                elif char_change == "":
                    break
                else:
                    if char == "dot":
                        self.dot = char_change
                    if char == "dash":
                        self.dash = char_change
                    break



    def debug_show_dict(self):
        print("Dot: ",self.dot,"\nDash: ", self.dash,"\nSupported characters: ", self.m_dict,"\n")