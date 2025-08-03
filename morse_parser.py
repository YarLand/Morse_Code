from morse_dict import MorseDict

morse_dict = MorseDict()

class MorseParser:

    def __init__(self):
        morse_dict.MorseInit()

    def message_proof(self, func, message):
        for character in message:
            if character not in morse_dict.m_dict:
                print(f"Message contains invalid character: {character}.\n"
                      f"Please remove the characters from the message")
                return None
        return func(message)

    def encode(self, message):
        encoded = " ".join([morse_dict.m_dict[letter.lower()] for letter in message]).strip()
        print(encoded)

    def decode(self, message):
        flipped_dict = {value: key for key, value in morse_dict.m_dict.items()}
        decoded = "".join([flipped_dict[block] for block in message.split(" ")]).strip()
        print(decoded)

    def debug_show_dict(self):
        print(morse_dict.m_dict)