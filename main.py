import pygame
import random

pygame.init()

WIDTH, HEIGHT = 960, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

CLOCK = pygame.time.Clock()
FPS = 30

particles_list = []


class GasParticle():
    def __init__(self, boundary):
        self.radius = 10
        self.pos_x = random.randrange(
            boundary[0] + self.radius, (boundary[0] + boundary[2]) - self.radius)
        self.pos_y = random.randrange(
            boundary[1] + self.radius, (boundary[1] + boundary[3]) - self.radius)
        self.velocity = 2
        self.color = RED
        self.center = [self.pos_x, self.pos_y]

    def move(self):
        pass

    def collide(self):
        pass

    def draw(self):
        pygame.draw.circle(SCREEN, self.color, self.center, self.radius)


# p1 = GasParticle([WIDTH//2 - 300, HEIGHT//2 - 300, 600, 600])
# p2 = GasParticle([WIDTH//2 - 300, HEIGHT//2 - 300, 600, 600])


def generate_particles(n):
    global particles_list

    for i in range(n):
        p = GasParticle([WIDTH//2 - 300, HEIGHT//2 - 300, 600, 600])
        particles_list.append(p)


generate_particles(10)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    SCREEN.fill(WHITE)

    pygame.draw.rect(SCREEN, BLACK, pygame.Rect(
        WIDTH//2 - 300, HEIGHT//2 - 300, 600, 600), 5)

    for p in particles_list:
        p.draw()

    # p1.draw()
    # p2.draw()

    # pygame.draw.rect(SCREEN, BLACK, pygame.Rect(
    #     10, HEIGHT//2 - 125, 300, 250), 5)
    # pygame.draw.rect(SCREEN, BLACK, pygame.Rect(
    #     330, HEIGHT//2 - 125, 300, 250), 5)
    # pygame.draw.rect(SCREEN, BLACK, pygame.Rect(
    #     650, HEIGHT//2 - 125, 300, 250), 5)

    pygame.display.update()
    CLOCK.tick(FPS)
