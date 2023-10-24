from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import os
import tkinter.font as font
import RPi.GPIO as GPIO
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
    if brickCount == 0:
        brickCount+1
    elif brickCount == 1:
        brickCount+1
    elif brickCount == 2:
        brickCount+1
    elif brickCount == 3:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18,GPIO.OUT)
        servo = GPIO.PWM(18,50)
        servo.start(0)
        time.sleep(1)
        duty=2
        while duty<=17:
            servo.ChangeDutyCycle(duty)
            time.sleep(1)
            duty=duty+1
        servo.ChangeDutyCycle(2)
        time.sleep(2)
        servo.ChangeDutyCycle(0)
        servo.stop()
        GPIO.cleanup()
win = Tk()
win.geometry('800x480')
win.attributes('-fullscreen',True)  
win.configure(background='black')
Grid.rowconfigure(win,0,weight=1)
Grid.columnconfigure(win,0,weight=1)
Grid.rowconfigure(win,1,weight=1)
Grid.columnconfigure(win,1,weight=1)
myFont = font.Font(family='Helvetica',size=35,weight='bold')
photo = PhotoImage(file="/brick.jpg")
lunchButton=Button(win,image=photo,command=codeCount)
lunchButton['font']=myFont
lunchButton.grid(column=0,row=0,sticky="NSEW")
walkButton = Button(win,image=photo,command=codeCount)
walkButton.grid(column=0,row=1,sticky='NSEW')
walkButton['font']=myFont
meetingButton=Button(win,image=photo,command=codeCount)
meetingButton.grid(column=1,row=0,sticky='NSEW')
meetingButton['font']=myFont
busyButton=Button(win,image=photo,command=codeCount)
busyButton.grid(column=1,row=1,sticky='NSEW')
busyButton['font']=myFont
idleButton=Button(win,image=photo,command=codeCount)
idleButton.grid(columnspan=2,row=2,sticky='NSEW')
idleButton['font']=myFont
    # Button(win,text='At lunch',command=gifPlay).pack()
win.mainloop()
