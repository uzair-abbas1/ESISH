import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("ESISH PUA")
font_size = 32

ESISH_font = pygame.font.Font("fonts/ESISHTest2.ttf", font_size)
normal_font = pygame.font.Font(None, font_size)

custom_text = "\uE100\uE101\uE102"
custom_surface = ESISH_font.render(custom_text, True, (240, 240, 240))

text = "Hello World!"
text_surface = ESISH_font.render(text, True, (240, 240, 240))

clock = pygame.time.Clock()
running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((30, 30, 30))
#
#     screen.blit(custom_surface, (50, 0))
#     screen.blit(text_surface, (50, font_size))
#
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    x = 50
    y = 50

    for i, ch in enumerate(custom_text):
        glyph = ESISH_font.render(ch, True, (240, 240, 240))
        screen.blit(glyph, (x, y))

        # advance logic
        if i == 0:
            # first character: normal spacing
            x += glyph.get_width()
        else:
            # last two characters: overlap immediately
            x += glyph.get_width() * 0.2   # adjust overlap amount here

    pygame.display.flip()
    clock.tick(60)

pygame.quit()