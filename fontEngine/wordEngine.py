from fontEngine import characters
from fontEngine.charTypes import Character

class WordEngine:
    def __init__(self):
        self.characters = characters.characters_as_codes

    def norm_character_to_char_code(self, char):
        if len(char) != 1:
            raise ValueError("Expected a single character")

        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            index = ord(char.lower()) - ord('a')
            return self.characters[index]
        elif char == ' ' or char == " ":
            return self.characters[26]
        # not A–Z / a–z → return standard char code
        return Character(1, 2, False, False, [char], False)

    def convert_characters_to_list(self, word):
        sub_square1 = False
        sub_square2 = False
        sub_square3 = False
        sub_square4 = False

        letters = []
        for char in word:
            char = self.norm_character_to_char_code(char)

            letters.append({
                "char": char,
                "length": char.length
                }
            )

        return letters
