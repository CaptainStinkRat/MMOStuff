from OSRSBytes import Hiscores
from OSRSBytes import Items
import argparse
import os

def bossStart(args):
    lookupUser = args.user
    bossingUser = Hiscores(lookupUser)
    bossStartNumber = bossingUser.boss(f'{str(args.boss)}','score')
    print("Starting boss number is: "+str(bossStartNumber))
def main():
    parser = argparse.ArgumentParser(description='Boss Tracker')
    parser.add_argument("-s","--start",default = None,action="store_true",help='Start of the bossing log')
    parser.add_argument('user',help='User to keep track of boss kills for')
    parser.add_argument('boss',help='Boss to keep track of')
    args= parser.parse_args()
    if args.start != None:
        bossStart(args)

if __name__ == '__main__':
    main()
