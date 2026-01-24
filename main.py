import pygame

pygame.init()

screen = pygame.display.set_mode((800, 200))
pygame.display.set_caption("Custom Script Renderer")

FONT_PATH = "fonts/ESISHTest2.ttf"
font = pygame.font.Font(FONT_PATH, 48)

# Example output from your engine (PUA characters)
text = "\uE100\uE101\uE102"

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((30, 30, 30))

    x = 50
    y = 80

    for i, ch in enumerate(text):
        glyph = font.render(ch, True, (240, 240, 240))

        if i == 2:  # character 3
            # overlap with character 2
            x -= 30  # adjust overlap amount
        screen.blit(glyph, (x, y))

        # normal advance for next character
        x += glyph.get_width()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()