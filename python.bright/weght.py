from genericpath import isfile
import numpy as np
import datetime
import os,sys

currentDT=datetime.datetime.now().date()
daily_array=[]

filename="My_weight_gain.txt"
if os.path.isfile(filename):
    print("\n file exists\n appending with provided data...")
else:
    print(" \n file does not exists \n creating{}".format(filename))
    #create a new file
    with open('Hello.txt','w')as file:
        file.write("Hello World")
        if os.path.isfile(filename):
            print("\n file exists\n appending with provided data...")
with open(filename,"a")as file:
    file.write("{:>20}{:>20}\n".format(str(currentDT),))

print("\n file does not exists \n creating{}".format(filename))
with open(filename,"w")as file:
    file.write("{:>20}{:>20}\n".format("Time","Mass(kg)"))
    file.write("{:>20}{:>10}\n".format(str(currentDT),))
def div(x,y):
    resuit=x/y 
    return 
div(5,6)
div(5,0)
def div (x,y):
    try:
        result=x/y
    except:
        print('Division by zero is dot allowed! Exiting...')
        result = None
        return result
    








