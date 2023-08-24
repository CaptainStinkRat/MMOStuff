import argparse
import webbrowser
import os

os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def wiki(args):
    website = f'https://oldschool.runescape.wiki/w/{str(args.searchTerm)}'
    print(style.MAGENTA + 'Opening wiki!')
    webbrowser.open(website)

def strategies(args):
    website = f'https://oldschool.runescape.wiki/w/{str(args.searchTerm)}/strategies'
    webbrowser.open(website)
# def scores(args):
#     person= f'https://secure.runescape.com/m=hiscore_oldschool/hiscorepersonal/{str(args.searchTerm)}'
#     print(person)
#     webbrowser.open(person)

def main():
    parser = argparse.ArgumentParser(description='Opener')

    parser.add_argument("-w","--wiki",default=None,action="store_true",help='Open wiki page for search item')
    # parser.add_argument('-s','--scores',default=None,action='store_true',help='Search someone on the Hi Scores')
    parser.add_argument('-s','--strat',default=None,action='store_true',help='Open a strategy guide on the wiki')
    parser.add_argument('searchTerm',help='Search term for wiki')
    args = parser.parse_args()
    if args.wiki != None:
        wiki(args)
    if args.strat != None:
        strategies(args)
    # if args.scores != None:
    #     scores(args)
if __name__=='__main__':
    main()