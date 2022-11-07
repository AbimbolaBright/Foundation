from _tkinter import*
from curses import *
from msilib.schema import RadioButton
from pydoc import text
from tkinter import Canvas, StringVar, Tk, Variable
#from tkinter.ttk import Frame
#from turtle import color
from typing_extensions import IntVar
import mysql.connector
from mysql.connector.errors import Error

class TrafficLight:
     def __init__(self):
        pass
        window =Tk()
        window.title("traffic Light")
        self.canvas = Canvas(window,width=450, height=300,bg="white")
        self.canvas.pack()
        Frame = Frame(window)
        Frame.pack
        self.v1 = IntVar()

        
        
        
        rd_Red = RadioButton(frametext="Red", bg="red",  
        variable= self.v1, value=1, 
        command=self.processRadiobutton)
        
        rd_Yellow= RadioButton(frametext ="Yellow",bg="yellow",
        variable= self.v1, value=2, 
        command=self.processRadiobutton)


        
        rd_Green =RadioButton(frametext="Green",bg="green",
        variable= self.v1, value=3, 
        command=self.processRadiobutton)

        rd_Red.grid(row= 10, column=1)
        rd_Yellow.grid(row= 10, column=2)
        rd_Green.grid(row= 10, column=3)
        
        
        
        
        
        window.mainloop()

        





     
        
    