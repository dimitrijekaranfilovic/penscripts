import sys
import requests
from bs4 import BeautifulSoup, Comment


def main():
    url = sys.argv[1]
    if not url.startswith('http://') and not url.startswith('https://'):
        print(f'Url should begin with http:// or https://')
        return
    try: 
        session = requests.Session()
        response = session.get(url)
        
        print(f'Response status: {response.status_code} {response.reason}')
        
        print("== HEADERS ==")
        sorted_headers = sorted(response.headers)
        for header in sorted_headers:
            print('{:40}{}'.format(header, response.headers.get(header)))

        print("\n== COMMENTS ==")
        content_type = response.headers.get('Content-Type')
        if 'text/html' not in content_type:
            print(f"Content-Type of the response is {content_type}, text/html is expected.")
        else:
            page = response.text
            bs = BeautifulSoup(page, 'html.parser')
            comments = bs.find_all(string=lambda text: isinstance(text, Comment))
            for comment in comments:
                print(comment)

    except Exception as ex:
        print(f'An error occurred: {repr(ex)}')

if __name__ == '__main__':
    main()