# from atexit import register
# from sqlite3 import Time, register_converter
# import string
from tkinter import*
from turtle import right

ws = Tk()
ws.geometry('700x300')
ws.title('registration')
ws . config(bg='#0B5A81')

f =('Time',14)
var=StringVar()
var.set('male')

country=[]
Variable= StringVar()



Matricnumber = StringVar()

username = StringVar()
Othername = StringVar()
Email = StringVar()
Mobilenumber = StringVar()
Password = StringVar()
Stateoforigin = StringVar()

# world =open('countries.txt','r')
# for countries in world:
#     country=country.rstrip('\n')
#     countries.append(country)
#     Variable.set(countries[22])
right_frame= Frame(
        ws,
        bd=2,
        bg="#cccccc",
        relief=SOLID,
        padx=10,
        pady=10
    )
Label(
        right_frame,
        text="Enter Name",
        bg='#cccccc',
        font=f
    ).grid(row=0, column=0,sticky=W, pady=10)


Label(
        right_frame,
        text="Enter Email",
        bg='#cccccc',
        font=f
    ).grid(row=1, column=0,sticky=W, pady=10)

Label(
        right_frame,
        text="Contact Number",
        bg='#cccccc',
        font=f
    ).grid(row=2, column=0,sticky=W, pady=10)

Label(
        right_frame,
        text="Select Gender",
        bg='#cccccc',
        font=f
    ).grid(row=3, column=0,sticky=W, pady=10)

Label(
        right_frame,
        text="Select Country",
        bg='#cccccc',
        font=f
    ).grid(row=4, column=0,sticky=W, pady=10)


Label(
        right_frame,
        text="Enter Password",
        bg='#cccccc',
        font=f
    ).grid(row=5, column=0,sticky=W, pady=10)


Label(
        right_frame,
        text="Re-Enter Password",
        bg='#cccccc',
        font=f
    ).grid(row=2, column=0,sticky=W, pady=10)


gender_frame =Label(
        right_frame,
        bg='#cccccc',
        padx=10,
        pady=10,
)


register_name=Entry(
    right_frame,
    font=f
)

register_email=Entry(
    right_frame,
    font=f
)

register_mobile=Entry(
    right_frame,
    font=f
)

male_rb=Radiobutton(
    gender_frame,
    text='male',
    bg='#CCCCCC',
    variable=var,
    value='male',
    font=('Times',10),
)


female_rb=Radiobutton(
    gender_frame,
    text='female',
    bg='#CCCCCC',
    variable=var,
    value='female',
    font=('Times',10),
)

other_rb=Radiobutton(
    gender_frame,
    text='Others',
    bg='#CCCCCC',
    variable=var,
    value='others',
    font=('Times',10),
)

# register_Countries=OptionMenu(
#     right_frame,
#     Variable,
#     *countries

# )

# register_Countries.config(
#     width=15,
#     font=('Times',12)

# )


register_pwd= Entry(
    right_frame,
    font=f,
    show='*'

)


pwd_again=Entry(
    right_frame,
    font=f,
    show='*',

)



register_btn=Button(
    right_frame,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=None,


)
register_name.grid(row=0,column=1,pady=10, padx=20,)

register_email.grid(row=1,column=1,pady=10, padx=20,)
register_mobile.grid(row=2,column=1,pady=10, padx=20,)
#register_Countries.grid(row=3,column=1,pady=10, padx=20,)
register_pwd.grid(row=4,column=1,pady=10, padx=20,)
pwd_again.grid(row=5,column=1,pady=10, padx=20,)
register_btn.grid(row=6,column=1,pady=10, padx=20,)
right_frame.pack()


gender_frame.grid(row=3, column=1,pady=10,padx=20)
male_rb.pack(expand=True,side=LEFT)
female_rb.pack(expand=True,side=LEFT)
other_rb.pack(expand=True,side=LEFT)





ws.mainloop


    







