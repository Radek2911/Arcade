import pygame
from Minesweeper import thegame
from pygame.locals import *

black=0,0,0
def MineSweeper():
    pygame.init()
    screen=pygame.display.set_mode((600,600))
    back=pygame.image.load('background.PNG')
    back=pygame.transform.scale(back,(600,600))
    def show_text(msg,x,y,color):

        fontobj= pygame.font.SysFont('freesans',50)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))

    while True:
        screen.blit(back,(0,0))
        show_text('EASY',450,100,black)
        show_text('MEDIUM',60,220,black)
        show_text('HARD',200,450,black)
        show_text ('MINESWEEPER',100,350,black)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                print (event.pos)
                if event.pos[0] in range(450,560) and event.pos[1] in range(100,150):
                    thegame(4)
                if event.pos[0] in range(60,223) and event.pos[1] in range(220,270):
                    thegame(6)
                if event.pos[0] in range(200,310) and event.pos[1] in range(450,500):
                    thegame(8)
                                
            if event.type==QUIT:
                pygame.quit()
                return

