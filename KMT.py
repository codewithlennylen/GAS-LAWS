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


class Container(object):
    def __init__(self):
        self.color = BLACK
        self.width = 600
        self.height = 600
        self.pos_x = ((WIDTH // 2) - (self.width // 2))
        self.pos_y = ((HEIGHT // 2) - (self.height // 2))

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, pygame.Rect(
            self.pos_x, self.pos_y, self.width, self.height), 5)


class GasParticle():
    def __init__(self, boundary):
        """Initialize the Object/Instance

        Args:
            boundary (List): This is the boundary that defines the container.
                            (Within which the particles are held and collide against)
                            Pos_X, Pos_Y, Width, Height
        """
        self.radius = 10  # Particle Radius
        self.velocity_range = [2, 3, 4]
        self.velocity = random.choice(self.velocity_range)
        # True = Positive && False = Negative
        self.x_direction = random.choice([True, False])
        # True = Positive && False = Negative
        self.y_direction = random.choice([True, False])
        self.color = RED

        # List of defined Particles for particle-collision
        self.gas_particles = particles_list
        self.boundary = boundary
        self.pos_x = random.randrange(
            self.boundary[0] + self.radius, (self.boundary[0] + self.boundary[2]) - self.radius)
        self.pos_y = random.randrange(
            self.boundary[1] + self.radius, (self.boundary[1] + self.boundary[3]) - self.radius)
        self.center = [self.pos_x, self.pos_y]

    def move(self):
        """Movement of the Particle. Rudimentary-Not as random as it should be
        We are simply changing direction to a predefined direction- PHYSICS-ELEMENT IS MISSING (VECTORS)
        """
        if self.x_direction == True:
            self.center[0] += self.velocity
        elif self.x_direction == False:
            self.center[0] -= self.velocity

        if self.y_direction == True:
            self.center[1] += self.velocity
        elif self.y_direction == False:
            self.center[1] -= self.velocity

    def collide_with_container(self):
        """With the boundaries of the bounding box defined. We can easily create/simulate collisions with the container
        """
        if self.center[0] + self.radius >= self.boundary[2] + self.boundary[0]:
            self.x_direction = False
        elif self.center[0] - self.radius < self.boundary[0]:
            self.x_direction = True

        if self.center[1] + self.radius >= self.boundary[3] + self.boundary[1]:
            self.y_direction = False
        elif self.center[1] - self.radius < self.boundary[1]:
            self.y_direction = True

    def collide_with_particle(self):
        """This handles the collision of this.particle with other particles. 
        BUG : Still not working. All particles assemble to one corner upon collision.
        """
        for gas_particle in self.gas_particles:
            if self.center[0] + self.radius > gas_particle.center[0] - gas_particle.radius:
                if self.center[1] > gas_particle.center[1] - gas_particle.radius and self.center[1] < gas_particle.center[1] + gas_particle.radius:
                    self.x_direction = False
            elif self.center[0] - self.radius < gas_particle.center[0] + gas_particle.radius:
                if self.center[1] > gas_particle.center[1] - gas_particle.radius and self.center[1] < gas_particle.center[1] + gas_particle.radius:
                    self.x_direction = True

            if self.center[1] + self.radius > gas_particle.center[1] - gas_particle.radius:
                if self.center[0] > gas_particle.center[0] - gas_particle.radius and self.center[0] < gas_particle.center[0] + gas_particle.radius:
                    self.y_direction = False
            elif self.center[1] - self.radius < gas_particle.center[1] + gas_particle.radius:
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
        # self.collide_with_particle()
        self.collide_with_container()

    def draw(self):
        """Draw/render the object onto the pygame.Surface(SCREEN)
        """
        pygame.draw.circle(SCREEN, self.color, self.center, self.radius)


def generate_particles(container, n):
    global particles_list

    for _ in range(n):
        p = GasParticle([container.pos_x, container.pos_y,
                         container.width, container.height])
        particles_list.append(p)


container = Container()
generate_particles(container, 10)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    SCREEN.fill(WHITE)

    container.draw()

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
