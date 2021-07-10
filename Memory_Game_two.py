from tkinter import *
from tkinter import messagebox
import time
import random
import string
counter=0
def memory_game():
    root=Toplevel()
    root.geometry('256x256')
    root.title("Memory game")

   
    for i in range(0,4):
        
        Grid.rowconfigure(root,i,weight=1)
        Grid.columnconfigure(root,i,weight=1)

    oneight=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
    random.shuffle(oneight)
    global clicks
    global numbers
    global counter
    clicks=0
    numbers=[]
    counter=0
    def pic(index):
        global clicks
        global numbers
        global counter
        if index not in numbers:
            
            clicks=clicks+1
            #print(oneight[index])
            buttons[index].configure(image=(images[index]))
            numbers.append(index)
            root.update()
            if clicks ==2:
                counter=counter+1

                time.sleep(1)
                if oneight[index]!=oneight[numbers[0]]:
                    buttons[index].configure(image=empty)
                    buttons[numbers[0]].configure(image=empty)
                    counter=counter-1
                print(counter)
                clicks=0
                numbers=[]
                if counter>=8:
                    print('end game')
                    time.sleep(3)
                    root.destroy()
            
        
        
        
    empty=PhotoImage(file='empty.png')
    empty=empty.zoom(4,4)
    images=[]
    for loop in oneight:
        Nums=PhotoImage(file='block'+str(loop)+'.png')
        Nums=Nums.zoom(4,4)
        images.append(Nums)
    
        
     
  
    
    button1=Button(root, image=empty, command=lambda:pic(0))
    button2=Button(root, image=empty, command=lambda:pic(1))
    button3=Button(root, image=empty, command=lambda:pic(2))
    button4=Button(root, image=empty, command=lambda:pic(3))
    button5=Button(root, image=empty, command=lambda:pic(4))
    button6=Button(root, image=empty, command=lambda:pic(5))
    button7=Button(root, image=empty, command=lambda:pic(6))
    button8=Button(root,image=empty, command=lambda:pic(7))
    button9=Button(root,image= empty, command=lambda:pic(8))
    button10=Button(root, image=empty, command=lambda:pic(9))
    button11=Button(root, image=empty, command=lambda:pic(10))
    button12=Button(root,image=empty, command=lambda:pic(11))
    button13=Button(root, image=empty, command=lambda:pic(12))
    button14=Button(root,image=empty, command=lambda:pic(13))
    button15=Button(root, image=empty, command=lambda:pic(14))
    button16=Button(root, image=empty, command=lambda:pic(15))

    buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9,
    button10,button11,button12,button13,button14,button15,button16]
   

    button1.grid(column=0,row=0,sticky='NSEW')
    button2.grid(column=1,row=0,sticky='NSEW')
    button3.grid(column=2,row=0,sticky='NSEW')
    button4.grid(column=3,row=0,sticky='NSEW')
    button5.grid(column=0,row=1,sticky='NSEW')
    button6.grid(column=1,row=1,sticky='NSEW')
    button7.grid(column=2,row=1,sticky='NSEW')
    button8.grid(column=3,row=1,sticky='NSEW')
    button9.grid(column=0,row=2,sticky='NSEW')
    button10.grid(column=1,row=2,sticky='NSEW')
    button11.grid(column=2,row=2,sticky='NSEW')
    button12.grid(column=3,row=2,sticky='NSEW')
    button13.grid(column=0,row=3,sticky='NSEW')
    button14.grid(column=1,row=3,sticky='NSEW')
    button15.grid(column=2,row=3,sticky='NSEW')
    button16.grid(column=3,row=3,sticky='NSEW')

    root.mainloop()
##memory_game()

