import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Matrix Rain - Ruby Poddar')

FONT_SIZE = 20
FONT = pygame.font.SysFont('consolas', FONT_SIZE)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0, 10)  

CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
columns = WIDTH // FONT_SIZE
drops = [0] * columns
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.size
            SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            columns = WIDTH // FONT_SIZE
            drops = [0] * columns
    fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    fade_surface.fill(BLACK)
    SCREEN.blit(fade_surface, (0, 0))

    for i in range(columns):
        text = random.choice(CHARS)
        x = i * FONT_SIZE
        y = drops[i] * FONT_SIZE

        char_surface = FONT.render(text, True, GREEN)
        SCREEN.blit(char_surface, (x, y))

        drops[i] += 1

        if drops[i] * FONT_SIZE > HEIGHT and random.random() > 0.95:
            drops[i] = 0

    pygame.display.flip()
    clock.tick(60)
