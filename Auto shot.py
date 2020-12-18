import pyautogui
import time
a=0
while True:
    time.sleep(3)
    a=a+1
    n2=str(a)
    n=".png"
    name=n2+n
    pyautogui.screenshot(name)
    
