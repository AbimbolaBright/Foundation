import tkinter
from tkinter import Button, Entry, Frame, Label, StringVar, Tk, messagebox
from tkinter import font
# import lib.mysql.connector as mysql
# from lib.mysql.connector.errors import Error
import mysql.connector
from mysql.connector.errors import Error



#initailizing our window and other form module

def saved():
   try:
        username = 'root'
        pwd = ''
        dbname = 'victor_db'
        host = 'localhost'
    
        con = mysql.connect(host=host,database=dbname, user=username, password=pwd)
        cursor = con.cursor()
     
        sql = "INSERT INTO users(`fullname`, `email`, `phone`, `password`) VALUES (%s, %s,%s,%s)"
        value = (fullname.get(),email.get(), phone.get(), password.get())
        cursor.execute(sql,value)
        con.commit()
        fullname.set('')
        email.set('')
        phone.set('')
        password.set('')
        message = 'Your record has been saved successfully!'
        messagebox.showinfo('Saving Record',message)
        
   except Error as err:
       messagebox.showerror('Database Error','The email used is already exist.')
   finally:
       con.close()




root = Tk()
root.title('Registration Form -  Glimpse Solution')
width= 600
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width//2 - width//2
y = screen_height//2 - height//2

root.geometry(f'{width}x{height}+{x}+{y}')

#Label with Entry form

lblfullname = Label(root,text="Fullname:", font=('Arial', 20, 'bold')).grid(row=0, column=0)
lblemail = Label(root,text="Email:", font=('Arial', 20, 'bold')).grid(row=1, column=0)
lblphone = Label(root,text="Phone No:",font=('Arial', 20, 'bold')).grid(row=2, column=0)
lblpassword = Label(root,text="Password:",font=('Arial', 20, 'bold')).grid(row=3, column=0)
fullname = StringVar()
email =StringVar()
phone = StringVar()
password = StringVar()
#Entry form
txtfullname = Entry(root, font=('Arial', 24, 'bold'), textvariable=fullname).grid(row=0, column=1, columnspan=4 , ipady=7,)
txtemail = Entry(root,font=('Arial', 24, 'bold'), textvariable=email).grid(row=1, column=1, columnspan=4 , ipady=7,)
txtphone = Entry(root,font=('Arial', 24, 'bold'), textvariable=phone).grid(row=2, column=1, columnspan=4 , ipady=7,)
txtpassword = Entry(root,font=('Arial', 24, 'bold'), show='x', textvariable=password).grid(row=3, column=1, columnspan=4 , ipady=7,)

btnsubmit = Button(root,font=('Arial', 18, 'bold'), text="Save Record", command=saved).grid(row=4, column=3, columnspan=4 ,pady=(15,0), ipady=6, sticky='EW')
root.mainloop()