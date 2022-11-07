from cProfile import label
from tkinter import Button, Entry, StringVar
from tkinter.ttk import Label

from tkinter.tix import Tk 
from functools import partial

def validateLogin(username, password):
    print("username  entered:",username.get())
    print("password entered:",password.get())
    return


#window 
tkwindow = Tk()
tkwindow.geometry('400x150')
tkwindow.title(' Login  Form')
#usernameLabel and text entry box
usernameLabel = Label(tkwindow,text="User Name").grid(row=0,column=0)
username =StringVar()
usernameEntry= Entry(tkwindow,textvariable=username).grid(row=0,column=1)
#password label and password entry box
PasswordLabel = Label(tkwindow,text="Password").grid(row=1,column=0)
password =StringVar()
passwordEntry=Entry(tkwindow, textvariable=password, show='*').grid(row=1,column=1)
validateLogin = partial(validateLogin, username,password)
#login button
loginbutton = Button(tkwindow,text="Login",command=validateLogin).grid(row=4,column=0)

tkwindow.mainloop()
