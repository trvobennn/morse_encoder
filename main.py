"""
Basic Morse code encoder/decoder program. Takes strings as input.
"""

class Morse:
    def __init__(self):
        self.to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                         'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                         'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
                         '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                         '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
        self.from_morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                           '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                           '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                           '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                           '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                           '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                           '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2',
                           '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                           '--...': '7', '---..': '8', '----.': '9', '-----': '0'}

    @property
    def get_morse_list(self):
        return self.to_morse

    def encode_text(self, plain_text):
        enc_string = ''
        for letter in plain_text:
            if letter.isalpha():
                enc_string += self.to_morse[letter.upper()]
            if letter.isdigit():
                enc_string += self.to_morse[letter]
            if letter.isspace():
                enc_string += '/'
            enc_string += ' '
        return enc_string
    def decode_text(self, morse_string):
        dec_string = ''
        m_str_ = morse_string.split('/')
        for item in m_str_:
            item_c = item.split(' ')
            for letter in item_c:
                if len(letter) > 0:
                    dec_string += self.from_morse[letter]
            dec_string += ' '
        return dec_string
