from cProfile import label
import code
from distutils.cmd import Command
from logging import error
import os
import mysql.connector
from mysql.connector.errors import Error

import tkinter 
from tkinter import *
from tkinter import messagebox

 
# # import other necessary modules
# import random
# import time
# import datetime

 
 
# creating root object
root = Tk()
 
# defining size of window
root.geometry("1200x6000")
 
# setting up the title of window
root.title("Porter Register")
 
Tops = Frame(root, width = 1600, relief =SUNKEN)
Tops.pack(side = TOP)
 
f1 = Frame(root, width = 800, height = 700,
                            relief = SUNKEN)
f1.pack(side = LEFT)
 
 
lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'),


          text = "Student' Portal Registration Page .",
                     fg = "green", bd = 10, anchor='w')
                      
lblInfo.grid(row = 0, column = 0)

 
                         
lblInfo.grid(row = 1, column = 0)
 
Matricnumber = StringVar()

username = StringVar()
Othername = StringVar()
Email = StringVar()
Mobilenumber = StringVar()
Password = StringVar()
Stateoforigin = StringVar()

 
# Function to reset the window

def saved():

        username = 'root'
        pwd = ''
        dbname = 'victor_db'
        host = 'localhost'
    
        # con = mysql.connect(host=host,database=dbname, user=username, password=pwd)
        # cursor = con.cursor()
     
        sql = "INSERT INTO users(`Matricnumber`, `username`, ` Othername`, `Email`,`Mobilenumber`,`Password`,`Stateoforigin`) VALUES (%s, %s,%s,%s,%s,%s,%s)"
        value = (Matricnumber.get(),Othername.get(),Email.get(), Mobilenumber.get(),Password.get(),Stateoforigin.get())
        # cursor.execute(sql,value)
        # con.commit()
def Reset():
    Matricnumber.set("")
    
    username.set("")
    Othername.set("")
    Email.set("")
    Mobilenumber.set("")
    Password.set("")
    Stateoforigin.set("")

    message = 'Your record has been saved successfully!'
    messagebox.showinfo('Saving Record',message)
    
    messagebox.showerror('Database Error','The email used is already exist.')
   




 
 
# reference
lblReferen = Label(f1, font = ('arial', 16, 'bold'),
                text = "                                       ", bd = 16, anchor = "w")
                 
lblReferen.grid(row = 0, column = 0)

lblReference = Label(f1, font = ('arial', 16, 'bold'),
                text =  "Matric Number*", anchor = "w")
                 
lblReference.grid(row = 0, column = 1)
 
txtReference = Entry(f1, font = ('arial', 16, 'bold'),
               textvariable = Matricnumber ,bd=6, insertwidth = 4,
                        bg = "white", justify = 'left')
                         
txtReference.grid(row = 0, column = 2)
 

 
lblkey = Label(f1, font = ('arial', 16, 'bold'),
            text = "Username *", bd = 16, anchor = "w" )
             
lblkey.grid(row = 1, column = 1)
 
txtkey = Entry(f1, font = ('arial', 16, 'bold'),
         textvariable = username, bd = 6, insertwidth = 4,
                bg = "white", justify = 'left',)
                 
txtkey.grid(row = 1, column = 2)
 
lblmode = Label(f1, font = ('arial', 16, 'bold'),
          text = "Othername*",bd = 16, anchor = "center")
                                
                                 
lblmode.grid(row = 2, column = 1)
 
txtmode = Entry(f1, font = ('arial', 16, 'bold'),
          textvariable = Othername, bd = 6, insertwidth = 4,
                  bg = "white", justify = 'left')
                   
txtmode.grid(row = 2, column = 2)

lblmode = Label(f1, font = ('arial', 16, 'bold'),
          text = "Email*",bd = 16, anchor = "center")
                                
                                 
lblmode.grid(row = 3, column = 1)
 
txtmode = Entry(f1, font = ('arial', 16, 'bold'),
          textvariable = Email, bd = 6, insertwidth = 4,
                  bg = "white", justify = 'left')
                   
txtmode.grid(row = 3, column = 2)
 

lblmode = Label(f1, font = ('arial', 16, 'bold'),
          text = "Mobilenumber*",bd = 16, anchor = "center")
                                
                                 
lblmode.grid(row = 4, column = 1)
 
txtmode = Entry(f1, font = ('arial', 16, 'bold'),
          textvariable = Mobilenumber, bd = 6, insertwidth = 4,
                  bg = "white", justify = 'left')
                   
txtmode.grid(row = 4, column = 2)
 

lblmode = Label(f1, font = ('arial', 16, 'bold'),
          text = "State Of Origin*",bd = 16, anchor = "center")
                                
                                 
lblmode.grid(row = 5, column = 1)
 
txtmode = Entry(f1, font = ('arial', 16, 'bold'),
          textvariable = Stateoforigin, bd = 6, insertwidth = 4,
                  bg = "white", justify = 'left',)
                   
txtmode.grid(row = 5, column = 2)
 

lblmode = Label(f1, font = ('arial', 16, 'bold'),
          text = "Password*",bd = 16, anchor = "center")
                                
                                 
lblmode.grid(row = 6, column = 1)
 
txtmode = Entry(f1, font = ('arial', 16, 'bold'),
          textvariable = Password, bd = 6, insertwidth = 4,
                  bg = "white", justify = 'left',show= '*')
                   
txtmode.grid(row = 6, column = 2)







# Submit button
btnsubmit = Button( f1 ,padx=18,pady=10,bd=18,font=('Arial', 18, 'bold'),width = 10, text="Save Record",command=saved).grid(row = 7, column = 2)
    
 
# Reset button
btnReset = Button(f1, padx = 18, pady = 10, bd = 18,
                  fg = "black", font = ('arial', 16, 'bold'),
                    width = 10, text = "Reset", bg = "green",
                   command = Reset).grid(row = 7, column = 3)
 

# keeps window alive
root.mainloop()
 