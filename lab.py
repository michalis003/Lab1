import requests  # εισαγωγή της βιβλιοθήκης
import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

# url = 'http://python.org/'  # προσδιορισμός του url
# url="www.google.com"


url = input("Give url: \t")

if not url.startswith('https://'):
     url = 'https://' + url

print(url)


with requests.get(url) as response:

    print(f"Server: {response.headers.get('Server')}")
    print(f"Has cookies:{'Set-Cookie' in response.headers}")

    cookies = response.cookies
    print("Cookies received")
    for cookie in cookies:
        print("-" * 30)
        print(f"Name: {cookie.name}")
        exp = datetime.datetime.fromtimestamp(cookie.expires)
        print(f"Expires: {exp}")
        



