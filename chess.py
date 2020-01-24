import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 640))
wh=pygame.image.load("wh.png")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    x=81
    y=0
    line=1
    for temp in range(64):
        pygame.draw.rect(screen, (255, 255, 255),(x,y,80,80))
        x+=160
        if x>560:
            line+=1
            y+=80
            if line%2==0:
                x=0
            else:
                x=80

    screen.blit(wh,((0,0)))

    msElapsed = clock.tick(30)
    pygame.display.update()
