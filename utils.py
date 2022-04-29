from sympy import root
import settings
import subprocess
from tkinter import Button

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

def height_prc(percentage):
    return (settings.HEIGHT / 100) * percentage

def width_prc(percentage):
    return (settings.WIDTH / 100) * percentage

def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])

def create_restart_btn(location):
    restart_btn = Button(location, text= "Restart", width=15, height=2)
    restart_btn.place(
    x=width_prc(47),
    y=40
    )
    return restart_btn


# Example uses:
#notify("Title", "Heres an alert")
#print(height_prc(25))