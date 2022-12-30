import pyautogui
import time
import pywhatkit as pyw


i=0
time.sleep(3)
count = 1

def bomb():
    pyautogui.typewrite("Welcome to WhatsApp SMS Bomber, made by Arkya ")
    pyautogui.press("enter")

def auto_msg():
    pyw.sendwhatmsg('Target-Phone-Number',' ',Hour,Minute)   # Please Replace the 'Target-Phone-Number','Hour', 'Minute' as you required
    while count>0:
        bomb()
while i<10:
    auto_msg()
