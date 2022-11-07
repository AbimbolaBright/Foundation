
import sys
from tkinter import *
from tkinter import ttk
from tkinter import font as ft, filedialog as fd
from tkinter import messagebox
import tkinter
from tkinter.scrolledtext import ScrolledText
import re
from datetime import datetime
import os
from turtle import undo
import webbrowser
from PIL import ImageTk

def find_file(value):
        f = str(value)
        print(f)
frmFind = Tk()
frmFind.title('Find and Replace')
width = 350
height = 150
sw = frmFind.winfo_screenwidth()
sh = frmFind.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
frmFind.geometry(f'{width}x{height}+{x}+{y}')
frmFind.resizable(0, 0)

#creatinf frames
notebook = ttk.Notebook(frmFind)
notebook.pack(side='top', fill='both') 

frame1 = ttk.Frame(notebook)
frame1.pack(fill='both',side='top' , expand=True)
frame2 = ttk.Frame(notebook)
frame2.pack(fill='both',side='top',expand=True)

notebook.add(frame1, text='Find Word')
notebook.add(frame2, text='Find & Replace')

#creating widget fro find function
findText= StringVar()
lblfind = ttk.Label(frame1,text='Find What:')
lblfind.pack(side='left', pady=20, padx=5)
txtfind = ttk.Entry(frame1, textvariable=findText)
txtfind.pack(side='left',pady=20, padx=5, fill=X, expand=True)

btnFind = ttk.Button(frame1, text='Find', command=lambda: find_file(findText.get()))
btnFind.pack(side='bottom', fill=X, pady=5, padx=5, expand=True)

#replace widget
lblfind2 = ttk.Label(frame2,text='Find What:')
lblfind2.grid(row=0, column=0, pady=20, padx=5)
txtfind2 = ttk.Entry(frame2)
txtfind2.grid(row=0, column=1, columnspan=2,pady=20, padx=5, sticky='ew')

lblreplace = ttk.Label(frame2,text='Replace with:')
lblreplace.grid(row=1, column=0, pady=5, padx=5)
txtreplace = ttk.Entry(frame2)
txtreplace.grid(row=1, column=1,columnspan=2,pady=5, padx=5,sticky='ew')

btnFindreplace = ttk.Button(frame2, text='Find & Replace')
btnFindreplace.grid(row=2, column=1, columnspan=2, pady=5, padx=5, )

    
frmFind.mainloop()