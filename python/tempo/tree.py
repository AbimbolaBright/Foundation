from random import sample
from tkinter import *
from tkinter import ttk
import mysql



root = Tk()
root.title('TreeView')


# configuring root width and height

width = 850
height = 350
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0, 0)
#Icons Library
fnameIcon = PhotoImage(file='./icons/select_users_30px.png') 

tree = ttk.Treeview(root,columns=['Firstname', 'Middlename', 'Lastname', 'Gender'],show='headings', height=30)

tree.heading('Firstname',text='First Name',anchor='center',image=fnameIcon)

tree.column('#1',stretch=False,anchor='center')
tree.column('#2',stretch=False,anchor='center')
tree.column('#3',stretch=False,anchor='center')
tree.column('#4',stretch=False,anchor='center')

tree.heading('Middlename',text='Middle Name',anchor='center',image=fnameIcon)
tree.heading('Lastname',image=fnameIcon,text='Last Name',anchor='center')
tree.heading('Gender',text='Gender',anchor='center')

samples = []
for n in range(1,51):
    samples.append((f'Firstname {n}', f'Middlename {n}', f'Lastname {n}',f'Gender {n}'))

for sample in samples:
    tree.insert('',END,values=sample)

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

    
tree.grid(row=0, column=0, stick='nsew')

root.mainloop()