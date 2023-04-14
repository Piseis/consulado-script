import time
import requests
import os

from constants import *

def play_notification():
    os.system("termux-vibrate -d 5000")


def check_active_url():
    while True:
        try:
            response = requests.head(URL_LINK, allow_redirects=True)
            redirected_url = response.url
            if redirected_url == URL_CONSULADO:
                play_notification()
                print('Consulta activa')
                break
            else:
                time.sleep(60)
        except requests.exceptions.RequestException as e:
            print(str(e))
            time.sleep(60)


if __name__ == '__main__':
    check_active_url()
    