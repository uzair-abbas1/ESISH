import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Custom Script Renderer")

FONT_PATH = "fonts/ESISH_PUA.ttf"
font = pygame.font.Font(FONT_PATH, 48)

# Example output from your engine (PUA characters)
text1= ''.join(chr(c) for c in range(0xE100, 0xE118))
text2= ''.join(chr(c) for c in range(0xE118, 0xE134))

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((30, 30, 30))

    x = 50
    y = 80

    for i, ch in enumerate(text1):
        glyph = font.render(ch, True, (240, 240, 240))

        screen.blit(glyph, (x, y))

        # normal advance for next character
        x += glyph.get_width()

    y += 80
    x = 50
    for i, ch in enumerate(text2):
        glyph = font.render(ch, True, (240, 240, 240))

        screen.blit(glyph, (x, y))

        # normal advance for next character
        x += glyph.get_width()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()