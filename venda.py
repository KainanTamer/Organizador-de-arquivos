import pyautogui as py
import random
import time

time.sleep(5)

mensagem = ['CARALHOOOOO, FODAAAAA']


for i in range(50):
    msg = random.choice(mensagem)
    py.write(msg)
    py.press('Enter')
