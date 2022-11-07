from cProfile import label
from tkinter import Button, Entry, StringVar
from tkinter.ttk import Label

from tkinter.tix import Tk 
from functools import partial

# def validateLogin(username, password):
#     print("username  entered:",username.get())
#     print("password entered:",password.get())
#     return


#window 
tkwindow = Tk()
tkwindow.geometry('700x300')
tkwindow.title(' Login  Form')
# #usernameLabel and text entry box
# usernameLabel = Label(tkwindow,font=('Arial', 18, 'bold'),text="User Name").grid(row=0, column=0)
# username =StringVar()
# usernameEntry= Entry(tkwindow,textvariable=username).grid(row=1, column=0)
# #password label and password entry box
# PasswordLabel = Label(tkwindow,font=('Arial', 18, 'bold'),text="Password").grid(row=2, column=0)
# password =StringVar()
# passwordEntry=Entry(tkwindow, font=('Arial', 18, 'bold'),textvariable=password, show='*').grid(row=3, column=0)
# validateLogin = partial(validateLogin, username,password)
# #login button
# loginbutton = Button(tkwindow,font=('Arial', 18, 'bold'),text="Login",command=validateLogin).grid(row=4, column=3, columnspan=4 ,pady=(15,0), ipady=6, sticky='EW')

tkwindow.mainloop()
