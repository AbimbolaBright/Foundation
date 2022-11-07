import code
import os
from re import search
import tkinter 
from tkinter import *
import pyttsx3
import os
 
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
                      
lblInfo.grid(row = 0, column = 0)
 
lblInfo = Label(Tops, font=('arial', 20, 'bold'),
             text = localtime, fg = "Steel Blue",
                           bd = 10, anchor = 'w')
                         
lblInfo.grid(row = 1, column = 0)
 
rand = StringVar()

key = StringVar()
Search = StringVar()
Amount = StringVar()
 
# exit function
def qExit():
    root.destroy()
 
# Function to reset the window
def Reset():
    rand.set("")
    
    key.set("")
    Search.set("")
    Amount.set("")
 
 
# reference
lblReference = Label(f1, font = ('arial', 16, 'bold'),
                text = " Company Name:", bd = 16, anchor = "w")
                 
lblReference.grid(row = 0, column = 0)
 
txtReference = Entry(f1, font = ('arial', 16, 'bold'),
               textvariable = rand, bd = 10, insertwidth = 4,
                        bg = "powder blue", justify = 'left')
                         
txtReference.grid(row = 0, column = 1)
 

 
lblkey = Label(f1, font = ('arial', 16, 'bold'),
            text = "Security key", bd = 16, anchor = "w" )
             
lblkey.grid(row = 2, column = 0)
 
txtkey = Entry(f1, font = ('arial', 16, 'bold'),
         textvariable = key, bd = 10, insertwidth = 4,
                bg = "powder blue", justify = 'left',show= '*')
                 
txtkey.grid(row = 2, column = 1)
 
lblmode = Label(f1, font = ('arial', 16, 'bold'),
          text = "Search(for drug you want)",bd = 16, anchor = "center")
                                
                                 
lblmode.grid(row = 3, column = 0)
 
txtmode = Entry(f1, font = ('arial', 16, 'bold'),
          textvariable = Search, bd = 10, insertwidth = 4,
                  bg = "white", justify = 'left')
                   
txtmode.grid(row = 3, column = 1)
 
lblService = Label(f1, font = ('arial', 16, 'bold'),
             text = " Amount-", bd = 16, anchor = "w")
              
lblService.grid(row = 2, column = 2)
 
txtService = Entry(f1, font = ('arial', 16, 'bold'),
             textvariable = Amount, bd = 10, insertwidth = 4,
                       bg = "powder blue", justify = 'left')
                        
txtService.grid(row = 2, column = 3)
 
#english
import base64
 

 
def Ref():
     print("Message= ", (Search.get()))

# Show message button
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
                        font = ('arial', 16, 'bold'), width = 10,
                       text = "Show Message", bg = "powder blue",
                         command = Ref).grid(row = 7, column = 1)
 
# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,
                  fg = "black", font = ('arial', 16, 'bold'),
                    width = 10, text = "Reset", bg = "green",
                   command = Reset).grid(row = 7, column = 2)
 
# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,
                 fg = "black", font = ('arial', 16, 'bold'),
                      width = 10, text = "Exit", bg = "red",
                  command = qExit).grid(row = 7, column = 3)
 
# keeps window alive
root.mainloop()