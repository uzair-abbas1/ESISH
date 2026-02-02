import pygame

class TextRenderer:
    def __init__(self, screen, esish_font, normal_font, word_engine, margin=35, line_spacing=10, outline=True):
        self.screen = screen
        self.esish_font = esish_font
        self.normal_font = normal_font
        self.WE = word_engine
        self.margin = margin
        self.line_spacing = line_spacing
        self.scroll_y = 0
        self.content_height = 0
        self.outline = outline

        space_char = self.WE.convert_characters_to_list(" ")[0]['char']
        self.space_width = self.esish_font.render(space_char, True, (0, 0, 0)).get_width()
        self.line_height = max(
            self.esish_font.get_height(),
            self.normal_font.get_height()
        ) + self.line_spacing

    def handle_scroll(self, event):
        if event.type == pygame.MOUSEWHEEL:
            self.scroll_y += event.y * 40
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.scroll_y -= 40
            if event.key == pygame.K_UP:
                self.scroll_y += 40

    def clamp_scroll(self):
        screen_h = self.screen.get_height()
        max_scroll = 0
        min_scroll = min(0, screen_h - self.content_height - self.margin)

        self.scroll_y = max(min(self.scroll_y, max_scroll), min_scroll)

    def draw(self, text, color=(240, 240, 240)):
        width, height = self.screen.get_size()
        max_x = width - self.margin

        x = self.margin
        y = self.margin + self.scroll_y

        char_dicts = self.WE.convert_characters_to_list(text)

        lines_used = 1

        for ch in char_dicts:
            char_code = ch["char"]
            is_esish = ch["is_esish_char"]

            x += self.space_width * ch["initial_x_change"]

            font = self.esish_font if is_esish else self.normal_font
            glyph = font.render(char_code, True, color)
            glyph_width = glyph.get_width()

            # --- LINE WRAP ---
            if x + glyph_width > max_x:
                x = self.margin
                y += self.line_height
                lines_used += 1

            self.screen.blit(glyph, (x, y))
            x += self.space_width * ch["final_x_change"]

        # --- content height ---
        self.content_height = lines_used * self.line_height + self.margin

        self.clamp_scroll()

        # --- outline/debug view ---
        if self.outline:
            pygame.draw.rect(
                self.screen,
                (100, 100, 100),
                pygame.Rect(
                    self.margin - 10,
                    self.margin - 10,
                    width - self.margin * 2 + 20,
                    height - self.margin * 2 + 20
                ),
                1
            )
