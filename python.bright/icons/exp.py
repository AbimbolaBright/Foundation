# from cProfile import label
# from tkinter import Button, Entry, StringVar
from operator import inv
from tkinter import BOTH, W, Entry, Frame, StringVar, font
from tkinter.ttk import Button, Label

from tkinter.tix import Tk 
from functools import partial




#window 
ws = Tk()
ws.geometry('700x300')
ws.title(' office Expense')
amtvar= ()
f= ('Times new roman',14)

dopvar= StringVar()


f2=Frame(ws)

f2.pack

f1=Frame(
    ws,
    padx=10,
    pady=10,

)

f1.pack(expand=True,fill=BOTH)

Label(f1,text='ITEM NAME',
font=f).grid(row=0,column=0,sticky=W)
Label(f1,text='ITEM PRICE',
font=f).grid(row=1,column=0,sticky=W)
Label(f1,text='PURCHASE DATE',
font=f).grid(row=2,column=0,sticky=W)


item_name= Entry(f1,font=f)
item_nmt= Entry(f1,font=f, textvariable=amtvar)
transaction_date=Entry(f1,font=f,textvariable=dopvar)


item_name.grid(row=0,column=1,sticky='EW',padx=(10,0))
item_nmt.grid(row=1,column=1,sticky='EW',padx=(10,0))
transaction_date.grid(row=2,column=1,sticky='EW',padx=(10,0))


cur_date= Button(
    f1,
    text='Current Date',
    font=f,
    bg='#04C4D9',
    command=None,
    width=15,
)
submit_btn=Button(
    f1,
    text='Save Record',
    font=f,
    bg='#42602D',
    fg='white',


)



ws.mainloop()
