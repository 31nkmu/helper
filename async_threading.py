from threading import Thread
import datetime
import time
import random


def schedule_loop(bot):
    print('hello')


# Создаем новый поток и в нем запускаем нашу функцию:
Thread(target=schedule_loop, args=(bot,)).start()