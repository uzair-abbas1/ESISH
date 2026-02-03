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

text = "On my first day learning a new language, I sat quietly in a small cafe, listening to the sounds of unfamiliar words around me, and even though I felt nervous and unsure, I decided to start practicing by imagining a simple conversation, where I politely greet a stranger, explain that I am still learning, and slowly ask for their name, hoping that each small sentence will help me feel more confident and comfortable with the language."

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
