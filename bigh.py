from time import strftime
from tkinter import *
import tkinter

def clock():
    time =strftime('%I:%M:%S %p')
    lblClock.config(text=time)
    lblClock.after(1000,clock)
    lblClock.pack(pady=20)

root = Tk()
root.geometry('400x100')
root.title('Digital Clock')
root.resizable(False,False)
#label into Root
lblClock = Label(root, fg='black',font=('arial',26,'bold'))
clock()
root.mainloop()