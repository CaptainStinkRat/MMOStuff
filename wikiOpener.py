import argparse
import webbrowser

def wiki(args):
    website = f'https://oldschool.runescape.wiki/w/{str(args.searchTerm)}'
    print(website)
    webbrowser.open(website)
def scores(args):
    person= f'https://secure.runescape.com/m=hiscore_oldschool/hiscorepersonal/{str(args.searchTerm)}'
    print(person)
    webbrowser.open(person)

def main():
    parser = argparse.ArgumentParser(description='Opener')

    parser.add_argument("-w","--wiki",default=None,action="store_true",help='Open wiki page for search item')
    parser.add_argument('-s','--scores',default=None,action='store_true',help='Search someone on the Hi Scores')
    parser.add_argument('searchTerm',help='Search term for wiki')
    args = parser.parse_args()
    if args.wiki != None:
        wiki(args)
    if args.scores != None:
        scores(args)
if __name__=='__main__':
    main()