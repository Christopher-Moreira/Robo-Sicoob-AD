import pyautogui
import time


try: 
    while True:
        x, y = pyautogui.position ()
        print(f'Pos: X = {x}, Y = {y}' )

        time.sleep (3)

except KeyboardInterrupt:
    print("\n interrompido")

