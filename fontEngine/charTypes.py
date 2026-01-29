# Characters, single, doubleHorizontal, doubleVertical, doubleHorizontalAndDiagonal, triple, quad
class Character:
    def __init__(self, length, width, diag, gap):
        self.length = length
        self.width = width
        self.diag = diag
        self.gap = gap

class SingleChar(Character):
    def __init__(self, glyph_code_lower, glyph_code_upper):
        super().__init__(1, 1, False, False)
        self.glyph_code_lower = glyph_code_lower
        self.glyph_code_upper = glyph_code_upper

class DoubleHorizontalChar(Character):
    def __init__(self, glyph_code_lower, glyph_code_upper):
        super().__init__(2, 1, False, False)
        self.glyph_code_lower = glyph_code_lower
        self.glyph_code_upper = glyph_code_upper

class DoubleVerticalChar(Character):
    def __init__(self, glyph_code):
        super().__init__(1, 2, False, False)
        self.glyph_code = glyph_code

class DoubleHorizontalAndDiagonalChar(Character):
    def __init__(self, glyph_code_lower, glyph_code_upper, glyph_code_diag):
        super().__init__(2, 1, False, False)
        self.glyph_code_lower = glyph_code_lower
        self.glyph_code_upper = glyph_code_upper
        self.glyph_code_diag = glyph_code_diag

class TripleChar(Character):
    def __init__(self, glyph_code_top_right, glyph_code_top_left, glyph_code_bottom_right):
        super().__init__(2, 2, False, True)
        self.glyph_code_top_right = glyph_code_top_right
        self.glyph_code_top_left = glyph_code_top_left
        self.glyph_code_bottom_right = glyph_code_bottom_right

class QuadChar(Character):
    def __init__(self, glyph_code):
        super().__init__(2, 2, False, False)
        self.glyph_code = glyph_code
