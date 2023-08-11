import argparse


def experience(args):
    experienceTotal = args.experience
    print(experienceTotal)

def level(args):
    print(args.level)


def main():
    parser = argparse.ArgumentParser(description="Experience and level tracker")
    parser.add_argument("-e","--experience",default = None, help="Inputs the experience gained")
    parser.add_argument("-l","--level",metavar="num",type=int,nargs=1,default=None,help="Inputs number of levels gained")
    args = parser.parse_args()
    if args.experience != None:
        experience(args)
    elif args.level != None:
        level(args)

if __name__=="__main__":
    main()
