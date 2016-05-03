import pygame
import random
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, xdir, ydir, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill(pygame.Color(255, 255, 255))
        pygame.draw.circle(self.image,
                           pygame.Color(255,0,0),
                           (10,10), 10, 0)
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.xdir, self.ydir = xdir, ydir
        self.speed = speed
    def update(self):
        self.x = self.x + (self.xdir * self.speed)
        self.y = self.y + (self.ydir * self.speed)
        if (self.x < 10) | (self.x > 490):
            self.xdir = self.xdir * -1
            self.speed *= 0.95
        if (self.y < 10) | (self.y > 490):
            self.ydir = self.ydir * -1
            self.speed *= 0.95
        self.rect.center = (self.x, self.y)
    def collide(self, other):
        if (abs(self.x - other.x) < 20 and abs(self.y - other.y) < 20):
            self.speed, other.speed = other.speed, self.speed
            if (self.xdir != other.xdir):
                self.xdir *= -1
                other.xdir *= -1
            if (self.ydir != other.ydir):
                self.ydir *= -1
                other.ydir *= -1
        
pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((500, 500))
running = True
allball = []
for i in range(0, 3):
    allball.append(Ball(i * 17, i * 10, random.choice([-1,1]),
                  random.choice([-1,1]), random.randrange(10,20)))

while running:
    window.fill(pygame.Color(255,255, 255))
    for i in range(0, len(allball)):
        allball[i].update()
        for j in range(i, len(allball)):
            allball[i].collide(allball[j])
        window.blit(allball[i].image, allball[i].rect)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            running = False
    pygame.display.update()
    fps.tick(30)
