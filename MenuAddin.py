import tkinter as tk
from OSRSBytes import Hiscores
from OSRSBytes import Items
import json
import tkinter.font as font
import time
from datetime import datetime
from tkinter import *
import os

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x480')
        self.attributes('-fullscreen',True)
        # self.configure(background='black')
        Grid.rowconfigure(self,0,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.columnconfigure(self,1,weight=1)
        self.myFont = font.Font(family='Helvetica' ,size=35,weight='bold')
        # self.timeLabel = tk.Label(self,text='0.00')
        # self.timeLabel.pack()
        # self.timeLabel['font'] = self.myFont
        self.isRunning = False
        self.startTime = time.time()
        self.bossUser = Hiscores('dad_pvmer')
        self.createWidgets()
    def createWidgets(self):    
        # self.startButton = Button(self,text='Start timer',command=self.start)
        # self.startButton['font'] =self.myFont
        # self.startButton.pack()
        self.wintertodtButton = Button(self,text='Wintertodt',command=self.wintertodtStart)
        self.wintertodtButton['font'] = self.myFont
        self.wintertodtButton.grid(column=0,row=0,sticky="NSEW")
        self.kbdButton = Button(self,text='KBD',command=self.kbdStart)
        self.kbdButton['font']=self.myFont
        self.kbdButton.grid(column=1,row=0,sticky="NSEW")
        self.giantMoleButton = Button(self,text='Giant Mole',command=self.giantMoleStart)
        self.giantMoleButton['font']=self.myFont
        self.giantMoleButton.grid(column=0,row=1,sticky="NSEW")
        self.kalphiteQueenButton = Button(self,text='KQ',command=self.kqStart)
        self.kalphiteQueenButton['font']=self.myFont
        self.kalphiteQueenButton.grid(column=1,row=1,sticky="NSEW")
        self.cerberusButton = Button(self,text='Cerberus',command=self.cerberusStart)
        self.cerberusButton['font']=self.myFont
        self.cerberusButton.grid(column=2,row=1,sticky="NSEW")
        self.krakenButton = Button(self,text='Kraken',command=self.krakenStart)
        self.krakenButton['font']=self.myFont
        self.krakenButton.grid(column=2,row=0,sticky="NSEW")
    def updateTime(self):
        if self.isRunning:
            self.elapsedTime=time.time() - self.startTime
            self.timeLabel.config(text="{:.2f}".format(self.elapsedTime))
            self.timeLabel.after(50,self.updateTime)
    def krakenStart(self):
        self.boss = 'kraken'
        self.bossStartNumber = self.bossUser.boss(f'{self.boss}','score')
        self.wintertodtButton.destroy()
        self.krakenButton.destroy()
        self.kbdButton.destroy()
        self.giantMoleButton.destroy()
        self.kalphiteQueenButton.destroy()
        self.cerberusButton.destroy()
        self.startButton = Button(self,text='Start timer',command=self.start)
        self.startButton['font'] =self.myFont
        self.startButton.grid(column=0,row=1,sticky="NSEW")
    def wintertodtStart(self):
        self.boss = 'wintertodt'
        self.bossStartNumber = self.bossUser.boss(f'{self.boss}','score')
        self.wintertodtButton.destroy()
        self.krakenButton.destroy()
        self.kbdButton.destroy()
        self.giantMoleButton.destroy()
        self.kalphiteQueenButton.destroy()
        self.cerberusButton.destroy()
        self.startButton = Button(self,text='Start timer',command=self.start)
        self.startButton['font'] =self.myFont
        self.startButton.grid(column=0,row=1,sticky="NSEW")

    def kbdStart(self):
        self.boss = 'KingBlackDragon'
        self.bossStartNumber = self.bossUser.boss(f'{self.boss}','score')
        self.wintertodtButton.destroy()
        self.kbdButton.destroy()
        self.giantMoleButton.destroy()
        self.kalphiteQueenButton.destroy()
        self.cerberusButton.destroy()
        self.krakenButton.destroy()
        self.startButton = Button(self,text='Start timer',command=self.start)
        self.startButton['font'] =self.myFont
        self.startButton.grid(column=0,row=1,sticky="NSEW")

    def giantMoleStart(self):
        self.boss = 'GiantMole'
        self.bossStartNumber = self.bossUser.boss(f'{self.boss}','score')
        self.wintertodtButton.destroy()
        self.kbdButton.destroy()
        self.giantMoleButton.destroy()
        self.kalphiteQueenButton.destroy()
        self.cerberusButton.destroy()
        self.krakenButton.destroy()
        self.startButton = Button(self,text='Start timer',command=self.start)
        self.startButton['font'] =self.myFont
        self.startButton.grid(column=0,row=1,sticky="NSEW")
    
    def startButtonAdd(self):
        self.wintertodtButton.destroy()
        self.kbdButton.destroy()
        self.giantMoleButton.destroy()
        self.kalphiteQueenButton.destroy()
        self.cerberusButton.destroy()
        self.krakenButton.destroy()
        self.startButton = Button(self,text='Start timer',command=self.start)
        self.startButton['font'] =self.myFont
        self.startButton.grid(column=0,row=1,sticky="NSEW")

    def kqStart(self):
        self.boss = 'KalphiteQueen'
        self.bossStartNumber = self.bossUser.boss(f'{self.boss}','score')
        self.wintertodtButton.destroy()
        self.kbdButton.destroy()
        self.giantMoleButton.destroy()
        self.kalphiteQueenButton.destroy()
        self.cerberusButton.destroy()
        self.krakenButton.destroy()
        self.startButton = Button(self,text='Start timer',command=self.start)
        self.startButton['font'] =self.myFont
        self.startButton.grid(column=0,row=1,sticky="NSEW")

    def cerberusStart(self):
        self.boss = 'cerberus'
        self.bossStartNumber = self.bossUser.boss(f'{self.boss}','score')
        self.wintertodtButton.destroy()
        self.kbdButton.destroy()
        self.giantMoleButton.destroy()
        self.kalphiteQueenButton.destroy()
        self.cerberusButton.destroy()
        self.krakenButton.destroy()
        self.startButton = Button(self,text='Start timer',command=self.start)
        self.startButton['font'] =self.myFont
        self.startButton.grid(column=0,row=0,sticky="NSEW")
    def start(self):
        self.startButton.destroy()
        self.stopButton = Button(self,text='Stop timer',command=self.stop)
        self.stopButton['font'] =self.myFont
        self.stopButton.grid(column=0,row=0,sticky="NSEW")
        self.timeLabel = tk.Label(self,text='0.00')
        self.timeLabel.grid(column=0,row=1,sticky="NSEW")
        self.timeLabel['font'] = self.myFont
        sTime = datetime.now()
        startTime = sTime.strftime("%H:%M:%S")
        log ={
            "User":"dad_pvmer",
            "bossTime":f"{startTime}",
            "bossStartNumber":f"{self.bossStartNumber}"
        }
        jsonObject = json.dumps(log,indent=4)
        with open("bossLog.json",'w') as outfile:
            outfile.write(jsonObject)
        if not self.isRunning:
            self.isRunning = True
            self.startTime = time.time()
            self.updateTime()
    def stop(self):
        self.stopButton.destroy()
        self.timeLabel.destroy()
        self.isRunning = False
        dataLog = open('bossLog.json')
        data = json.load(dataLog)
        endingBossCount = self.bossUser.boss(f'{self.boss}','score')
        self.bossEndNumber = self.bossStartNumber - endingBossCount
        if data['User'] == 'dad_pvmer':
            fTime = datetime.now()
            finishTime = fTime.strftime("%H:%M:%S")
        #finishTimeStamp = int(finishTime)
            dateStr = data['bossTime']
        #startTimeStamp = int(dateStr)
            sT = datetime.strptime(dateStr,"%H:%M:%S")
            fT = datetime.strptime(finishTime,"%H:%M:%S")
            totalTime = fT - sT
            finishedLog = {
                "User":"dad_pvmer",
                "bossTotalTime":f'{totalTime}',
                'numberOfBossesKilled':f'{self.bossEndNumber}'
            }
            jsonObject = json.dumps(finishedLog,indent=4)
            with open("finishedBossLog.json",'w') as outfile:
                outfile.write(jsonObject)
        
        self.killLabel = Label(text='Number of bosses killed: ' +finishedLog['numberOfBossesKilled'])
        self.killLabel['font']=self.myFont
        self.killLabel.grid(row=0,column=0)
        self.timeLapsedLabel = Label(text='Time lapsed: '+finishedLog['bossTotalTime'])
        self.timeLapsedLabel.grid(row=1,column=0)
        self.timeLapsedLabel['font']=self.myFont
        # self.avgKillTimeLabel = Label(text='Average kill time: '+self.avgKillTime)
        # self.avgKillTimeLabel.grid(row=0,column=1)
        # self.avgKillTimeLabel['font']=self.myFont
        self.exitButton = Button(self,text='Exit',command=self.exit)
        self.exitButton['font']=self.myFont
        self.exitButton.grid(row=1,column=1,sticky='NSEW')
    def exit(self):
        self.destroy()
if __name__=='__main__':
    app=Menu()
    app.mainloop()
