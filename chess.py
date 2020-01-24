import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((480, 480))
screen.fill((50,50,50))
wh=pygame.image.load("bb.png")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    x=60
    y=0
    line=1
    for temp in range(64):
        pygame.draw.rect(screen, (255, 255, 255),(x,y,60,60))
        x+=120
        if x>420:
            line+=1
            y+=60
            if line%2==0:
                x=0
            else:
                x=60

    screen.blit(wh,((60,0)))

    msElapsed = clock.tick(30)
    pygame.display.update()
