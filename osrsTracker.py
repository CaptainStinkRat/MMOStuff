from OSRSBytes import Hiscores
from OSRSBytes import Items
import argparse
import os
from datetime import datetime
import json

def bossStart(args):
    lookupUser = args.user
    bossingUser = Hiscores(lookupUser)
    bossStartNumber = bossingUser.boss(f'{str(args.boss)}','score')
    print("Starting boss number is: "+str(bossStartNumber))
    sTime = datetime.now()
    startTime = sTime.strftime("%H:%M:%S")
    log ={
        "Boss":f"{str(args.boss)}",
        "User":f"{lookupUser}",
        "bossTime":f"{startTime}",
        "bossStartNumber":f"{bossStartNumber}"
    }
    jsonObject = json.dumps(log,indent=4)
    with open("bossLog.json",'w') as outfile:
        outfile.write(jsonObject)
def bossFinish(args):
    lookupUser = args.user
    dataLog = open('bossLog.json')
    data = json.load(dataLog)
    os.remove("bossLog.json")
    if data['User'] == f'{str(lookupUser)}':
        bossingUserStats = data['User']
        bossUser = Hiscores(bossingUserStats)
        bossingUserStart=data['bossStartNumber']
        boss = data['Boss']
        bossFinish = bossUser.boss(f'{boss}')
        bossTotal = int(bossingUserStart)-int(bossFinish)
        fTime = datetime.now()
        finishTime = fTime.strftime("%H:%M:%S")
        #finishTimeStamp = int(finishTime)
        dateStr = data['bossTime']
        #startTimeStamp = int(dateStr)
        sT = datetime.strptime(dateStr,"%H:%M:%S")
        fT = datetime.strptime(finishTime,"%H:%M:%S")
        totalTime = fT - sT
        print("Time lapsed: "+str(totalTime)+" and "+str(bossTotal)+" killed in that time.")
        log ={
            "Boss":f"{str(args.boss)}",
            "User":f"{bossingUserStats}",
            "timeLapsed":f"{totalTime}",
            "totalKilled":f"{bossTotal}"
        }
        jsonObject = json.dumps(log,indent=4)
        with open("bossEndLog.json",'w') as outfile:
            outfile.write(jsonObject)
def main():
    parser = argparse.ArgumentParser(description='Boss Tracker')
    parser.add_argument("-s","--start",default = None,action="store_true",help='Start of the bossing log')
    parser.add_argument("-f","--finish",default=None,action='store_true',help='Finish of bossing time')
    parser.add_argument('user',help='User to keep track of boss kills for')
    parser.add_argument('boss',help='Boss to keep track of')
    args= parser.parse_args()
    if args.start != None:
        bossStart(args)
    if args.finish != None:
        bossFinish(args)

if __name__ == '__main__':
    main()
