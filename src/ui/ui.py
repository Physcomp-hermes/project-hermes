import sqlite3
import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import Combobox

# create object 'window' of Tk()
window = Tk()
window.title("Registration Form")
window.geometry('500x550')
# set font design
f1 = tkFont.Font(family='URW Gothic L', size=20)
f2 = tkFont.Font(family='Ubuntu Mono', size=12)
f3 = tkFont.Font(family='Sawasdee', size=11)

# set each variable to save data
Name = StringVar()
var1 = StringVar()
var2 = IntVar()
Country = StringVar()
var3 = StringVar()

# Function to save the data
def database():
    name=Name.get()
    codeId=var1.get()
    gender=var2.get()
    country=Country.get()
    interest=var3.get()
    conn=sqlite3.connect('person.py')
    with conn:
        cursor=conn.cursor()
    cursor.execute('INSERT INTO Person (Name, Code Id, Gender, Country, Interest)',(name,codeId,gender,country,interest,))
    conn.commit()

# create a title label
label_title = Label(window, text="Registration Form",font=f1)
label_title.place(x=150,y=53)

# create a name label
label_a = Label(window,text = "Name",font=f2)
label_a.place(x=90,y=130)
# create a text entry box for name
entry_a = Entry(window,textvariable=Name)
entry_a.place(x=240,y=130)

# create a code id label
label_b = Label(window,text = "Code Id",font=f2)
label_b.place(x=90,y=180)
# create list of code id available in the dropdownlist
var1.set("1")
data_1=("1", "2", "3", "4")
entry_b = Combobox(window, values=data_1, width=17)
entry_b.place(x=240,y=180)

# create a gender label
label_c = Label(window,text = "Gender",font=f2)
label_c.place(x=90,y=230)
# create 'Radio button' widget and uses place() method
Radiobutton(window, text="Male",font=("bold", 11),padx = 5, variable=var2, value=1).place(x=235,y=230)
Radiobutton(window, text="Female",font=("bold", 11),padx = 20, variable=var2, value=2).place(x=295,y=230)

# create a country label
label_d = Label(window,text = "Country",font=f2)
label_d.place(x=90,y=280)
# create a text entry box for country
entry_d = Entry(window, textvariable=Country)
entry_d.place(x=240,y=280)

# create a interest label
label_e = Label(window,text = "Interest Categories",font=f2)
label_e.place(x=90,y=330)
# create list of interest available in the dropdownlist
var3.set("Interest")
data_2=("Arts", "Vehicles", "Beauty", "Fitness", "Business", "Electronics", "Finance", "Food & Drink", "Games", "Home", "Internet", "Jobs", "Education")
entry_e = Combobox(window, values=data_2, width=17)
entry_e.place(x=240,y=330)

# create a Submit Button and place into the window
Button(window, text='Submit',font=f3,width=20,bg='maroon',fg='ivory',command=database).place(x=160,y=400)

# run the mainloop
window.mainloop()