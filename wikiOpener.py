import argparse
import webbrowser

def wiki(args):
    website = f'https://en.wikipedia.org/wiki/{str(args.searchTerm)}'
    print(website)
    webbrowser.open(website)

def main():
    parser = argparse.ArgumentParser(description='Opener')

    parser.add_argument("-w","--wiki",default=None,action="store_true",help='Open wiki page for search item')
    parser.add_argument('searchTerm',help='Search term for wiki')
    args = parser.parse_args()
    if args.wiki != None:
        wiki(args)

if __name__=='__main__':
    main()