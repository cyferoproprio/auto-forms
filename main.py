import pyautogui
import time
import tkinter as tk
import threading
import keyboard

running = False #Loop dont auto starts

def start_autoforms():
    global running
    try:
      interval = float(entry_interval.get())
      if interval <= 0:
        label_status.config(text="Interval > 0")
        return
    except ValueError: 
        label_status.config(text="Invalid Value")
        return

    running = True
    label_status.config(text="Running")
       
    def running_form():
        while running:
             time.sleep(interval)
             pyautogui.write('Pedro', interval = 0.1)
             pyautogui.press('tab')
             pyautogui.write('pedro@gmail.com', interval=0.1)
             pyautogui.press('tab')
             pyautogui.write('082527', interval=0.1)
             pyautogui.press('enter')
             
             label_status.config(text="Stoped")
            
      
    threading.Thread(target=running_form).start()

def stop_autoforms():
    global running
    if keyboard.is_pressed('shift'):
     running = False       

#Main window
root = tk.Tk()
root.title("Auto Forms - Vgermann")
root.geometry("300x180")

tk.Label(root,text="writing speed: ").pack(pady=5)
entry_interval = tk.Entry(root)
entry_interval.pack()

#bottons 
tk.Button(root, text="Start", command=start_autoforms).pack(pady=5)
tk.Button(root, text="Stop", command=stop_autoforms).pack(pady=5)

#status label
label_status = tk.Label(root, text = "Stoped")
label_status.pack(pady=5)
root.mainloop()


