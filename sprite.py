import pygame
import random
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, xdir, ydir, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill(pygame.Color(255, 255, 255))
        pygame.draw.circle(self.image,
                           pygame.Color(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)),
                           (10,10), 10, 0)
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.xdir, self.ydir = xdir, ydir
        self.speed = speed
        self.flag = True
    def update(self):
        self.x = self.x + (self.xdir * self.speed)
        self.y = self.y + (self.ydir * self.speed)
        if ((self.x <= 0) or (self.x >= 500)):
            self.xdir = self.xdir * -1
            self.speed *= 0.80
        if ((self.y <= 0) or (self.y >= 500)) and self.flag:
            self.ydir = self.ydir * -1
            self.speed *= 0.80
        while (self.x <= 0 or self.x >= 500):
            self.x = self.x + (self.xdir * self.speed)
        while (self.y <= 0 or self.y >= 500):
            self.y = self.y + (self.ydir * self.speed)
        self.rect.center = (self.x, self.y)
    def collide(self, other):
        if (abs(self.x - other.x) < 17 and abs(self.y - other.y) < 17):
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
for i in range(0, 10):
    allball.append(Ball((random.randrange(10, 500)), (random.randrange(10, 500)), random.choice([-1,1]),
                  random.choice([-1,1]), random.randrange(10,20)))
    #allball.append(Ball(0,0,-1,-1,10))
while running:
    window.fill(pygame.Color(255,255, 255))
    for i in range(0, len(allball)):
        for j in range(i+1, len(allball)):
            allball[i].collide(allball[j])
        allball[i].update()
        window.blit(allball[i].image, allball[i].rect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            running = False

    pygame.display.update()
    fps.tick(30)
