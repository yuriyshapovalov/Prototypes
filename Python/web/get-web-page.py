from urllib import request, error
import sys

def main(url):
    headers = {}
    
    try: response = request.urlopen(url)
    except error.URLError as e:
        print(e.reason)
    else:
        print(response.read())

if __name__ == '__main__':
    main(str(sys.argv[1]))
