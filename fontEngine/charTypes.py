# Characters, single, doubleHorizontal, doubleVertical, doubleHorizontalAndDiagonal, triple, quad

class Character:
    def __init__(self, length, height, diag, gap, glyph_codes, ESISHChar):
        self.length = length
        self.height = height
        self.diag = diag
        self.gap = gap
        self.glyph_codes = glyph_codes
        self.ESISHChar = ESISHChar

class SingleChar(Character):
    def __init__(self, glyph_code_lower, glyph_code_upper):
        super().__init__(1, 1, False, False, [glyph_code_lower, glyph_code_upper], True)

class DoubleHorizontalChar(Character):
    def __init__(self, glyph_code_lower, glyph_code_upper):
        super().__init__(2, 1, False, False, [glyph_code_lower, glyph_code_upper], True)

class DoubleVerticalChar(Character):
    def __init__(self, glyph_code):
        super().__init__(1, 2, False, False, [glyph_code], True)

class DoubleHorizontalAndDiagonalChar(Character):
    def __init__(self, glyph_code_lower, glyph_code_upper, glyph_code_diag):
        super().__init__(2, 1, False, False, [glyph_code_lower, glyph_code_upper, glyph_code_diag], True)

class TripleChar(Character):
    def __init__(self, glyph_code_top_left, glyph_code_bottom_left):
        super().__init__(2, 2, False, True, [glyph_code_top_left, glyph_code_bottom_left], True)

class QuadChar(Character):
    def __init__(self, glyph_code):
        super().__init__(2, 2, False, False, [glyph_code], True)
