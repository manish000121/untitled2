import random
import urllib.request


def download_img(url):
    name = random.randrange(0, 20000)
    f_name = str(name)+".jpg"
    urllib.request.urlretrieve(url, f_name)
    print("ok")


download_img(r"https://www.google.com/logos/doodles/2018/dolores-olmedos-110th-birthday-5723789210943488-2x.png")
