
import ttkthemes
from ttkthemes import THEMES
import tkinter
from tkinter import ttk
from tkinter import *
import cx_Freeze

root = Tk()
root.title('Student Record')
# configuring root width and height
__primary_color= '#282828'
width = 700
height = 400
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0, 0)
print(THEMES)
root.attributes('-alpha',0.876)
root.configure(background=__primary_color)
root.state('zoomed')
style = ttk.Style(root)
style.configure('tree.Treeview', background=__primary_color, foreground='#fff')
tree = ttk.Treeview(root,show='headings',height=15, columns=['first_name', 'Middle_name', 'Last_name','Phone', 'Gender'], style='tree.Treeview')




scrolbarY = ttk.Scrollbar(root,orient='vertical',command=tree.yview)
tree.configure(yscrollcommand=scrolbarY.set)
tree.heading('first_name',text='First Name', anchor='center')
tree.heading('Middle_name',text='Middle Name', anchor='center')
tree.heading('Last_name',text='Last Name', anchor='center')
tree.heading('Phone',text='Phone Number', anchor='center')
tree.heading('Gender',text='Gender', anchor='center')

tree.column('#1',anchor='center')
tree.column('#2',anchor='center')
tree.column('#3',anchor='center')
tree.column('#4',anchor='center')
tree.column('#5',anchor='center')


scrolbarY.grid(row=0, column=1,sticky='ns')
data = []
for dt in range(1,100):
    data.append([f'first Name {dt}', f'Middle Name {dt}', f'Last Name {dt}', f'Phone {dt}', f'Gender {dt}'])

for mydata in  data:
    tree.insert('',index=END,values=mydata)

scrolbarX = ttk.Scrollbar(root,orient='horizontal',command=tree.xview)
tree.configure(xscrollcommand=scrolbarX.set)
scrolbarX.grid(row=1, column=0, sticky='we')
tree.grid(row=0, column=0, sticky='nsew')
root.mainloop()