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
        self.velocity_range = [2,3,4]
        self.velocity = random.choice(self.velocity_range)
        self.x_direction = random.choice([True, False])  # True = Positive && False = Negative
        self.y_direction = random.choice([True, False])  # True = Positive && False = Negative
        self.color = RED

        self.gas_particles = particles_list
        self.boundary = boundary
        self.pos_x = random.randrange(
            self.boundary[0] + self.radius, (self.boundary[0] + self.boundary[2]) - self.radius)
        self.pos_y = random.randrange(
            self.boundary[1] + self.radius, (self.boundary[1] + self.boundary[3]) - self.radius)
        self.center = [self.pos_x, self.pos_y]

    def move(self):
        if self.x_direction == True:
            self.center[0] += self.velocity
        elif self.x_direction == False:
            self.center[0] -= self.velocity

        if self.y_direction == True:
            self.center[1] += self.velocity
        elif self.y_direction == False:
            self.center[1] -= self.velocity

    def collide_with_container(self):
        if self.center[0] + self.radius >= self.boundary[2] + self.boundary[0]:
            self.x_direction = False
        elif self.center[0] - self.radius < self.boundary[0]:
            self.x_direction = True

        if self.center[1] + self.radius >= self.boundary[3] + self.boundary[1]:
            self.y_direction = False
        elif self.center[1] - self.radius < self.boundary[1]:
            self.y_direction = True
    
    def collide_with_particle(self):
        for gas_particle in self.gas_particles:
            if self.center[0] + self.radius > gas_particle.center[0] - gas_particle.radius:
                if self.center[1] > gas_particle.center[1] - gas_particle.radius and self.center[1] < gas_particle.center[1] + gas_particle.radius:
                    self.x_direction = False
            elif self.center[0] < gas_particle.center[0]:
                if self.center[1] > gas_particle.center[1] - gas_particle.radius and self.center[1] < gas_particle.center[1] + gas_particle.radius:
                    self.x_direction = True

            if self.center[1] + self.radius > gas_particle.center[1] - gas_particle.radius:
                if self.center[0] > gas_particle.center[0] - gas_particle.radius and self.center[0] < gas_particle.center[0] + gas_particle.radius:
                    self.y_direction = False
            elif self.center[1] < gas_particle.center[1]:
                if self.center[0] > gas_particle.center[0] - gas_particle.radius and self.center[0] < gas_particle.center[0] + gas_particle.radius:
                    self.y_direction = True

        # for gas_particle in self.gas_particles:
        #     if self.center[0] + self.radius >= gas_particle.center[0] - gas_particle.radius:
        #         self.x_direction = False
        #     elif self.center[0] - self.radius <= gas_particle.center[0] + gas_particle.radius:
        #         self.x_direction = True

        #     if self.center[1] + self.radius >= gas_particle.center[1] - gas_particle.radius:
        #         self.y_direction = False
        #     elif self.center[1] - self.radius <= gas_particle.center[1] + gas_particle.radius:
        #         self.y_direction = True

    def collide(self):
        self.collide_with_container()
        # self.collide_with_particle()

    def draw(self):
        pygame.draw.circle(SCREEN, self.color, self.center, self.radius)


# p1 = GasParticle([WIDTH//2 - 300, HEIGHT//2 - 300, 600, 600])
# p2 = GasParticle([WIDTH//2 - 300, HEIGHT//2 - 300, 600, 600])


def generate_particles(n):
    global particles_list

    for _ in range(n):
        p = GasParticle([WIDTH//2 - 300, HEIGHT//2 - 300, 600, 600])
        particles_list.append(p)


generate_particles(2)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    SCREEN.fill(WHITE)

    pygame.draw.rect(SCREEN, BLACK, pygame.Rect(
        WIDTH//2 - 300, HEIGHT//2 - 300, 600, 600), 5)

    for p in particles_list:
        p.draw()
        p.move()
        p.collide()

    # p1.draw()
    # p1.move()
    # p1.collide()

    # p2.draw()
    # p2.move()
    # p2.collide()

    # if keys[pygame.K_SPACE]:
    #     p1.move()

    # pygame.draw.rect(SCREEN, BLACK, pygame.Rect(
    #     10, HEIGHT//2 - 125, 300, 250), 5)
    # pygame.draw.rect(SCREEN, BLACK, pygame.Rect(
    #     330, HEIGHT//2 - 125, 300, 250), 5)
    # pygame.draw.rect(SCREEN, BLACK, pygame.Rect(
    #     650, HEIGHT//2 - 125, 300, 250), 5)

    pygame.display.update()
    CLOCK.tick(FPS)
