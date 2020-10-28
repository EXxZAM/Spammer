# PyAutoGui

# while True:
#     pyautogui.write('Hi')
#     pyautogui.press('enter', interval=int(1))


import pyautogui
import time
from tkinter import *

# Functions

def spam():
    time.sleep(5)
    i = 0
    while i < int(time_entry.get()):
        pyautogui.write(text_entry.get())
        pyautogui.press('enter', interval=int(1))
        i += 1



# Define the main window
root = Tk()
root.title('Spammer')
root.geometry('400x200')
root.config(bg='#121212')
# Making the widgets
text_entry = Entry(root, width=30)
time_entry = Entry(root, width=30)
confirm_btn = Button(root, text='Start Spam', bg='#121212', fg='white', borderwidth=3, command=spam)

# Griding
text_entry.grid(row=0,column=0,pady=10, padx=70)
time_entry.grid(row=1, column=0,pady=10, padx=70)
confirm_btn.grid(row=3, column=0,pady=10, padx=70)

# Calling the main window's mainloop
root.mainloop()