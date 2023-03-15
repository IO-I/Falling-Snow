import pygame
import random

background_colour = (0,0,0)
(width, height) = (900, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snowfall')
screen.fill(background_colour)
pygame.display.flip()
running = True
radius = 2
flakes = []
amount = 500

class Flake:
    def __init__(self, x, y, speed, direction, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.radius = radius

    def fall(self):
        if self.speed < 3:
            self.y+=self.speed/30
        else:
             self.y+=self.speed/40
        self.radius = self.speed/1.5
        if self.x > width:
             self.x = 0
        if self.x < 0:
             self.x = width

    def reset(self):
        if self.y > height:
            self.y = random.randint(-800, -10)
            self.direction = random.randint(-10, 10)

    def wind(self):
        user = pygame.mouse.get_pos()[0] - width/2
        self.x +=self.direction/300 + user*0.0004*(self.radius*0.5)
        
for i in range(amount):
        user = pygame.mouse.get_pos()[0] - width/2
        flakes.append(Flake(random.randint(0, width), random.randint(-800,-10), random.randint(1, 6), random.randint(-10, 10), random.randint(1,20)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for flake in flakes:
         flake.fall()
         flake.reset()
         flake.wind()
    
    screen.fill(background_colour)
    for flake in flakes:
        pygame.draw.circle(screen,(255, 255, 255),(flake.x,flake.y),flake.radius)
    pygame.display.update()
