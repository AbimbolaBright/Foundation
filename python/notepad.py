# begins module import statement
import sys
from tkinter import *
from tkinter import ttk
from tkinter import font as ft, filedialog as fd
from tkinter import messagebox
import tkinter
from tkinter.scrolledtext import ScrolledText
import re
from datetime import datetime
import os
from googlesearch import search
from turtle import undo
import webbrowser
from PIL import ImageTk


# End of module statement
# variable Declaration
statusBar_Flag=True
text_changed= False
url=''
# Function for Tolevel Design for Help Button
start_pos =1.0
prev_pos = 1.0

def search_google():
   mysearch= search('Who is Google',tld='com',num=5,stop=5, lang='en',country='Nigeria')
   for result in mysearch:
        webbrowser.open_new(result)
search_google()
def find_func(event=None):
    def find_next_file(value):
        global start_pos, prev_pos
        f = str(value)
        scroltext.tag_remove('found',1.0, END)
        if f:
            start_pos
            start_pos = scroltext.search(f,start_pos,END)
            if(not start_pos):
                return
            end_pos= f'{start_pos}+ {len(f)}c'
            scroltext.tag_add('found',start_pos,end_pos)
            start_pos=end_pos
            scroltext.tag_configure('found',background='blue', foreground='white')
                
    def find_file(value):
        global start_pos, prev_pos
        f = str(value)
        scroltext.tag_remove('found',1.0, END)
        if f:
            start_pos = scroltext.search(f,start_pos,END)
            if(not start_pos):
                return
            end_pos= f'{start_pos}+ {len(f)}c'
            scroltext.tag_add('found',start_pos,end_pos)
            start_pos=end_pos
            scroltext.tag_configure('found',background='blue', foreground='white')
   
    def find_Prev_file(value):
        pass           
    def replace_All():
        f= txtFind.get()
        r= txtReplace.get()
        content = scroltext.get(1.0, END)
        scroltext.delete('1.0', END)
        newcontent =content.replace(f,r)
        scroltext.insert(1.0,newcontent)

    def replace_singular():
          f = txtFind.get()
          r=txtReplace.get()
          scroltext.tag_remove('found',1.0, END)
          if f:
            start_pos = 1.0
            while True:
                start_pos = scroltext.search(f,start_pos,END)
                print(start_pos)
                if(not start_pos):
                    break
                end_pos= f'{start_pos}+ {len(f)}c'
                scroltext.delete(start_pos,end_pos)
                scroltext.insert(start_pos,r)
    frmFind = Toplevel(root)
    frmFind.title('Find and Replace')
    width = 350
    height = 150
    sw = frmFind.winfo_screenwidth()
    sh = frmFind.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    frmFind.geometry(f'{width}x{height}+{x}+{y}')
    frmFind.resizable(0, 0)
    
    #creatinf frames
    notebook = ttk.Notebook(frmFind)
    notebook.pack(side='top', fill='both') 
    
    frame1 = ttk.Frame(notebook)
    frame1.pack(fill='both',side='top' , expand=True)
    frame2 = ttk.Frame(notebook)
    frame2.pack(fill='both',side='top',expand=True)
    
    notebook.add(frame1, text='Find Word')
    notebook.add(frame2, text='Find & Replace')
    
    #creating widget fro find function
    findText= StringVar()
    lblframe1 = Frame(frame1)
    lblframe1.pack(pady=2, side='top')
    lblfind = ttk.Label(lblframe1,text='Find What:')
    lblfind.pack( pady=5, padx=5)
    txtfind = ttk.Entry(lblframe1, textvariable=findText)
    txtfind.pack(padx=5, fill=X, expand=True)
    
    lblframe = Frame(frame1)
    lblframe.pack(pady=5, side='top')
    btnFindPrev = ttk.Button(lblframe, text='Find Prev', command=lambda: find_Prev_file(findText.get()))
    btnFindPrev.pack(side='left',  pady=5, padx=5, expand=True)
    
    btnFind = ttk.Button(lblframe, text='Find', command=lambda: find_file(findText.get()))
    btnFind.pack(side='left', pady=5, padx=5, expand=True)
    
    btnFindNext = ttk.Button(lblframe, text='Find Next', command=lambda: find_next_file(findText.get()))
    btnFindNext.pack(side='left',  pady=5, padx=5, expand=True)
    
    #replace widget
    txtFind=StringVar()
    lblfind2 = ttk.Label(frame2,text='Find What:')
    lblfind2.grid(row=0, column=0, pady=20, padx=5)
    txtfind2 = ttk.Entry(frame2, textvariable=txtFind)
    txtfind2.grid(row=0, column=1, columnspan=2,pady=20, padx=5, sticky='ew')
    
    txtReplace=StringVar()
    lblreplace = ttk.Label(frame2,text='Replace with:')
    lblreplace.grid(row=1, column=0, pady=5, padx=5)
    txtreplace = ttk.Entry(frame2,textvariable=txtReplace)
    txtreplace.grid(row=1, column=1,columnspan=2,pady=5, padx=5,sticky='ew')
    
    btnFindreplace = ttk.Button(frame2, text='Find & Replace', command=replace_singular)
    btnFindreplace.grid(row=2, column=1, columnspan=2, pady=5, padx=5 )

    
    frmFind.mainloop()
    

