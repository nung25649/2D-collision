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
        
pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((500, 500))
allball = []
for i in range(0, 30):
    allball.append(Ball(i * 17, i * 10, random.choice([-1,1]),
                  random.choice([-1,1]), random.randrange(10,20)))
while True:
    window.fill(pygame.Color(255,255, 255))
    for ball in allball:
        ball.update()
        
        window.blit(ball.image, ball.rect)
    #window.blit(ball.image, ball.rect)
    #window.blit(ball2.image, ball2.rect)
    pygame.display.update()
    fps.tick(30)
