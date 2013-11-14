from urllib.request import urlopen

def main():
    url = 'http://google.com'
    headers = {}
    response = urlopen(url)

    print(response.read())

if __name__ == '__main__':
    main()
