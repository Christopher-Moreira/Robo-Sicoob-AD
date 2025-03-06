import pyautogui
import time




try:
    while True:
        pyautogui.moveTo(54, 102)
        pyautogui.click()

        time.sleep(3)

except KeyboardInterrupt:
    print("interrompido")
