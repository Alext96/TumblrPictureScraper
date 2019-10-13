from bs4 import BeautifulSoup
import requests
import urllib.request
import random

x = 2


def get_image(x):
    while x < 5:
        url = "https://tumblrlinkhere" + str(x)
        x += 1
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')
        tags = soup.find_all('img')
        y = 0
        for tag in tags:
            y += 1
            if y > 2:
                print(tag.get('src'))
                src = tag.get('src')
                download_image(src)


def download_image(src):
    try:
        name = random.randrange(1, 100000)
        full_name = str(name) + ".png"
        urllib.request.urlretrieve(src, full_name)
    except:
        pass


get_image(x)