#definition  function for NotePad
def new_file():
    global url
    url= ''
    scroltext.delete('1.0',END)

def open_file(event=None):
    global url
    url = fd.askopenfilename(initialdir=os.getcwd(), title='Select your Text Document',
                             filetypes=(('All Text(*.*)', '*.*'),('TempoPad(.txt)','*.txt')))
    try:
        with open(url, 'r') as f:
            scroltext.delete('1.0', END)
            scroltext.insert('1.0',f.read())
            root.title(os.path.basename(url + ' - Tempopad'))
    except FileNotFoundError:
        return
    except:
        return

def save_file(event=None):
    global url
    try:
        if(url):
            content = str(scroltext.get('1.0', END))
            with open(url,'w', encoding='utf-8') as f:
                f.write(content)
        else:
         save_as_file()
         root.title(os.path.basename(url + ' - Tempopad'))
    except FileNotFoundError:
        return
    except:
        return

def save_as_file(event=None):
    global url
    url = fd.asksaveasfilename(initialdir=os.getcwd(), title='Save your Document',
                           filetypes=(('All files(*.*)', '*.*'), ('Text files(*.txt)', '*.txt')),
                           defaultextension='.txt')
    content = str(scroltext.get('1.0', END))
    with open(url,'w') as f:
        f.write(content)
    root.title(os.path.basename(url + ' - Tempopad'))

#Exit App Function
def exit_file():
    fb = messagebox.askyesno('Exit Tempopad', 'Do you want to exit?')
    if(fb):
        sys.exit(0)
    else:
        return

#Undo Function
def undo_file():
    scroltext.event_generate('<<Undo>>')
    
#Redo Function
def redo_file():
    scroltext.event_generate('<<Redo>>')
#Copy Function 
def copy_file():
    scroltext.event_generate('<<Copy>>')
#Paste Function 
def paste_file():
    scroltext.event_generate('<<Paste>>')
#Cut Function 
def cut_file():
    scroltext.event_generate('<<Cut>>')
#Select Delete Function 
def delete_file():
    scroltext.delete(1.0,END)
    scroltext.focus()
#Send Feedback Function 
def send_feedback():
    answer = messagebox.askyesno('Send Feedback','Do you like our project?')
    if(answer):
        fb = messagebox.askyesno('Send Feedback', 'Do you want to rate us?')
        if(fb):
            urls= 'https://facebook.com/tempodigitalculture'
            webbrowser.open_new(urls)
        else:
            return
    else:
        return

#Date and Time function 
def timeDate():
    dateString=datetime.today()
    today = datetime.strftime(dateString,'%d-%B-%Y %I:%M:%S %p')
    print(today)
    messagebox.showinfo("Today's Date",today)

#Font size and font-family variables
current_font_size = 12
current_font_family = 'Arial'
#Font Size Function 
def font_size_file(evt=None):
    global current_font_size, current_font_family
    current_font_size= fontSize.get()
    scroltext.config(font=(current_font_family,current_font_size))
    
