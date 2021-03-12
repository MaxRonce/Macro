import pyautogui as pg
import keyboard
import time

while True :
    try :
        if keyboard.is_pressed('F3'):
            print("noir")
            pg.click(2700, 100)
            time.sleep(0.2)
        if keyboard.is_pressed('F6'):
            print("bleu")
            pg.click(2800, 100)
            time.sleep(0.2)
        if keyboard.is_pressed('F9'):
            print("rouge")
            pg.click(2750, 100)
            time.sleep(0.2)
        if keyboard.is_pressed('shift + F1'):
            print('gomme')
            pg.click(2630, 113)
            time.sleep(0.2)
        if keyboard.is_pressed('Pause'):
            break



    except :
        break

# noir = 2700 150
# bleu = 2800 150
# rouge = 1750 150
# gomme = 2630 113