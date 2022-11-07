
from importlib.metadata import EntryPoint
from tkinter import *
from turtle import width
from tkinter import messagebox as msg

expression=''

def equal():
    global expression
    answer = str(eval(expression))
    expression= answer
    display.set(expression)
    
def press(number):
    global expression
    expression= expression + str(number)
    display.set(expression)

def clear():
    display.set('')
    
def delete():
    global expression #12345
    text = str(expression) # '12345'
    lenght = len(text) -1 # 5-1 = 4
    answer = text[0:lenght] #text[0:4]
    expression =answer
    display.set(expression)
    
    
root = Tk()
root.title('calculator')
width= 700//2 #350
height =850//2 #400
screen_width= root.winfo_screenwidth()//2 - width
screen_height = root.winfo_screenheight()//2 - height
root.geometry(f'{width}x{height}+{screen_width}+{screen_height}')
#..............Frame.................................................
display=StringVar()
frmB = Frame(root,width=width, height=50, relief='flat', bd=4, bg='#282828')
txtDisplay = Entry(frmB,background='white', fg='black', width=300, font=('arial', 24, 'bold'), textvariable=display).pack(ipady=11)
frmB.pack(pady=(0,10))


frmA = Frame(root,width=width, relief='flat', bd=4, bg='#282828')
#..............Buttons...............................
btn9 = Button(frmA,bg='black', fg='white', font=('arial', 12, 'bold'), text='9', command=lambda: press(9)).grid(row=1, column=0, ipadx=10, ipady=10, pady=10)
btn8 = Button(frmA, bg='black', fg='white', font=('arial', 12, 'bold'), text='8',command=lambda: press(8)).grid(row=1, column=1, ipadx=10, ipady=10,  pady=10)
btn7 = Button(frmA,bg='black', fg='white', font=('arial', 12, 'bold'), text='7',command=lambda: press(7)).grid(row=1, column=2, ipadx=10, ipady=10, pady=10)
btn6 = Button(frmA,bg='black', fg='white', font=('arial', 12, 'bold'), text='6',command=lambda: press(6)).grid(row=1, column=3, ipadx=10, ipady=10, pady=10)
btnMult = Button(frmA,bg='white', fg='black', font=('arial', 12, 'bold'), text='x',command=lambda: press('*')).grid(row=1, column=4, ipadx=10, ipady=10, pady=10)

btn5 = Button(frmA,bg='black', fg='white', font=('arial', 12, 'bold'), text='5',command=lambda: press(5)).grid(row=2, column=0, ipadx=10, ipady=10)
btn4 = Button(frmA, bg='black', fg='white', font=('arial', 12, 'bold'), text='4',command=lambda: press(4)).grid(row=2, column=1, ipadx=10, ipady=10)
btn3 = Button(frmA,bg='black', fg='white', font=('arial', 12, 'bold'), text='3',command=lambda: press(3)).grid(row=2, column=2, ipadx=10, ipady=10)
btn2 = Button(frmA,bg='black', fg='white', font=('arial', 12, 'bold'), text='2',command=lambda: press(2)).grid(row=2, column=3, ipadx=10, ipady=10)
btnDiv = Button(frmA,bg='white', fg='black', font=('arial', 12, 'bold'), text='/',command=lambda:press('/')).grid(row=2, column=4, ipadx=10, ipady=10)

btn1 = Button(frmA,bg='black', fg='white', font=('arial', 12, 'bold'), text='1',command=lambda: press(1)).grid(row=3, column=0, ipadx=10, ipady=10, pady=10)
btn0 = Button(frmA, bg='black', fg='white', font=('arial', 12, 'bold'), text='0',command=lambda: press(0)).grid(row=3, column=1, ipadx=10, ipady=10,  pady=10)
btnDot = Button(frmA,bg='black', fg='white', font=('arial', 12, 'bold'), text='.', command=lambda: press('.')).grid(row=3, column=2, ipadx=10, ipady=10, pady=10)
btnC = Button(frmA,bg='black', fg='white', font=('arial', 12, 'bold'), text='C', command=clear).grid(row=3, column=3, ipadx=10, ipady=10, pady=10)
btnAdd = Button(frmA,bg='white', fg='black', font=('arial', 12, 'bold'), text='+',command=lambda: press('+')).grid(row=3, column=4, ipadx=10, ipady=10, pady=10)

btnDel = Button(frmA,bg='white', fg='black', font=('arial', 12, 'bold'), text='Del', command=delete).grid(row=4, column=0, ipadx=10, ipady=10, pady=10)
btnMplus = Button(frmA, bg='white', fg='black', font=('arial', 12, 'bold'), text='M+').grid(row=4, column=1, ipadx=10, ipady=10,  pady=10)
btnSub = Button(frmA,bg='white', fg='black', font=('arial', 12, 'bold'), text='-',command=lambda: press('-')).grid(row=4, column=2, ipadx=10, ipady=10, pady=10)
btnEqual = Button(frmA,bg='green', fg='white', font=('arial', 12, 'bold'), text='=',command=equal).grid(row=4, column=3,columnspan=2, sticky='WE', ipadx=10, ipady=10, pady=10)
frmA.place(relx=0.1, rely=0.2)
root.mainloop()



