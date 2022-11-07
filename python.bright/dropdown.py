# import module

from cProfile import label
from pydoc import text
from optparse import Option
from ssl import Options
from tkinter import*
#create object
root=Tk()
#Adjust size
root. geometry("200x200")
root.title("Porter Register")
 
Tops = Frame(root, width = 1600, relief =SUNKEN)
Tops.pack(side = TOP)
 
f1 = Frame(root, width = 800, height = 700,
                            relief = SUNKEN)
f1.pack(side = LEFT)
 
 
#change the label text
def show ():
     label. config(text =clicked.get())

    #Dropdown menu option
Option = [
        "Monday"
        "Tuesday"
        "Wednesday"
        "thursday"
        "Friday"
        "Saturday"
        "Sunday"
    ]

    # datatype of  menun text
clicked= StringVar()
    #initial menu text

clicked.set("Monday")
    #create Dropdown menu
drop = OptionMenu(root, clicked,*Options)
drop .pack()

    #create button, it will change label text
button=  Button(root,text="clink me", command = show ).pack()
    # create label
label=Label(root,text ="")
label.pack()
    #Execute tkinter
root.mainloop



