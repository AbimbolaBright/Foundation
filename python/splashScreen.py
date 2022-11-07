import tkinter
from tkinter import ttk 
from tkinter import *


root =Tk()
width = 400
height = 250
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
root.overrideredirect(True)
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0, 0)


btnCancel=ttk.Button(root, text='Click Me to Cancel')
btnCancel.grid(row=0, column=0,pady=20, ipady=5, ipadx=5)
btnCancel['command'] = root.destroy

#progressbar
pb = ttk.Progressbar(root,orient='horizontal',mode='determinate',value=80, length=300)
pb.grid(row=1, column=0, sticky='ew')
root.mainloop()