#Font Family Function 
def font_family_file(e=None):
    global current_font_size, current_font_family
    current_font_family = fontBox.get()
    scroltext.config(font=(current_font_family, current_font_size))

#Event function for Text Changed
def change_text_file(evt=None):
    global text_changed
    if(scroltext.edit_modified()):
        text_changed = True
        char_lenght = len(scroltext.get(1.0,'end-1c'))
        word_lenght = len(scroltext.get(1.0, 'end-1c').split())
        lblChar.config(text='Col: ' + str(char_lenght))
        lblLine.config(text='Word: ' + str(word_lenght))
        scroltext.edit_modified(False)
        
#Function for Bold Text 
def bold_file():
    text_prop = ft.Font(scroltext,scroltext.cget('font'))
    text_prop.configure(weight='bold')
    current_tags = scroltext.tag_names('sel.first')
    scroltext.tag_configure('bold',font=text_prop)
    if 'bold' in current_tags:
        scroltext.tag_remove('bold','sel.first','sel.last')
    else:
        scroltext.tag_add('bold','sel.first', 'sel.last')
        
#Italic Function 
def italic_file():
    text_prop = ft.Font(scroltext,scroltext.cget('font'))
    text_prop.configure(slant='italic')
    current_tags = scroltext.tag_names('sel.first')
    scroltext.tag_configure('italic',font=text_prop)
    if 'italic' in current_tags:
        scroltext.tag_remove('italic','sel.first','sel.last')
    else:
        scroltext.tag_add('italic','sel.first', 'sel.last')


#Underline Function for File 
def underline_file():
    text_prop = ft.Font(scroltext,scroltext.cget('font'))
    text_prop.configure(underline=True)
    current_tags = scroltext.tag_names('sel.first')
    scroltext.tag_configure('underline',font=text_prop)
    if 'underline' in current_tags:
        scroltext.tag_remove('underline','sel.first','sel.last')
    else:
        scroltext.tag_add('underline','sel.first', 'sel.last')
                       
#function for Alignment 
def left_align_file():
    text_content = scroltext.get(1.0, END)
    scroltext.delete('1.0', END)
    scroltext.tag_config('left',justify=LEFT)
    scroltext.insert(1.0,text_content, 'left')

def right_align_file():
    text_content = scroltext.get(1.0, END)
    scroltext.delete('1.0', END)
    scroltext.tag_config('right',justify=RIGHT)
    scroltext.insert(1.0,text_content,'right')
 
def center_align_file():
    text_content = scroltext.get(1.0, END)
    scroltext.delete('1.0', END)
    scroltext.tag_config('center',justify=CENTER)
    scroltext.insert(1.0,text_content,'center')

    
def zoom_in_file():
    global current_font_size, current_font_family
    current_font_size +=2
    scroltext.configure(font=(current_font_family, current_font_size)) 

def zoom_out_file():
    global current_font_size, current_font_family
    if(current_font_size <=8):
        return
    current_font_size -=2
    scroltext.configure(font=(current_font_family, current_font_size)) 

def zoom_default_file():
    global current_font_size, current_font_family
    current_font_size =12
    scroltext.configure(font=(current_font_family, current_font_size)) 

def selectAll_file():
    scroltext.event_generate('<<SelectAll>>')
#End of function for NotePad


def aboutHelp():
    aboutTk = Toplevel(root)
    aboutTk.transient(root)
    aboutTk.grab_set()
    aboutTk.title('About TempoPad')
    width = 400
    height = 300
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    aboutTk.geometry(f'{width}x{height}+{x}+{y}')
    aboutTk.resizable(0, 0)
    aboutTk.wm_iconbitmap('./icons8_notepad.ico')
    lblAbout = ttk.Label(aboutTk, text='About TempoPad', font=('arial', 20, 'bold'))
    lblAbout.pack(pady=10)
    message = 'This application is developed by Python Developer Team under JayTee Foundation. It is well-known that ' \
              'this app act as a guideline for young developer who wish to join the winning team for developing ' \
              'different application for mankind. This application for for personal use only. Any alteration or ' \
              'decompiling of this software is highly prohibited. Thanks. '
    lblTextAbout = ttk.Label(aboutTk, text=message, font=('arial', 12), wraplength=300, justify=CENTER)
    lblTextAbout.pack(pady=5)
    aboutTk.mainloop()

