import code
from cgitb import reset
import os
from re import search
import tkinter 
from tkinter import *
import pyttsx3
from tkinter import Button, Entry, Frame, Label, StringVar, Tk, messagebox
import os
import mysql.connector as mysql
from mysql.connector.errors import Error
 
# import other necessary modules
import random
import time
import datetime
# create object and assign voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.say('Hello customer how are you doing !!')
 # changing index changes voices but only
# 0 and 1 are working here
engine.setProperty('voice', voices[0].id)
engine.runAndWait()
print("")
print("")
 
 
# creating root object
root = Tk()
 
# defining size of window
root.geometry("1200x6000")
 
# setting up the title of window
root.title("pharmacy")
 
Tops = Frame(root, width = 1600, relief =SUNKEN)
Tops.pack(side = TOP)
 
f1 = Frame(root, width = 800, height = 700,
                            relief = SUNKEN)
f1.pack(side = LEFT)
 
# ==============================================
#                  TIME
# ==============================================
localtime = time.asctime(time.localtime(time.time()))
 
lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'),


 text = "Welcome to our pharmacy .",
 fg = "Black", bd = 10, anchor='w')
def login():
    try:    
        username = 'root'
        pwd = ''
        dbname = 'python_db'
        host = 'localhost'
    
        con = mysql.connect(host=host, database=dbname, user=username, password=pwd,phonenumber=phonenumber)
        cursor = con.cursor()
        sql = "SELECT * FROM users WHERE email=%s AND password=%s AND phonenumber=%s"
        cursor.execute(sql,(email.get(), password.get(),phonenumber.get(),))
        result=  cursor.fetchone()
        if(result== None):
           messagebox.showinfo('Login Error', 'Email or Password is INVALID')
        else:
            messagebox.showinfo('Login Success', 'Your login is successful.')
            
            root.destroy()
            mainForm()
    except Error as ex:
        messagebox.showerror('Error', ex.msg)
        def reset():
            
            phonenumber.set("")
            email.set("")
            password.set("")
            username.set

def mainForm():
    main = Tk()
    main.title('Dashboard-  Glimpse Solution')
    width= 800
    height = 700
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    x = screen_width/2 - width/2
    y = screen_height/2 - height/2
    main.geometry(f'{width}x{height}+{x}+{y}')
    main.mainloop()

    
        
      
    
    
    
    
root = Tk()
root.title('Login Form -  Glimpse Solution')
width= 800
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width//2 - width//2
y = screen_height//2 - height//2

root.geometry(f'{width}x{height}+{x}+{y}')

#Label with Entry form

lblusername= Label(root,text="username:",font=('Arial',20,'bold')).grid(row=0,column=0)
lblpheno= Label(root,text="phonenumber:", font=('Arial',20,'bold')).grid(row=1,column=0)
lblemail = Label(root,text="Email:", font=('Arial', 20, 'bold')).grid(row=2, column=0)
lblpassword = Label(root,text="Password:",font=('Arial', 20, 'bold')).grid(row=3, column=0)
username=StringVar()
email =StringVar()
phonenumber=StringVar()
password = StringVar()

#Entry form
textusername= Entry(root,font=('Arial',24,'bold'),textvariable=username).grid(row=0 ,column=1,columnspan=4,ipady=7,sticky='WE')
textphonenumber= Entry(root,font=('Arial',24,'bold'),textvariable=phonenumber).grid(row=1,column=1,columnspan=4,ipady=7,sticky='WE')

txtemail = Entry(root,font=('Arial', 24, 'bold'), textvariable=email).grid(row=2, column=1, columnspan=4 , ipady=7,sticky='WE')
txtpassword = Entry(root,font=('Arial', 24, 'bold'), show='x', textvariable=password).grid(row=3, column=1, columnspan=4 , ipady=7,sticky='WE')

btnsubmit = Button(root,font=('Arial', 18, 'bold'), text="Login", command=login).grid(row=4, column=3, columnspan=6 ,pady=(17,0), ipady=12, sticky='E')

# Reset button
btnReset = Button(root, font =('Arial',18,'bold'), text="Reset", bg = "green",
                   command=reset).grid(row = 4, column = 3,columnspan=6 ,pady=(12,0), ipady=8,sticky='w') 

                  
root.mainloop()
