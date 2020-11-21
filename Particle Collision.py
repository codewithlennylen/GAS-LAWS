'''
Test Particle Collision by using Circle attached to mouse, colliding against a static particle
++ Include Boundary to test for boundary Collision
++ Include Movement
'''

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

CLOCK = pygame.time.Clock()
FPS = 30



done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    SCREEN.fill(WHITE)

    obj_x, obj_y = 300,300
    circle1 = pygame.draw.circle(SCREEN, RED, (obj_x, obj_y), 50)
    pos_x, pos_y = mouse_pos[0],mouse_pos[1]
    circle2 = pygame.draw.circle(SCREEN, RED, (pos_x, pos_y), 50)

    if (pos_x + 50 > obj_x - 50 and (pos_y + 50 > obj_y - 50 and pos_y - 50 < obj_y + 50)) and (pos_x - 50 < obj_x + 50 and (pos_y + 50 > obj_y - 50 and pos_y - 50 < obj_y + 50)):
        print('Collide')


    pygame.display.update()
    CLOCK.tick(FPS)
