import tkinter 
from tkinter import *

#initializing our window and other module
def save():
   
     username='root'
     pwd = ''
     dbname= 'python_db'
     host = 'localhost'
     
     message = 'Your record has been saved successfully!'


root = Tk()
root.title('Registration Login Form - Glimpse Solution')
width = 600
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width//2 -width//2
y = screen_height//2 - height//2

root.geometry(f'{width}x{height}+{x}+{y}')
#Label with  Entry form
lblfullname= Label(root, text="fullname:").grid(row=0, column=0)
lblemail= Label(root, text="email:").grid(row=1, column=0)
lblphone= Label(root, text="phone:").grid(row=2, column=0)
lblpassword= Label(root, text="password:").grid(row=3, column=0)

#Entry form

textfullname= Entry(root,font=('arial',24, 'bold')).grid(row=0, column=1,columnspan=4,ipady=7, sticky='WE')
textemail= Entry(root, font=('arial',24, 'bold')).grid(row=1, column=1,columnspan=4,ipady=7, sticky='WE')
textphone= Entry(root, font=('arial',24, 'bold')).grid(row=2, column=1,columnspan=4,ipady=7, sticky='WE')
textpassword= Entry(root, font=('arial',24, 'bold')).grid(row=3, column=1,columnspan=4,ipady=7, sticky='WE')



root.mainloop()
