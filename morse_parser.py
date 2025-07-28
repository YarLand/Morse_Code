from morse_dict import MorseDict

morse_dict = MorseDict()

morse_dict.MorseInit()

print(morse_dict.m_dict)

class MorseParser:
    def __init__(self):
        pass

    def decode(self, message):
        decoded = " ".join([morse_dict.m_dict[letter.lower()] for letter in message]).strip()
        print(decoded)