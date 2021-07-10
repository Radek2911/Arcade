##support@youngwonks.com
## SEnd one line email with name project and teacher name
## June 20th, 6:00 pm Warsaw Time, Saturday
import pygame

import time
import random
from pygame.locals import *
def Ninja_Platformer():
    clock=pygame.time.Clock()

    pygame.init()

    black=0,0,0
    blue=0,0,255
    jump=[]
    jumpcount=0
    j=0
    black=0,0,0
    idlecount=0
    idle=[]
    w=0
    runcount=0
    run=[]
    direction=0
    x=0
    y=0
    endx=0
    endy=0
    switching=0
    spikelist=[]
    fall=1
    levelcount=0
    level_list=[]
    for loop in range(0,10,1):
        NI=pygame.image.load('png/Idle__00'+str (loop)+'.png')
        NI=pygame.transform.rotozoom(NI,0,0.1)

        idle.append(NI)
    for loop in range(0,10,1):
        NR=pygame.image.load('png/Run__00'+str (loop)+'.png')
        NR=pygame.transform.rotozoom(NR,0,0.1)

        run.append(NR)
    for loop in range(0,10,1):
        NJ=pygame.image.load('png/Jump__00'+str (loop)+'.png')
        NJ=pygame.transform.rotozoom(NJ,0,0.1)

        jump.append(NJ)
    ## Floor: 1, Acid: 2 Spiketraps: 3, Saw: 4, Switch: 5, Door: '*', Spawn:'P'
    level0=[[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,'*'],
            [0,0,0,0,0,1,3,1,3,1],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,1,3,3],
            [0,0,0,0,1,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0],
            ['p',0,0,1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0],
            [2,2,2,2,2,2,2,2,2,2]]
    level_list.append(level0)
    level1=[[0,0,3,0,0,0,0,0,0,0],
            ['p',0,3,0,0,0,0,0,0,'*'],
            [1,0,3,0,0,0,0,1,3,1],
            [0,0,3,0,1,0,0,0,0,0],
            [0,3,3,0,0,1,0,0,0,0],
            [0,0,3,0,0,0,0,1,3,3],
            [3,0,3,0,1,0,0,0,0,0],
            [0,0,3,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,1,0,0,0],
            [1,1,1,1,0,0,0,0,0,0],
            [2,2,2,2,2,2,2,2,2,2]]
    level_list.append(level1)
    level2=[[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,'*'],
            [1,0,0,1,0,1,0,1,3,1],
            [0,1,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,1,3,3],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            ['p',1,0,0,0,0,0,0,0,5],
            [1,1,4,4,3,1,0,0,1,1],
            [2,2,2,2,2,2,2,2,2,2]]
    level_list.append(level2)
    level3=[[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            ['p',0,0,4,4,0,3,0,0,0],
            [1,3,3,1,0,0,1,0,1,0],
            [4,4,4,4,4,4,4,4,4,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,4,0],
            ['*',0,0,1,0,0,1,3,0,1],
            [0,0,0,0,0,0,0,0,0,0],
            [2,2,2,2,2,2,2,2,2,2]]

    level_list.append(level3)
    level4=[[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,'p',0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1]]
    level_list.append(level4)

    locked=pygame.image.load('background/png/Objects/DoorLocked.png')
    locked=pygame.transform.scale(locked,(30,60))
    opened=pygame.image.load('background/png/Objects/DoorOpen.png')
    opened=pygame.transform.scale(opened,(30,60))
    switchon=pygame.image.load('background/png/Objects/Switch (1).png')
    switchon=pygame.transform.scale(switchon,(10,40))
    switchoff=pygame.image.load('background/png/Objects/Switch (2).png')
    switchoff=pygame.transform.scale(switchoff,(10,40))
    saw=pygame.image.load('background/png/Objects/Saw.png')
    saw=pygame.transform.scale(saw,(50,50))
    door=pygame.image.load('background/png/Objects/DoorOpen.png')
    door=pygame.transform.scale(door,(30,60))
    spike=pygame.image.load('background/png/tiles/Spike.png')
    spike=pygame.transform.scale(spike,(60,30))
    screen=pygame.display.set_mode((600,660))
    acid=pygame.image.load('background/png/tiles/Acid (1).png')
    acid=pygame.transform.scale(acid,(60,60))
    floor=pygame.image.load('background/png/tiles/Tile (2).png')
    floor=pygame.transform.scale(floor,(60,60))
    bgtile=pygame.image.load("background/png/Tiles/BGTile (5).png")
    bgtile=pygame.transform.scale(bgtile,(60,60))
    spiketile=pygame.image.load('background/png/tiles/Tile (9).png')
    spiketile=pygame.transform.scale(spiketile,(60,60))

    platlist=[]
    background=pygame.Surface((600,660))
    def levelmaker():
        global Exit
        global x,y
        global switchrect
        for bgy in range(0,660,60):
            for bgx in range(0,600,60):
        ## Dividing each row and column into single integers
               


                if level_list[levelcount][bgy//60][bgx//60]==0:
                    background.blit(bgtile,(bgx,bgy))
                if level_list[levelcount][bgy//60][bgx//60]==1:
                    background.blit(floor,(bgx,bgy))
                    platform=pygame.Rect(bgx,bgy,60,1)
                    platlist.append(platform)
                    pygame.draw.rect(background,blue,platform)

                if level_list[levelcount][bgy//60][bgx//60]==2:
                    background.blit(acid,(bgx,bgy))
                if level_list[levelcount][bgy//60][bgx//60]==3:
                    background.blit(bgtile,(bgx,bgy))
                    background.blit(spiketile,(bgx,bgy))
                    trap=pygame.Rect(bgx,bgy-10,50,10)
                    spikelist.append(trap)
                    

                    background.blit(spike,(bgx,bgy-30))
                if level_list[levelcount][bgy//60][bgx//60]=='*':
                
                    
                    background.blit(bgtile,(bgx,bgy))
                    background.blit(door,(bgx+30,bgy))

                    Exit=pygame.Rect(bgx+45,bgy,5,60)
                if level_list[levelcount][bgy//60][bgx//60]=='*/':
                
                    
                    background.blit(bgtile,(bgx,bgy))
                    background.blit(locked,(bgx+30,bgy))

                    Exit=pygame.Rect(bgx+45,bgy,5,60)
                
                if level_list[levelcount][bgy//60][bgx//60]=='p':
                    background.blit(bgtile,(bgx,bgy))
                
                    
                    x,y=bgx,bgy
                if level_list[levelcount][bgy//60][bgx//60]==4:
                    background.blit(bgtile,(bgx,bgy))
                    background.blit(saw,(bgx+5,bgy+5))
                    trap=pygame.Rect(bgx+5,bgy+5,50,50)
                    spikelist.append(trap)
                if level_list[levelcount][bgy//60][bgx//60]==5:
                    background.blit(bgtile,(bgx,bgy))
                    background.blit(switchoff,(bgx+30,bgy+20))
                    switchrect=pygame.Rect(bgx,bgy,60,60)
    ##                pygame.draw.rect(background,blue,(bgx,bgy,60,60))
                    
                    
    ##                pygame.draw.rect(background,blue,(bgx+5,bgy+5,50,50))
    levelmaker()
    def showtext(text,position):
        fontobj= pygame.font.SysFont('freesans',30)
        msgobj = fontobj.render(str(text),False,blue)
        screen.blit(msgobj,position)
    while True:
    ##   player hitbox 
        player=pygame.Rect(x,y+40,30,1)
        playerhit=pygame.Rect(x,y,30,30)
        clock.tick(30)
        screen.fill(black)
        if x<0:
            x=0
        if x>570:
            x=570
        
            
        if playerhit.colliderect(Exit):
            print('why you leave')
            background.fill(black)
            levelcount=levelcount+1
            switching=0
                
            platlist=[]
            spikelist=[]
            levelmaker()

        if y >600:
            levelmaker()
        screen.blit(background,(0,0))
    ##    pygame.draw.rect(screen,blue,Exit)
        for platform in platlist:
    ##        pygame.draw.rect(screen, blue, platform)
            if platform.colliderect(player):
              
                fall=0
            
               
                break
            
            else:
                fall=1
        for trap in spikelist:
    ##        pygame.draw.rect(screen,blue,trap)
            if trap.colliderect(player):
                platlist=[]
                spikelist=[]
                levelmaker()
    ##READ: BELOW IS WHAT CHECKS WHEN THE GAME ENDS. WHEN MAKING A NEW LEVEL, INCREASE BY ONE##
    ##READ: BELOW IS WHAT CHECKS WHEN THE GAME ENDS. WHEN MAKING A NEW LEVEL, INCREASE BY ONE##

        if levelcount==4:
            showtext('The end',(250,30))
            showtext('Thanks for playing',(200,60))
            
            

        if fall==1:
            y=y+10
        if j==1 :
            if w==1 and direction==0:
                x=x+10
            elif w==1 and direction==1:
                x=x-10
            if jumpcount<9:
                y=y-20
            
            if direction==0:
                image=jump[jumpcount]
            else:
                image=pygame.transform.flip(jump[jumpcount],1,0)

           
            
            jumpcount=jumpcount+1
            if jumpcount==9:
                jumpcount=0
                j=0        
        elif w==1 or w==-1:

            if direction==0:
                image=run[runcount]
                x=x+10


            else:
                image=pygame.transform.flip(run [runcount],1,0)
                x=x-10
            runcount=runcount+1
            if runcount==9:
                runcount=0
            
                
        else:
            if direction==0:
                image=idle [idlecount]

            else:
                image=pygame.transform.flip(idle [idlecount],1,0)
            idlecount=idlecount+1
            if idlecount==9:
                idlecount=0
                

                

        screen.blit(image,(x,y))
        if switching ==1: 
            screen.blit(switchon,(switchrect.x+30,switchrect.y+20))
            screen.blit(opened,(Exit.x-15,Exit.y))
    ## READ;IMPORTANT: WHEN MAKING NEW LEVEL, INCREASE LEVELCOUNT VALUE BY ONE
        if levelcount==3:
            for bgx in range(0,endx,60):
                for bgy in range(0,endy,60):
                    pygame.draw.rect(screen,black,(bgx,bgy,60,60))
            
            endx=endx+60
            if endx>600:
                endy=endy+60
                endx=0
                if endy>600:
                    platlist=[]
                    spikelist=[]
                    levelcount=0
                    levelmaker()
                    endx=0
                    endy=0
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_RIGHT:
                    w=1
                    direction=0
                if event.key==K_UP and fall==0:
                    j=1
                if event.key==K_LEFT:
                    w=1
                    direction=1
                if event.key==K_SPACE and levelcount in [2]:
                    if playerhit.colliderect(switchrect):
                        switching=1
                        print('door is unlocked')
                    
            if event.type==KEYUP:
                if event.key==K_RIGHT:
                    w=0
                if event.key==K_LEFT:
                    w=0
            

                    
            if event.type==QUIT:
                pygame.quit()
                return
    ##ninja_platformer()


