from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
import time
import os
import tkinter.font as font
#
import time
# win = Tk()
# win.geometry('800x480')
# win.attributes('-fullscreen',True)
# win.configure(background='black')
# Grid.rowconfigure(win,0,weight=1)
# Grid.columnconfigure(win,0,weight=1)
# Grid.rowconfigure(win,1,weight=1)
# Grid.columnconfigure(win,1,weight=1)
brickCount = 0 

def codeCount():
    pass
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(18,GPIO.OUT)
    # servo = GPIO.PWM(18,50)
    # servo.start(0)
    # time.sleep(1)
    # duty=2
    # while duty<=17:
    #     servo.ChangeDutyCycle(duty)
    #     time.sleep(1)
    #     duty=duty+1
    # servo.ChangeDutyCycle(2)
    # time.sleep(2)
    # servo.ChangeDutyCycle(0)
    # servo.stop()
    # GPIO.cleanup()
win = Tk()
win.geometry('800x480')
win.attributes('-fullscreen',True)  
win.configure(background='black')
Grid.rowconfigure(win,0,weight=1)
Grid.columnconfigure(win,0,weight=1)

myFont = font.Font(family='Helvetica',size=35,weight='bold')
photo = PhotoImage(file="Harry.png")
photo2 = PhotoImage(file="ron.png")
photo3 = PhotoImage(file="hermione.png")
lunchButton=Button(win,image=photo,command=codeCount)

lunchButton.grid(column=0,row=0,sticky="NSEW")

meetingButton=Button(win,image=photo2,command=codeCount)
meetingButton.grid(column=1,row=0,sticky='NSEW')

busyButton=Button(win,image=photo3,command=codeCount)
busyButton.grid(column=2,row=0,sticky='NSEW')


    # Button(win,text='At lunch',command=gifPlay).pack()
win.mainloop()
