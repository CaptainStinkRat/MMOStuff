from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import os
import tkinter.font as font
# win = Tk()
# win.geometry('800x480')
# win.attributes('-fullscreen',True)
# win.configure(background='black')
# Grid.rowconfigure(win,0,weight=1)
# Grid.columnconfigure(win,0,weight=1)
# Grid.rowconfigure(win,1,weight=1)
# Grid.columnconfigure(win,1,weight=1)
def eatingGif():
    win.destroy()
    root = Tk()
    root.configure(background='black')
    root.attributes('-fullscreen',True)
    framecnt= 6
    frames = [PhotoImage(file='./Eating.gif',format='gif -index %i' %(i)) for i in range(framecnt)]

    def update(ind):
        time.sleep(0.15)
        frame = frames[ind]
        ind += 1
        if ind == framecnt:
            ind = 0
        label.configure(image=frame)
        win.after(1,update,ind)
    label = Label(root)
    label.pack()
    title = Label(root,text='On lunch',font=('Arial',35),fg='#FFFFFF',bg='#000000')
    title.pack()
    root.after(0,update,0)
    backButton = Button(root,text='Back',command=root.destroy)
    backButton['font']=myFont
    backButton.pack()
def walkGif():
    win.destroy()
    root = Tk()
    root.configure(bg='black')
    root.attributes('-fullscreen',True)
    root.title("On a walk")
    framecnt= 20
    frames = [PhotoImage(file='./walking.gif',format='gif -index %i' %(i)) for i in range(framecnt)]

    def update(ind):
        time.sleep(0.15)
        frame = frames[ind]
        ind += 1
        if ind == framecnt:
            ind = 0
        label.configure(image=frame)
        win.after(1,update,ind)
    label = Label(root)
    label.pack()
    title = Label(root,text='On a walk',font=('Arial',35),fg='#FFFFFF',bg='#000000')
    title.pack()
    root.after(0,update,0)
    backButton = Button(root,text='Back',command=root.destroy)
    backButton['font']=myFont
    backButton.pack()
def meetingGif():
    win.destroy()
    root = Tk()
    root.configure(bg='black')
    root.attributes('-fullscreen',True)
    root.title("In a meeting")
    framecnt= 35
    frames = [PhotoImage(file='./meeting.gif',format='gif -index %i' %(i)) for i in range(framecnt)]

    def update(ind):
        time.sleep(0.1)
        frame = frames[ind]
        ind += 1
        if ind == framecnt:
            ind = 0
        label.configure(image=frame)
        win.after(1,update,ind)
    label = Label(root)
    label.pack()
    title = Label(root,text='In a meeting',font=('Arial',35),fg='#FFFFFF',bg='#000000')
    title.pack()
    root.after(0,update,0)
    backButton = Button(root,text='Back',command=root.destroy)
    backButton['font']=myFont
    backButton.pack()
def busyGif():
    win.destroy()
    root = Tk()
    root.configure(bg='black')
    root.attributes('-fullscreen',True)
    root.geometry('800x480')
    root.title("Busy")
    framecnt= 10
    frames = [PhotoImage(file='./busy.gif',format='gif -index %i' %(i)) for i in range(framecnt)]

    def update(ind):
        time.sleep(0.15)
        frame = frames[ind]
        ind += 1
        if ind == framecnt:
            ind = 0
        label.configure(image=frame)
        win.after(1,update,ind)
    label = Label(root,text='Busy working')
    label.pack()
    title = Label(root,text='Busy',font=('Arial',35),fg='#FFFFFF',bg='#000000')
    title.pack()
    root.after(0,update,0)
    backButton = Button(root,text='Back',command=root.destroy)
    backButton['font']=myFont
    backButton.pack()
def idleGif():
    win.destroy()
    root = Tk()
    root.configure(bg='black')
    root.attributes('-fullscreen',True)
    root.geometry('800x480')
    root.title("Idle")
    framecnt= 48
    frames = [PhotoImage(file='./idle.gif',format='gif -index %i' %(i)) for i in range(framecnt)]

    def update(ind):
        time.sleep(0.06)
        frame = frames[ind]
        ind += 1
        if ind == framecnt:
            ind = 0
        label.configure(image=frame)
        win.after(1,update,ind)
    label = Label(root,text='Busy working')
    label.pack()
    root.after(0,update,0)
    backButton = Button(root,text='Back',command=root.destroy)
    backButton['font']=myFont
    backButton.pack()
# def gifPlay():
#     win.destroy()

win = Tk()
win.geometry('800x480')
win.attributes('-fullscreen',True)  
win.configure(background='black')
Grid.rowconfigure(win,0,weight=1)
Grid.columnconfigure(win,0,weight=1)
Grid.rowconfigure(win,1,weight=1)
Grid.columnconfigure(win,1,weight=1)
myFont = font.Font(family='Helvetica',size=35,weight='bold')
lunchButton=Button(win,text = 'At lunch',command=eatingGif)
lunchButton['font']=myFont
lunchButton.grid(column=0,row=0,sticky="NSEW")
walkButton = Button(win,text = 'On a walk',command=walkGif)
walkButton.grid(column=0,row=1,sticky='NSEW')
walkButton['font']=myFont
meetingButton=Button(win,text = 'In a meeting',command=meetingGif)
meetingButton.grid(column=1,row=0,sticky='NSEW')
meetingButton['font']=myFont
busyButton=Button(win,text = 'Busy',command=busyGif)
busyButton.grid(column=1,row=1,sticky='NSEW')
busyButton['font']=myFont
idleButton=Button(win,text = 'Idle',command=idleGif)
idleButton.grid(columnspan=2,row=2,sticky='NSEW')
idleButton['font']=myFont
    # Button(win,text='At lunch',command=gifPlay).pack()
win.mainloop()

