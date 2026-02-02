import pygame
from fontEngine.esishFontEngine import EsishFontEngine
from textRenderer.textRenderer import TextRenderer

pygame.init()

screen = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
pygame.display.set_caption("Custom Script Renderer")

FONT_SIZE = 48
ESISH_font = pygame.font.Font("fonts/ESISH_PUA.ttf", FONT_SIZE)
normal_font = pygame.font.Font(None, FONT_SIZE)

WE = EsishFontEngine()
renderer = TextRenderer(screen, ESISH_font, normal_font, WE)

text = "What is your name"

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((30, 30, 30))

    renderer.draw(text)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        renderer.handle_scroll(event)

    clock.tick(60)

pygame.quit()
