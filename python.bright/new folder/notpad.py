from logging import root
from tkinter import*
from tkinter.scrolledtext import ScrolledText
import re
from datetime import datetime
import os
from turtle import width
# end of module statement

# initialize root element from tk
root= Tk()
root.title('Tempopad - Untitled')
width= 600
height= 400

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw//2- width//2
y= sh//2- height//2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0,0)

root.mainloop()