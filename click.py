#you need to install pyautogui like this:
#py.exe -m pip install pyautogui
#then...
import pyautogui,time
while True:
    print("click")
    pyautogui.click(300,300)
    time.sleep(15 )
    #sleep(60 - time() % 60)