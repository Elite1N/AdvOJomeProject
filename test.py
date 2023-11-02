import random
import pygame

class HealthBar:

    def __init__(self, rect, health):
        self.rect = rect
        self.max_health = health
        self.reset()

    def reset(self):
        self.health = self.max_health
        self.damage = 0
        self.elapsed = 0
        self.timer = 150

    @property
    def step_damage(self):
        half = int(self.damage / 2)
        if half == 0:
            half = 1
        return half

    def update(self, elapsed):
        if (self.elapsed + elapsed) < self.timer:
            self.elapsed += elapsed
        else:
            self.elapsed = (self.elapsed + elapsed) % self.timer
            if self.damage > 0:
                step_damage = self.step_damage
                if self.health > 0:
                    self.health -= self.step_damage
                self.damage -= self.step_damage
        if self.health < 0:
            self.health = 0

    @property
    def percent_health(self):
        percent_health = ((self.health - self.damage) / self.max_health)
        if percent_health < 0:
            percent_health = 0
        return percent_health

    def draw(self, image):
        healthrect = pygame.Rect(
            self.rect.topleft,
            (self.rect.width * self.percent_health, self.rect.height))
        pygame.draw.rect(image, (200,10,10), healthrect)
        if self.damage > 0:
            damagerect = pygame.Rect(
                healthrect.topright,
                ((self.damage / self.max_health * self.rect.width), self.rect.height))
            pygame.draw.rect(image, (200,200,10), damagerect)
        pygame.draw.rect(image, (200,200,200), self.rect, 1)


pygame.display.init()

screen = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()

healthbar = HealthBar(screen.get_rect().inflate(-100,-250), 100)
max_damage = int(healthbar.max_health * .25)

running = True
while running:
    elapsed = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif event.key == pygame.K_SPACE:
                if healthbar.percent_health > 0:
                    healthbar.damage += random.randint(1,max_damage)
            elif event.key == pygame.K_r:
                healthbar.reset()
    healthbar.update(elapsed)
    screen.fill((0,0,0))
    healthbar.draw(screen)
    pygame.display.flip()