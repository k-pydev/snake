import sys

import pygame

pygame.init()

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
pygame.display.set_caption("Game Name")

clock = pygame.time.Clock()
FPS = 60

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
