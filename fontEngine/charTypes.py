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
        self.glyph_code_lower = glyph_code_lower
        self.glyph_code_upper = glyph_code_upper

class DoubleHorizontalChar(Character):
    def __init__(self, glyph_code_lower, glyph_code_upper):
        super().__init__(2, 1, False, False, [glyph_code_lower, glyph_code_upper], True)
        self.glyph_code_lower = glyph_code_lower
        self.glyph_code_upper = glyph_code_upper

class DoubleVerticalChar(Character):
    def __init__(self, glyph_code):
        super().__init__(1, 2, False, False, [glyph_code], True)
        self.glyph_code = glyph_code

class DoubleHorizontalAndDiagonalChar(Character):
    def __init__(self, glyph_code_lower, glyph_code_upper, glyph_code_diag):
        super().__init__(2, 1, False, False, [glyph_code_lower, glyph_code_upper, glyph_code_diag], True)
        self.glyph_code_lower = glyph_code_lower
        self.glyph_code_upper = glyph_code_upper
        self.glyph_code_diag = glyph_code_diag

class TripleChar(Character):
    def __init__(self, glyph_code_top_right, glyph_code_top_left, glyph_code_bottom_right):
        super().__init__(2, 2, False, True, [glyph_code_top_right, glyph_code_top_left, glyph_code_bottom_right], True)
        self.glyph_code_top_right = glyph_code_top_right
        self.glyph_code_top_left = glyph_code_top_left
        self.glyph_code_bottom_right = glyph_code_bottom_right

class QuadChar(Character):
    def __init__(self, glyph_code):
        super().__init__(2, 2, False, False, [glyph_code], True)
        self.glyph_code = glyph_code