def hide_statusBar():
    global statusBar_Flag
    if(statusBar_Flag):
        statusBar.pack_forget()
        statusBar_Flag=False

    else:
        scroltext.pack_forget()
        statusBar.pack(side=BOTTOM)
        statusBar_Flag=True
        scroltext.pack(side=TOP)


# initialize root element from TK
root = Tk()
root.title('Untitled - Tempopad')
root.protocol('WM_DELETE_WINDOW',exit_file)
# configuring root width and height
width = 900
height = 550
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0, 0)

# setting icon to the root window
icon = PhotoImage(file='./icons/icons8_notepad_48.png')
root.iconphoto(False, icon)
# adding menuBar to the root window
menuBar = Menu(root)
root.configure(menu=menuBar)

# Tool Bar Menu
toolBar = ttk.Label(root)
toolBar.pack(side=TOP, fill=X, expand=True)

# adding status bar element to the notepad
lblstatusBar= StringVar()

statusBar = Label(root, textvariable=lblstatusBar)
statusBar.pack(side=BOTTOM, fill=X, expand=TRUE)
lblstatusBar.set(True)
# addding scroltext to my rpoot window
text_editor= StringVar()
scroltext = ScrolledText(root, font=('Time new romans', 14),undo=True)
scroltext.pack(side=TOP, fill=X)

# adding menus to the menuBar window
fileMenu = Menu(menuBar, tearoff=0)
editMenu = Menu(menuBar, tearoff=0)
formatMenu = Menu(menuBar, tearoff=0)
viewMenu = Menu(menuBar, tearoff=0)
zoomMenu = Menu(viewMenu, tearoff=0)
helpMenu = Menu(menuBar, tearoff=0)

# Toobar Menu ICOn Initializing photoIcon
UnderlineIcon = PhotoImage(file='icons/underline_30px.png')
BoldIcon = PhotoImage(file='icons/bold_30px.png')
ItalicIcon = PhotoImage(file='icons/italic_30px.png')
LeftIcon = PhotoImage(file='icons/align_left_30px.png')
RightIcon = PhotoImage(file='icons/align_right_30px.png')
CenterIcon = PhotoImage(file='icons/align_center_30px.png')

# File Menu Icon initializing photoIcon
newIcon = PhotoImage(file='icons/create_new-16.png')
openIcon = PhotoImage(file='icons/open_document-16.png')
newWindowIcon = PhotoImage(file='icons/windows8_tablet-16.png')
printIcon = PhotoImage(file='icons/print-16.png')
pagesetupIcon = PhotoImage(file='icons/page_overview_4-16.png')
exitIcon = PhotoImage(file='icons/exit-16.png')
saveIcon = PhotoImage(file='icons/save-16.png')
saveAsIcon = PhotoImage(file='icons/save_new-16.png')

# edit Menu icons initialization
undoIcon = PhotoImage(file='icons/edit/undo_16px.png')
redoIcon = PhotoImage(file='icons/edit/redo_16px.png')
cutIcon = PhotoImage(file='icons/edit/cut_16px.png')
copyIcon = PhotoImage(file='icons/edit/copy_16px.png')
pasteIcon = PhotoImage(file='icons/edit/paste_16px.png')
delIcon = PhotoImage(file='icons/edit/delete_16px.png')
searchIcon = PhotoImage(file='icons/edit/search_16px.png')
findIcon = PhotoImage(file='icons/edit/find_and_replace_16px.png')
findNextIcon = PhotoImage(file='icons/edit/find_and_replace_16px.png')
preIcon = PhotoImage(file='icons/edit/prev_16px.png')
replaceIcon = PhotoImage(file='icons/edit/find_and_replace_16px.png')
gotoIcon = PhotoImage(file='icons/edit/forward_16px.png')
selectAllIcon = PhotoImage(file='icons/edit/checkmark_16px.png')
timeDateIcon = PhotoImage(file='icons/edit/schedule_16px.png')

# format Icons Initialization
wordwrapIcon = PhotoImage(file='icons/format/word_16px.png')
fontIcon = PhotoImage(file='icons/format/typography_16px.png')

