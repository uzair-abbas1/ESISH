from fontEngine.wordEngine import WordEngine
import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
pygame.display.set_caption("Custom Script Renderer")

font_size = 48

FONT_PATH = "fonts/ESISH_PUA.ttf"
esish_font = pygame.font.Font(FONT_PATH, font_size)
normal_font = pygame.font.Font(None, font_size)

# Example output from your engine (PUA characters)
WE = WordEngine()
word_as_char_dict = []
for charDict in WE.convert_characters_to_list("I am alive"):
    word_as_char_dict.append(charDict)
clock = pygame.time.Clock()
running = True

# space width
space_char = WE.convert_characters_to_list(" ")[0]['char']
space_width = esish_font.render(space_char.glyph_codes[0], True, (240, 240, 240)).get_width()

while running:
    screen.fill((30, 30, 30))

    x = 50
    y = 80

    for i, ch_as_dict in enumerate(word_as_char_dict):
        ch = ch_as_dict["char"]
        if ch.ESISHChar:
            glyph = esish_font.render(ch.glyph_codes[0], True, (240, 240, 240))
        else:
            glyph = normal_font.render(ch.glyph_codes[0], True, (240, 240, 240))
        screen.blit(glyph, (x, y))
        x += space_width * ch_as_dict["length"]

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(
                (event.w, event.h), pygame.RESIZABLE
            )

    clock.tick(60)

pygame.quit()