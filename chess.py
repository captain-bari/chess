import pygame
import rules
from pygame.locals import *

pygame.init()                                               #Start
clock = pygame.time.Clock()                                 #fps initalise
screen = pygame.display.set_mode((480, 480))                #main window
screen.fill((50,50,50))                                     #background black
pygame.display.set_caption('Chess')


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
firsttap="-"
lastmoveby="b"

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            a, b = event.pos
            print(a,b)

            for n in range(8):
                for m in range(8):
                    if (b>n*60 and b<(n+1)*60) and (a>m*60 and a<(m+1)*60):
                        if firsttap is "-":
                            firsttap = pieces[n][m]
                            if(pieces[n][m]=="-"):
                                break
                            if(firsttap[0]==lastmoveby):
                                firsttap = "-"
                                pygame.mixer.music.load('turn.mp3')
                                pygame.mixer.music.play(0)
                                break
                            pieces[n][m] = "-"
                            from_x=n
                            from_y=m
                            pygame.mixer.music.load('f.mp3')
                            pygame.mixer.music.play(0)
                        else:
                    
                            if rules.check(pieces, firsttap, from_x, from_y, n, m):
                                pieces[n][m] = firsttap
                                lastmoveby=firsttap[0]
                                firsttap = "-"
                                pygame.mixer.music.load('s.mp3')
                                pygame.mixer.music.play(0)
                            else:
                                pieces[from_x][from_y] = firsttap
                                firsttap = "-"
                                pygame.mixer.music.load('invalid.mp3')
                                pygame.mixer.music.play(0)

                        print(pieces)
                        break


    x=0
    y=0
    line=1
    screen.fill((50, 50, 50))
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
