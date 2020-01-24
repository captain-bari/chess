import pygame
from pygame.locals import *

pygame.init()                                               #Start
clock = pygame.time.Clock()                                 #fps initalise
screen = pygame.display.set_mode((480, 480))                #main window
screen.fill((50,50,50))                                     #background black


#storing images------------------------------------------------------------------------------------------------
bb=pygame.image.load("bb.png")
wb=pygame.image.load("wb.png")
bh=pygame.image.load("bh.png")
wh=pygame.image.load("wh.png")
wq=pygame.image.load("wq.png")
wk=pygame.image.load("wk.png")
bq=pygame.image.load("bq.png")
bk=pygame.image.load("bk.png")
wp=pygame.image.load("wp.png")
bp=pygame.image.load("bp.png")
wr=pygame.image.load("wr.png")
br=pygame.image.load("br.png")

pieces = [["br", "bh", "bb", "bq", "bk", "bb", "bh", "br"], ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"], ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-", "-"], ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"], ["wr", "wh", "wb", "wq", "wk", "wb", "wh", "wr"]]
#--------------------------------------------------------------------------------------------------------------------
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    x=0
    y=0
    line=1
    for temp in range(64): #BOARD
        pygame.draw.rect(screen, (255, 255, 255),(x,y,60,60))
        x+=120
        if x>420:
            line+=1
            y+=60
            if line%2==0:
                x=60
            else:
                x=0

    for i in range(8):
        for j in range(8):
            temp=pieces[i][j]

            if temp is "-":
                pass
            else:
                if temp is "wr":
                    screen.blit(wr,((j*60,i*60)))
                if temp is "br":
                    screen.blit(br, ((j * 60, i * 60)))
                if temp is "wp":
                    screen.blit(wp, ((j * 60, i * 60)))
                if temp is "bp":
                    screen.blit(bp, ((j * 60, i * 60)))
                if temp is "wb":
                    screen.blit(wb, ((j * 60, i * 60)))
                if temp is "bb":
                    screen.blit(bb, ((j * 60, i * 60)))
                if temp is "wk":
                    screen.blit(wk, ((j * 60, i * 60)))
                if temp is "bk":
                    screen.blit(bk, ((j * 60, i * 60)))
                if temp is "wq":
                    screen.blit(wq, ((j * 60, i * 60)))
                if temp is "bq":
                    screen.blit(bq, ((j * 60, i * 60)))
                if temp is "wh":
                    screen.blit(wh, ((j * 60, i * 60)))
                if temp is "bh":
                    screen.blit(bh, ((j * 60, i * 60)))

    msElapsed = clock.tick(30)
    pygame.display.update()
