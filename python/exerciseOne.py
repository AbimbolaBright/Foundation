from tkinter import *
from tkinter import ttk
from tkinter import font
import mysql.connector as mysql
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import re
root = Tk()
root.title('Exercise One')



# configuring root width and height

width = 600
height = 350
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0, 0)
#Icons
LoginIcon = PhotoImage(file='./icons/select_users_30px.png')
RegisterIcon = PhotoImage(file='./icons/select_users_30px.png')
saveIcon = PhotoImage(file='./icons/save-16.png')
notebook = ttk.Notebook(root)
notebook.pack(pady=5,expand=True)
frm1 = ttk.Frame(notebook, width=600, height=250)
frm1.pack(ipadx=5, fill=BOTH, expand=True)
frm2 = ttk.Frame(notebook, width=600, height=250)
frm2.pack(ipadx=5, fill=BOTH, expand=True)
frm3 = ttk.Frame(notebook, width=400, height=250)
frm3.pack(ipadx=5, fill=BOTH, expand=True)
notebook.add(frm1, text='Register', image=LoginIcon, compound=LEFT)
notebook.add(frm2, text='Login', image=RegisterIcon,compound=LEFT)
notebook.add(frm3, text='Save Record', image=saveIcon,compound=LEFT)



btnLogin = ttk.Button(frm1, text='Login >>')
btnLogin.pack(ipady=5, ipadx=5, pady=10)
root.mainloop()