from OSRSBytes import Hiscores
from OSRSBytes import Items
import argparse
import os
import datetime
import json

def bossStart(args):
    lookupUser = args.user
    bossingUser = Hiscores(lookupUser)
    bossStartNumber = bossingUser.boss(f'{str(args.boss)}','score')
    print("Starting boss number is: "+str(bossStartNumber))
    startTime = datetime.datetime.now()
    log ={
        "User":f"{lookupUser}",
        "bossTime":f"{startTime}",
        "bossStartNumber":f"{bossStartNumber}"
    }
    jsonObject = json.dumps(log,indent=4)
    with open("bossLog.json",'w') as outfile:
        outfile.write(jsonObject)
def bossFinish(args):
    lookupUser = args.user
    bossingUser = Hiscores(lookupUser)
    dataLog = open('bossLog.json')
    data = json.load(dataLog)
    if data['User'] == f'{str(lookupUser)}':
        finishTime = datetime.datetime.now()
        finishTimeStamp = int(finishTime.timestamp())
        dateFormat = '%Y-%m-%d %H:%M:%S'
        dateStr = data['bossTime']
        dateObj = datetime.strptime(dateStr,dateFormat)
        startTimeStamp = int(dateObj)
        totalTime = finishTimeStamp - startTimeStamp
        dateTimeObj = datetime.fromtimestamp(totalTime)
        print("Time lapsed: "+str(dateTimeObj))
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
