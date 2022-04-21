
# This is the main file for ui elements of the application

from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Registration Form")
window.geometry('500x550')


label_title = Label(window, text="Registration Form",font=("black", 20))
label_title.place(x=150,y=53)

label_a = Label(window,text = "Name",font=("bold", 12))
label_b = Label(window,text = "Code Id",font=("bold", 12))
label_c = Label(window,text = "Gender",font=("bold", 12))
label_d = Label(window,text = "Country",font=("bold", 12))
label_e = Label(window,text = "Interest",font=("bold", 12))
label_a.place(x=90,y=130)
label_b.place(x=90,y=180)
label_c.place(x=90,y=230)
label_d.place(x=90,y=280)
label_e.place(x=90,y=330)

entry_a = Entry(window)
entry_b = Entry(window)
entry_c = Entry(window)
entry_d = Entry(window)
entry_e = Entry(window)
entry_b.place(x=240,y=180)
entry_c.place(x=240,y=230)
entry_d.place(x=240,y=280)
entry_e.place(x=240,y=330)

var = IntVar()
Radiobutton(window, text="Male",font=("bold", 11),padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(window, text="Female",font=("bold", 11),padx = 20, variable=var, value=2).place(x=295,y=230)

Button(window, text='Submit',font=("bold", 11),width=20,bg='maroon',fg='ivory').place(x=160,y=400)

window.mainloop()