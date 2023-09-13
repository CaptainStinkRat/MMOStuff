from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import os
win = Tk()
win.geometry('800x480')
Grid.rowconfigure(win,0,weight=1)
Grid.columnconfigure(win,0,weight=1)
Grid.rowconfigure(win,1,weight=1)
Grid.columnconfigure(win,1,weight=1)

def eatingGif():
    win.destroy()
    root = Tk()
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
    label = Label(root,width=800,height=480)
    label.pack()
    root.after(0,update,0)
def walkGif():
    win.destroy()
    root = Tk()
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
    label = Label(root,width=800,height=480)
    label.pack()
    root.after(0,update,0)
def meetingGif():
    win.destroy()
    root = Tk()
    root.title("In a meeting")
    framecnt= 10
    frames = [PhotoImage(file='./meeting.gif',format='gif -index %i' %(i)) for i in range(framecnt)]

    def update(ind):
        time.sleep(0.15)
        frame = frames[ind]
        ind += 1
        if ind == framecnt:
            ind = 0
        label.configure(image=frame)
        win.after(1,update,ind)
    label = Label(root,width=800,height=480)
    label.pack()
    root.after(0,update,0)
def busyGif():
    win.destroy()
    root = Tk()
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
    label = Label(root,width=800,height=480)
    label.pack()
    root.after(0,update,0)
# def gifPlay():
#     win.destroy()
lunchButton=ttk.Button(win,text = 'At lunch',command=eatingGif)
lunchButton.grid(column=0,row=0,sticky="NSEW")
walkButton = ttk.Button(win,text = 'On a walk',command=walkGif)
walkButton.grid(column=0,row=1,sticky='NSEW')
meetingButton=ttk.Button(win,text = 'In a meeting',command=meetingGif)
meetingButton.grid(column=1,row=0,sticky='NSEW')
busyButton=ttk.Button(win,text = 'Busy',command=busyGif)
busyButton.grid(column=1,row=1,sticky='NSEW')
# Button(win,text='At lunch',command=gifPlay).pack()
win.mainloop()