import sys
import requests
from bs4 import BeautifulSoup, Comment

ANSI_RESET = '\u001b[0m'
ANSI_RED = '\u001b[31m'

def main():
    url = sys.argv[1]
    if not url.startswith('http://') and not url.startswith('https://'):
        print(f'Url should begin with http:// or https://')
        return
    try: 
        session = requests.Session()
        response = session.get(url)
        page = response.text
        bs = BeautifulSoup(page, 'html.parser')
        comments = bs.find_all(string=lambda text: isinstance(text, Comment))

        print(ANSI_RED + "## HEADERS ##\n" + ANSI_RESET)

        print(f'{response.status_code} {response.reason}')
        for header, value in response.headers.items():
            print(f'{header}: {value}')

        print('\n' + ANSI_RED + '## COMMENTS ##\n' + ANSI_RESET)
        for comment in comments:
            print(comment)

    except Exception as ex:
        print(f'An error occurred: {repr(ex)}')

if __name__ == '__main__':
    main()