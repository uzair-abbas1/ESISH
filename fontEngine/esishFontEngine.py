from fontEngine import characters
from fontEngine.charTypes import Character

# coordinate: top left, start from 0
# number: start from 0, count to 3

class EsishFontEngine:
    def __init__(self):
        self.characters_codes = characters.characters_as_codes
        self.squares = [True, True, True, True]

    def find_esish_character_class(self, char):
        if len(char) != 1:
            raise ValueError("Expected a single character")

        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            index = ord(char.lower()) - ord('a')
            return self.characters_codes[index]
        elif char == ' ' or char == " ":
            return self.characters_codes[26]
        # not A–Z / a–z → return standard char code
        return Character(1, 2, False, False, [char], False)

    def is_top_row_empty(self):
        return self.squares[0] and self.squares[1]

    def is_bottom_row_empty(self):
        return self.squares[2] and self.squares[3]

    def is_left_column_empty(self):
        return self.squares[0] and self.squares[2]

    def is_right_column_empty(self):
        return self.squares[1] and self.squares[3]

    def find_coordinate_and_num_of_first_empty_square(self):
        if self.squares[0] and self.squares[1] and self.squares[3]:
            return [0, 1, 0]
        if self.squares[1] and self.squares[3]:
            return [1, 1, 1]
        if self.squares[2] and self.squares[3]:
            return [0, 0, 2]
        if self.squares[3]:
            return [1, 0, 3]
        return [None, None, 5]

    def reset_squares(self):
        self.squares = [True, True, True, True]

    def set_squares_to_false_based_num(self, list_):
        for item in list_:
            if 0 <= item <= 3:
                self.squares[item] = False

    def convert_characters_to_list(self, sentence):
        letters = []

        for letter in sentence:
            character_class = self.find_esish_character_class(letter)
            char = None
            initial_x_change = 0
            final_x_change = 0
            length = character_class.length
            height = character_class.height

            if length == 1:
                if height == 1:
                    # single char

                    [x, y, pos] = self.find_coordinate_and_num_of_first_empty_square()
                    if pos != 5:
                        char = character_class.glyph_codes[0 if y == 0 else 1]
                        initial_x_change = x
                        final_x_change = 1 if x == 1 and y == 0 else -x

                        # mark correct squares - order matters of reset
                        self.set_squares_to_false_based_num([pos])
                        if x == 1 and y == 0:
                            self.reset_squares()
                    else:
                        # no available single square
                        char = character_class.glyph_codes[1]
                        initial_x_change = 2
                        self.reset_squares()
                        self.set_squares_to_false_based_num([0])

                else:
                    # vertical char

                    # always the same, order matters
                    if not self.is_left_column_empty():
                        if self.is_right_column_empty():
                            initial_x_change = 1
                        else:
                            initial_x_change = 2

                    char = character_class.glyph_codes[0]
                    final_x_change = 1
                    self.reset_squares()

            else:
                # length is equal 2
                if height == 1:
                    if self.is_top_row_empty():
                        char = character_class.glyph_codes[1]
                        self.set_squares_to_false_based_num([0, 1])
                    elif self.is_bottom_row_empty():
                        char = character_class.glyph_codes[0]
                        if self.squares[1]:
                            self.set_squares_to_false_based_num([2, 3])
                        else:
                            final_x_change = 2
                            self.reset_squares()
                    elif self.squares[1]:
                        initial_x_change = 1
                        final_x_change = 1
                        char = character_class.glyph_codes[1]
                        self.reset_squares()
                        self.set_squares_to_false_based_num([0])
                    elif self.squares[3]:
                        initial_x_change = 1
                        final_x_change = 1
                        char = character_class.glyph_codes[0]
                        self.reset_squares()
                        self.set_squares_to_false_based_num([2])
                    # else:
                    #     initial_x_change = 2
                    #     self.reset_squares()
                    #     char = character_class.glyph_codes[0]
                    #     self.set_squares_to_false_based_num([0, 1])
                else:
                    # square: 2*2

                    if not character_class.gap:
                        # full square
                        # always the same, order matters
                        if not self.is_left_column_empty():
                            if self.is_right_column_empty():
                                initial_x_change = 1
                            else:
                                initial_x_change = 2

                        char = character_class.glyph_codes[0]
                        final_x_change = 2
                        self.reset_squares()
                    else:
                        # broken square, with gap - triple char
                        if self.is_bottom_row_empty() and self.squares[1]:
                            char = character_class.glyph_codes[0]
                        elif self.is_top_row_empty() and self.squares[3]:
                            char = character_class.glyph_codes[1]
                        elif self.squares[3]:
                            char = character_class.glyph_codes[0]
                            initial_x_change = 1
                        elif self.squares[1]:
                            char = character_class.glyph_codes[1]
                            initial_x_change = 1

                        # currently, we always reset squares
                        final_x_change = 2
                        self.reset_squares()

            letters.append({
                "char": char,
                "initial_x_change": initial_x_change,
                "final_x_change": final_x_change,
                "is_esish_char": character_class.ESISHChar,
                }
            )
        # Assume
        self.reset_squares()

        return letters
