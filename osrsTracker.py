import argparse 
import sys

# def experience(args):
#     experienceTotal = args.experience
#     print(experienceTotal)
#     gainsList = []
#     # with open('Gains.json') as fp:
#     #     gainsList = json.load(fp)
#     gainsList.append({
#         "experience":experienceTotal
#     })
#     with open('Gains.json','w') as outfile:
#         json.dump(gainsList,outfile,indent=4,separators=(',',': '))

def new(args):
    newExperienceTracker = args.experience
    with open(args.fileName,'w') as f:
        f.write(newExperienceTracker)
        f.close()

    # print(newExperienceTracker)
    # newGainsList = []
    # newGainsList.append({
    #     "experience":newExperienceTracker
    # })
    # with open('Gains.json','w') as outfile:
    #     json.dump(newGainsList,outfile,indent=4,separators=(',',': '))

def add(args):
    existingExperienceTracker = int(args.experience)
    with open(args.fileName,'r+') as f:
        total = sum(int(line) for line in f if line.strip())
        total += existingExperienceTracker
        print(total)
        f.seek(0)
        f.truncate()
        f.write(str(total))
    

    # print(existingExperienceTracker)
    # gainsList = []
    # with open('Gains.json') as fp:
    #     gainsList = json.load(fp)

    # gainsList.append({
    #     "experience":existingExperienceTracker
    # })
    # with open('Gains.json','w') as outfile:
    #     json.dump(existingExperienceTracker,outfile,indent=4,separators=(',',': '))

# def level(args):
#     print(args.level)


def main():
    parser = argparse.ArgumentParser(description="Experience and level tracker")

    parser.add_argument("-a","--add",default=None,action="store_true", help = "Add experience to total gained")
    parser.add_argument("-n","--new",default=None,action="store_true",help = "Create a new experience tracker")
    parser.add_argument("fileName",help="File location for storage")
    parser.add_argument("experience",help="Experience gained")

    # parser.add_argument("-e","--experience",default = None, help="Inputs the experience gained")
    # parser.add_argument("-l","--level",metavar="num",type=int,nargs=1,default=None,help="Inputs number of levels gained")
    args = parser.parse_args()
    if args.new != None:
        new(args)
    elif args.add != None:
        add(args)

if __name__=="__main__":
    main()
