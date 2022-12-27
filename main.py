import pyautogui
import time

time.sleep(3)
count = 1

while count>0:
    pyautogui.typewrite("Welcome to WhatsApp SMS Bomber, made by Arkya "+str(count))
    pyautogui.press("enter")
    count = count + 1

