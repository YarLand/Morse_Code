from morse_dict import MorseDict

morse_dict = MorseDict()

class MorseParser:

    def __init__(self):
        morse_dict.MorseInit()

    def invalid_check(func):
        def character_check(*args):
            message = args[-1]
            invalid_chars = []
            for character in message:
                if character not in morse_dict.m_dict:
                    invalid_chars.append(character)
            if len(invalid_chars) > 0:
                print(f"Message contains invalid character/s: {list(set(invalid_chars))}.\n"
                      f"Please remove the characters from the message")
            else:
                func(*args)
        return character_check


    def message_proof(self, func, message):
        return func(message.strip())

    @invalid_check
    def encode(self, message):
        encoded = " ".join([morse_dict.m_dict[letter.lower()] for letter in message]).strip()
        print(encoded)

    def decode(self, message):
        flipped_dict = {value: key for key, value in morse_dict.m_dict.items()}
        decoded = "".join([flipped_dict[block] for block in message.split(" ")]).strip()
        print(decoded)

    def debug_show_dict(self):
        print(morse_dict.m_dict)