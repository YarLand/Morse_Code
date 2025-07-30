from morse_dict import MorseDict

morse_dict = MorseDict()

class MorseParser:
    def __init__(self):
        morse_dict.MorseInit()

    def encode(self, message):
        encoded = " ".join([morse_dict.m_dict[letter.lower()] for letter in message]).strip()
        print(encoded)

    def decode(self, message):
        flipped_dict = {value: key for key, value in morse_dict.m_dict.items()}
        decoded = "".join([flipped_dict[block] for block in message.split(" ")]).strip()
        print(decoded)