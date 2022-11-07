#begins module import statement
import sys
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import re
from datetime import datetime
import os
#End of module statement

# initialize root element from TK
root = Tk()
root.title('Victor - Untitled')

#configuring root width and height

width = 800
height = 450
sw = root.winfo_screenwidth()
sh =root.winfo_screenheight()
x= sw//2 - width//2
y = sh//2 - height//2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0,0)

#setting icon to the root window
icon = PhotoImage(file='icons/note-48.png')
root.iconphoto(False,icon)

#adding menuBar to the root window
menuBar = Menu(root)
root.configure(menu=menuBar)

#addding scroltext to my rpoot window  
scroltext = ScrolledText(root, font=('Time new romans', 14))
scroltext.pack()
#adding menus to the menuBar window
fileMenu = Menu(menuBar, tearoff=0)

#initializing photoIcon 
newIcon = PhotoImage(file='icons/create_new-16.png')
openIcon = PhotoImage(file='icons/open_document-16.png')
newWindowIcon = PhotoImage(file='icons/windows8_tablet-16.png')
printIcon = PhotoImage(file='icons/print-16.png')
pagesetupIcon = PhotoImage(file='icons/page_overview_4-16.png')
exitIcon = PhotoImage(file='icons/exit-16.png')
saveIcon = PhotoImage(file='icons/save-16.png')
saveAsIcon = PhotoImage(file='icons/save_new-16.png')


#adding menu items to the file  Menu
fileMenu.add_command(label='New', accelerator='Ctrl + N', underline=0, image=newIcon, compound=LEFT)

fileMenu.add_command(label='New Window', accelerator='Ctrl + Shift + N', underline=4, compound=LEFT, image=newWindowIcon)
fileMenu.add_command(label='Open...', accelerator='Ctrl + O', underline=0, image=openIcon, compound=LEFT)
fileMenu.add_command(label='Save', accelerator='Ctrl + S', underline=0, image=saveIcon, compound=LEFT)
fileMenu.add_command(label='Save As...', accelerator='Ctrl + Shift + S', underline=5, compound=LEFT, image=saveAsIcon)
fileMenu.add_separator()
fileMenu.add_command(label='Page Setup...', underline=8, image=pagesetupIcon, compound=LEFT)
fileMenu.add_command(label='Print...', accelerator='Ctrl + P', underline=0, compound=LEFT, image=printIcon)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',compound=LEFT, image=exitIcon, underline=1,accelerator='Ctrl + Q', command=root.quit)
menuBar.add_cascade(label='File', compound=LEFT, underline=0, menu=fileMenu)

#binding event to the root
#adding menu items to the Edit  Menu
EditMenu = Menu(menuBar, tearoff=0)

EditMenu.add_command(label='undo', accelerator='Ctrl + Z', underline=0,compound=LEFT,state=DISABLED)
EditMenu.add_separator()
EditMenu.add_command(label='Cut', accelerator='Ctrl + X', underline=4, compound=LEFT,state=DISABLED )
EditMenu.add_command(label='Copy', accelerator='Ctrl + C', underline=0,  compound=LEFT,state=DISABLED)
EditMenu.add_command(label='Peste', accelerator='Ctrl + V', underline=0,  compound=LEFT)
EditMenu.add_command(label='Delete', accelerator='Ctrl + Del', underline=5, compound=LEFT,state=DISABLED)
EditMenu.add_separator()
EditMenu.add_command(label='Seacrh With Bing...',accelerator='Ctrl + E', underline=8 ,compound=LEFT)
EditMenu.add_command(label='Find...', accelerator='Ctrl + F', underline=0, compound=LEFT,state=DISABLED)

EditMenu.add_command(label='Find Next',compound=LEFT,  underline=1,accelerator='F3',state=DISABLED)
EditMenu.add_command(label='Replace...',compound=LEFT,  underline=1,accelerator='Ctrl + H', command=root.quit)
EditMenu.add_command(label='Go To...',compound=LEFT,  underline=1,accelerator='Ctrl + G', command=root.quit)
EditMenu.add_separator()
EditMenu.add_command(label='Select All',compound=LEFT,  underline=1,accelerator='Ctrl + A', command=root.quit)
EditMenu.add_command(label='Time/Date',compound=LEFT,  underline=1,accelerator='F5', command=root.quit)
menuBar.add_cascade(label='Edit', compound=LEFT, underline=1, menu=EditMenu)

#adding menu items to the Format  Menu
FormatMenu = Menu(menuBar, tearoff=0)
FormatMenu.add_command(label='Word Wrap',  underline=4, compound=LEFT, )
FormatMenu.add_command(label='Font...',  underline=0,  compound=LEFT)
menuBar.add_cascade(label='Format', compound=LEFT, underline=2, menu=FormatMenu)





#adding menu items to the View  Menu
ViewMenu = Menu(menuBar, tearoff=0)
zoommenu = Menu(ViewMenu, tearoff=0)
zoommenu.add_command(label="Zoom in", accelerator='Ctrl + Plus', underline = 5, compound= LEFT)
zoommenu.add_command(label="Zoom out", accelerator='Ctrl + Minus',underline = 5, compound= LEFT)
zoommenu.add_command(label="Restore Default Zoom", accelerator='Ctrl + O',underline = 0, compound= LEFT)
ViewMenu.add_cascade(label="Zoom", compound= LEFT, menu=zoommenu)

# ViewMenu.add_command(label='Zoom',  underline=4, compound=LEFT, )
ViewMenu.add_command(label='Status Bar',  underline=0,  compound=LEFT)
menuBar.add_cascade(label='View', compound=LEFT, underline=3, menu=ViewMenu)




#adding menu items to the Help  Menu
HelpMenu = Menu(menuBar, tearoff=0)
HelpMenu.add_command(label='View Help',  underline=4, compound=LEFT, )
HelpMenu.add_separator()
HelpMenu.add_command(label='About Notpad',  underline=0,  compound=LEFT)
menuBar.add_cascade(label='Help', compound=LEFT, underline=4, menu=HelpMenu)

    
root.bind_all('<Control-q>',quit)
  
def quit(event):
    sys.exit(0)

#compile and view notepad using mainloop
root.mainloop()
