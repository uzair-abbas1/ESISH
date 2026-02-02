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
for charDict in WE.convert_characters_to_list("fxffxcd"):
    word_as_char_dict.append(charDict)
clock = pygame.time.Clock()
running = True

# space width
# space_char = WE.convert_characters_to_list(" ")[0]['char']
# space_width = esish_font.render(space_char, True, (240, 240, 240)).get_width()
space_width = 24
while running:
    screen.fill((30, 30, 30))

    x = 50
    y = 80

    for i, ch_as_dict in enumerate(word_as_char_dict):
        char_code = ch_as_dict["char"]
        is_esish = ch_as_dict["is_esish_char"]
        initial_x_change = ch_as_dict["initial_x_change"]
        final_x_change = ch_as_dict["final_x_change"]
        x += space_width * ch_as_dict["initial_x_change"]
        # x += 24 * initial_x_change

        if is_esish:
            glyph = esish_font.render(char_code, True, (240, 240, 240))
        else:
            glyph = normal_font.render(char_code, True, (240, 240, 240))
        screen.blit(glyph, (x, y))

        # x += 24 * final_x_change
        x += space_width * final_x_change

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