# View Icons Initialization
statusIcon = PhotoImage(file='icons/view/bar_chart_16px.png')
zoominIcon = PhotoImage(file='icons/view/zoom_in_16px.png')
zoomoutIcon = PhotoImage(file='icons/view/zoom_out_16px.png')
zoomDefaultIcon = PhotoImage(file='icons/view/view_16px.png')

# View Icons Initialization
viewHelpIcon = PhotoImage(file='icons/help/help_16px.png')
sendFeedbackIcon = PhotoImage(file='icons/help/feedback_16px.png')
aboutIcon = PhotoImage(file='icons/help/about_16px.png')

# adding menu items to the file  Menu
fileMenu.add_command(label='New', accelerator='Ctrl + N', underline=0, image=newIcon, compound=LEFT, command=new_file)
fileMenu.add_command(label='New Window', accelerator='Ctrl + Shift + N', underline=4, compound=LEFT,
                     image=newWindowIcon)
fileMenu.add_command(label='Open...', accelerator='Ctrl + O', underline=0, image=openIcon, compound=LEFT, command=open_file)
fileMenu.add_command(label='Save', accelerator='Ctrl + S', underline=0, image=saveIcon,command=save_file, compound=LEFT)
fileMenu.add_command(label='Save As...', accelerator='Ctrl + Shift + S',command=save_as_file, underline=5, compound=LEFT, image=saveAsIcon)
fileMenu.add_separator()
fileMenu.add_command(label='Page Setup...', underline=8, image=pagesetupIcon, compound=LEFT)
fileMenu.add_command(label='Print...', accelerator='Ctrl + P', underline=0, compound=LEFT, image=printIcon)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', compound=LEFT, image=exitIcon, underline=1, accelerator='Ctrl + Q',
                     command=exit_file)

# Edit Menu Items initialization
editMenu.add_command(label='Undo', accelerator='Ctrl + Z', image=undoIcon, compound=LEFT,command=undo_file)
editMenu.add_command(label='Redo', accelerator='Ctrl + Y',image=redoIcon, compound=LEFT,command=redo_file)
editMenu.add_separator()
editMenu.add_command(label='Cut',command=cut_file, accelerator='Ctrl + X', compound=LEFT, image=cutIcon)
editMenu.add_command(label='Copy',command= copy_file, accelerator='Ctrl + C', image=copyIcon, compound=LEFT)

editMenu.add_command(label='Paste',command=paste_file, accelerator='Ctrl + V', image=pasteIcon, compound=LEFT)
editMenu.add_command(label='Delete',command=delete_file, accelerator='Ctrl + Del', compound=LEFT, image=delIcon)
editMenu.add_separator()
editMenu.add_command(label='Search with bing', accelerator='Ctrl + E', image=searchIcon, compound=LEFT)

editMenu.add_command(label='Find', accelerator='Ctrl + F', image=findIcon, compound=LEFT, command=find_func)
editMenu.add_command(label='Find Next',command=find_func, accelerator='F3', compound=LEFT, image=findNextIcon)
editMenu.add_command(label='Find Prev',command=find_func, accelerator='Shift + F3', image=preIcon, compound=LEFT)

editMenu.add_command(label='Replace',command=find_func, accelerator='Ctrl + H', image=replaceIcon, compound=LEFT)
editMenu.add_command(label='Goto', accelerator='Ctrl + G', compound=LEFT, image=gotoIcon)
editMenu.add_separator()
editMenu.add_command(label='Select All',command=selectAll_file, accelerator='Ctrl + A', image=selectAllIcon, compound=LEFT)
editMenu.add_command(label='Time/Date',command=timeDate, accelerator='F5', image=timeDateIcon, compound=LEFT)

# Format Menu Items initialization
formatMenu.add_checkbutton(label='Word Wrap', image=wordwrapIcon, compound=LEFT)

# adding menu items to the View  Menu
viewMenu.add_cascade(label='Zoom', menu=zoomMenu)
show_status= StringVar()
show_status.set(True)
viewMenu.add_checkbutton(label='Status Bar', image=statusIcon, compound=LEFT, command=hide_statusBar,
                         variable=show_status,onvalue=True, offvalue=False)

