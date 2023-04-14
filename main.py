import time
import requests
import os
#from playsound import playsound
from plyer import notification, audio

from constants import *


def play_notification():
    #playsound(os.path.join(current_path, 'sounds', 'notification.wav'))
    #os.system('termux-notification --title "Consulado" --content "Página para sacar cita activa"')
    notification.notify(
        title="Hola",
        message="Esta es una notificación de prueba.",
        app_name="Termux",
        app_icon=None
    ) 

    audio.play_effect('Bell')


def check_active_url():
    while True:
        try:
            response = requests.head(URL_LINK, allow_redirects=True)
            redirected_url = response.url
            if redirected_url == URL_CONSULADO:
                print('Consulta activa')
                play_notification()
                break
            else:
                time.sleep(60)
        except requests.exceptions.RequestException as e:
            print(str(e))
            time.sleep(60)


if __name__ == '__main__':
    check_active_url()
    