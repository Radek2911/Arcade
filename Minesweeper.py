import pygame
import random
import time
from pygame.locals import *
def thegame(difficulty):
    class Block():
        def __init__ (self,x,y,size):
            self.x=x
            self.y=y
            self.size=size
            self.value=''
            self.show=0
        def draw(self):
            screen.blit(mineblock,(self.x,self.y))
        def isclicked(self,pos,button):
            if self.show==0 and pos[0]in range(self.x,self.x+self.size)and pos[1] in range(self.y,self.y+self.size) and button==1:
                if self.value==1:
                    screen.blit(oneblock,(self.x,self.y))
                if self.value=='*':
                    screen.blit(mine,(self.x,self.y))
                    show_text('You went boom',300,300,((0,0,0)))
                    pygame.display.update()
                    time.sleep(3)
                    return'mine'
                if self.value==0:
                    screen.blit(empty,(self.x,self.y))
                if self.value==2:
                    screen.blit(twoblock,(self.x,self.y))
                if self.value==3:
                    screen.blit(threeblock,(self.x,self.y))
                self.show=1
            if self.show==0 and pos[0]in range(self.x,self.x+self.size)and pos[1] in range(self.y,self.y+self.size) and button==3:
                screen.blit(flagged,(self.x,self.y))
                flaglist.append((self.x,self.y))

    screen=pygame.display.set_mode((600,600))
    grey=(0,20,0)
    def show_text(msg,x,y,color):

        fontobj= pygame.font.SysFont('freesans',50)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
    size=600//difficulty



    blocklayout=[]
    blocklist=[]
    flaglist=[]
    ##for x in range(0,600,150):
    ##    for y in range(0,600,150):
           
    minelist=[]
    for loop2 in range(0,difficulty,1):
        row=[]
        for loop3 in range(0,difficulty,1):
            row.append(0)
        blocklayout.append(row)

    for loop in range(0,difficulty//2,1):
        minex=random.randint(0,difficulty-1)
        miney=random.randint(0,difficulty-1)

        while blocklayout[miney][minex]=='*':
            minex=random.randint(0,difficulty-1)
            miney=random.randint(0,difficulty-1)

        blocklayout[miney][minex]='*'
        minelist.append((minex*size,miney*size))
    ##the code beneath this sets the location of each number block    
        try:
            if minex>0:
                blocklayout[miney][minex-1]+=1
        except TypeError:
            print ("found a mine skipping block")
        try:
            if miney>0 and minex>0:
                blocklayout[miney-1][minex-1]+=1
        except TypeError:
            print ("found a mine skipping block")
        try:
            if miney>0:
                blocklayout[miney-1][minex]+=1
        except TypeError:
            print ("found a mine skipping block")
        try:
            if minex<difficulty-1 and miney>0:
                blocklayout[miney-1][minex+1]+=1
        except TypeError:
            print ("found a mine skipping block")
        try:
            if minex<difficulty-1:
                blocklayout[miney][minex+1]+=1
        except TypeError:
            print ("found a mine skipping block")
        try:
            if miney<difficulty-1 and minex<difficulty-1:    
                blocklayout[miney+1][minex+1]+=1
        except TypeError:
            print ("found a mine skipping block")
        try:
            if miney<difficulty-1:
                blocklayout[miney+1][minex]+=1
        except TypeError:
            print ("found a mine skipping block")
        try:
            if miney<difficulty-1 and minex>0:
                blocklayout[miney+1][minex-1]+=1
        except TypeError:
            print ("dude, there's a mine")
        print(blocklayout)
    ##up till here

  
    for y in range(0,difficulty,1):
        for x in range(0,difficulty,1):
           
            block=Block(x*size,y*size,size)
            block.value=blocklayout[y][x]
            blocklist.append(block)
    mineblock=pygame.image.load('mineblock.png')
    mineblock=pygame.transform.scale(mineblock,(size,size))
    oneblock=pygame.image.load('block1.png')
    oneblock=pygame.transform.scale(oneblock,(size,size))
    twoblock=pygame.image.load('block2.png')
    twoblock=pygame.transform.scale(twoblock,(size,size))
    threeblock=pygame.image.load('block3.png')
    threeblock=pygame.transform.scale(threeblock,(size,size))
    fourblock=pygame.image.load('block4.png')
    mine=pygame.image.load('mine.png')
    mine=pygame.transform.scale(mine,(size,size))
    empty=pygame.image.load('empty.png')
    empty=pygame.transform.scale(empty,(size,size))
    flagged=pygame.image.load('flagged.png')
    flagged=pygame.transform.scale(flagged,(size,size))
    for block in blocklist:
        block.draw()
    while True:
        pygame.display.update()
        if set (minelist)==set (flaglist):
            show_text('YOU WIN',200,200,((0,0,0)))
            pygame.display.update()
            time.sleep(3)
            return
                    
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                print(minelist,flaglist)
                for block in blocklist:
                    variable=block.isclicked(event.pos,event.button)
                    if variable=='mine':
                        screen.fill((0,0,0))
                        return
                
            if event.type==QUIT:
                pygame.quit()
                exit()

            

