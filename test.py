import pygame
from fontEngine.esishFontEngine import EsishFontEngine
from textRenderer.textRenderer import TextRenderer

pygame.init()

screen = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
pygame.display.set_caption("Custom Script Renderer")

FONT_SIZE = 48
rate = 1/50
ESISH_font = pygame.font.Font("fonts/ESISH_PUA.ttf", FONT_SIZE)
normal_font = pygame.font.Font(None, FONT_SIZE)

WE = EsishFontEngine()
renderer = TextRenderer(screen, ESISH_font, normal_font, WE)

# DRILLS: PRONOUNCE COMPLEX WORDS -> QUICKLY PRONOUNCE SIMPLE SENTENCES
text = """
Here’s the important thing: whatever your reasons for wanting to start 
a marketing services company, it is absolutely necessary that you are honest 
with yourself and your partners. It isn’t necessarily a bad thing if you and your 
partners have different ideas of what they want to get out of the company, 
so long as these are frankly addressed up front. It’s amazing how much two 
people can discuss a plan without getting to the central core of why they’re 
doing it, and if you’re not careful, you’ll end up several years down the road 
before such things are frankly addressed, and by then it may well be too late 
to accommodate both of your needs and desires. 
"""

text1 = ("--"
        "Life-Advice"
        "--"
        "Don't be in a rush to grow up. Live in the present."
        "Time is the greatest currency."
        "Stop waiting to be ready"
        "Never underestimate compound interest - Habit Stack + Daily improvements + Daily Work + Daily Skill training"
        "Follow your dreams, don't listen to what others say"
        "--"
        "Life-Advice from Elders"
        "--"
        "Don't wait to follow your dreams. Do it know"
        "Listen to other people's advice"
        "Pay attention to this advice in life"
        "--"
        "Regrets"
        "--"
        "Not spending enough time with loved ones."
        "Not taking better care of my health."
        "Working too much"
        "Not going on enough trips with family and friends."
        "I wish I had not worked so hard."
        "I wish I never waited for the right moment"
        "Not standing up to bad people in life"
        "Letting friendship fizzle out"
        "One of the most common: Not/Having a relationship with someone. Wrong time, gave up on dream, staying in relationship"
        "One of the most common: Not doing something"
        "--"
        "Regrets from Elders"
        "--"
        "Not doing things in their youth"
        "Spending time with parents"
        "Learning things too late"
        )

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

    clock.tick(rate)

pygame.quit()
