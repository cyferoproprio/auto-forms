import pyautogui
import time
import keyboard

time.sleep(5) 
while True:
  if keyboard.is_pressed('q'): 
        break
  pyautogui.write('Pedro', interval=0.1)
  pyautogui.press('tab')
  pyautogui.write('pedro@email.com', interval=0.1) 
  pyautogui.press('tab')
  pyautogui.write('123456789', interval=0.1)
  pyautogui.press('enter')