# adding menu items to Zoom menu
zoomMenu.add_command(label='Zoom In', image=zoominIcon, compound=LEFT, accelerator='Ctrl + Plus', command= zoom_in_file)
zoomMenu.add_command(label='Zoom Out',command=zoom_out_file, image=zoomoutIcon, compound=LEFT, accelerator='Ctrl + Minus')
zoomMenu.add_command(label='Restored Default Zoom', image=zoomDefaultIcon, compound=LEFT, command=zoom_default_file, accelerator='Ctrl + 0')

# adding menu items to Help menu
helpMenu.add_command(label='View Help', image=viewHelpIcon, compound=LEFT, )
helpMenu.add_command(label='Send Feedback',command=send_feedback, image=sendFeedbackIcon, compound=LEFT)
helpMenu.add_command(label='About Tempopad', command=aboutHelp, image=aboutIcon, compound=LEFT)

# Cascading the menu Bar to the root windows
menuBar.add_cascade(label='File', underline=0, menu=fileMenu)
menuBar.add_cascade(label='Edit', underline=0, menu=editMenu)
menuBar.add_cascade(label='Format', underline=1, menu=formatMenu)
menuBar.add_cascade(label='View', underline=0, menu=viewMenu)
menuBar.add_cascade(label='Help', underline=0, menu=helpMenu)

# Setting the Tool bar menu 
# Font Style Element
fontElement = StringVar()
font_family = ft.families()
fontBox = ttk.Combobox(toolBar, width=25, textvariable=fontElement, state='readonly')
fontBox['values'] = font_family
fontBox.current(font_family.index('Arial CE'))
fontBox.grid(row=0, column=0, ipady=3, padx=5, pady=5)

# Font SizeElement
sizeElement = StringVar()
fontSize = ttk.Combobox(toolBar, width=25, textvariable=sizeElement, state='readonly')
fontSize['values'] = tuple(range(8, 42, 2))
fontSize.current(2)
fontSize.grid(row=0, column=1, ipady=3, padx=5, pady=5)

# Toobar Buttons Element Initializing
btnUnderline = ttk.Button(toolBar, image=UnderlineIcon, command=underline_file)
btnUnderline.grid(row=0, column=2, pady=5, padx=5)

btnBold = ttk.Button(toolBar, image=BoldIcon, command=bold_file)
btnBold.grid(row=0, column=3, pady=5, padx=5)

btnItalic = ttk.Button(toolBar, image=ItalicIcon, command=italic_file)
btnItalic.grid(row=0, column=4, pady=5, padx=5)

btnLeft = ttk.Button(toolBar, image=LeftIcon, command=left_align_file)
btnLeft.grid(row=0, column=5, pady=5, padx=5)

btnCenter = ttk.Button(toolBar, image=CenterIcon, command=center_align_file)
btnCenter.grid(row=0, column=6, pady=5, padx=5)

btnRight = ttk.Button(toolBar, image=RightIcon, command=right_align_file)
btnRight.grid(row=0, column=7, pady=5, padx=5)


# Status Bar Element
lblEmpty = Label(statusBar, text='    ', width=50)
lblEmpty.grid(row=0,column=0)

lblLine =Label(statusBar, text='Word: 0')
lblLine.grid(row=0, column=1, padx=5)
# lblcharacter = StringVar()
lblChar =Label(statusBar, text='Col: 0')
lblChar.grid(row=0, column=2, padx=5)

Label(statusBar, text='100%').grid(row=0, column=3, padx=5)
Label(statusBar, text='Windows(CRLF)').grid(row=0, column=4, padx=5)
Label(statusBar, text='UTF-8').grid(row=0, column=5, padx=10)
# binding event to the root
root.bind_all('<Control-q>', quit)




#binding controls
root.bind('<Control o>',open_file)
root.bind('<Control n>', new_file)
root.bind('<Control s>', save_file)
root.bind('<Control-Shift-S>', save_as_file)
fontSize.bind('<<ComboboxSelected>>', font_size_file)
fontBox.bind('<<ComboboxSelected>>', font_family_file)
scroltext.bind('<<Modified>>', change_text_file)
# compile and view notepad using mainloop
root.mainloop()
