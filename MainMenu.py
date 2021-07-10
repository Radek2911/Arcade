from tkinter import *
from tkinter import font
from tkinter import messagebox
from Memory_Game_two import memory_game
from minesweepermenu import MineSweeper
from ninja_platformer import Ninja_Platformer
import time
import random
import string
def menu():
    root=Tk()
    root.title("Memory game")
      
    button1=Button(root, text='Memory Game', activeforeground= '#EE3B3B', overrelief='flat', relief='flat', borderwidth=2,
        highlightthickness=1, font=font.Font(family='SignPainter', size=40, weight='bold', slant='roman'),
        highlightbackground='#CD5555', foreground='#1F1F1F', background='#7A7A7A',
            command=memory_game)
    button1.grid(column=0,row=1,sticky='NSEW')

    button2=Button(root, text='MineSweeper', activeforeground= '#EE3B3B', overrelief='flat', relief='flat', borderwidth=2,
        highlightthickness=1, font=font.Font(family='SignPainter', size=40, weight='bold', slant='roman'),
        highlightbackground='#CD5555', foreground='#1F1F1F', background='#7A7A7A',
            command=MineSweeper)
    button2.grid(column=0,row=2,sticky='NSEW')

    button3=Button(root, text='Ninja Platformer', activeforeground= '#EE3B3B', overrelief='flat', relief='flat', borderwidth=2,
        highlightthickness=1, font=font.Font(family='SignPainter', size=40, weight='bold', slant='roman'),
        highlightbackground='#CD5555', foreground='#1F1F1F', background='#7A7A7A',
          command=Ninja_Platformer)
    button3.grid(column=0,row=3,sticky='NSEW')

    root.mainloop()
menu() 
