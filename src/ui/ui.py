import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import Combobox


# create object 'window' of Tk()
window = Tk()
window.title("Registration Form")
window.geometry('500x560')
# set font design
f1 = tkFont.Font(family='URW Gothic L', size=20)
f2 = tkFont.Font(family='Ubuntu Mono', size=12)
f3 = tkFont.Font(family='Sawasdee', size=11)


# form ui
def draw_ui():
    # create a title label
    label_title = Label(window, text="Registration Form",font=f1)
    label_title.place(x=150,y=53)

    # create a name label
    label_a = Label(window,text = "Name",font=f2)
    label_a.place(x=90,y=130)
    # create a text entry box for name
    name = StringVar()
    entry_name = Entry(window,textvariable=name)
    entry_name.place(x=240,y=130)

    # create a code id label
    label_b = Label(window,text = "Code Id",font=f2)
    label_b.place(x=90,y=180)
    # create list of code id available in the dropdownlist
    # list of code id
    list_id=("1", "2", "3", "4","5")
    entry_id = Combobox(window, values=list_id, width=17)
    entry_id.place(x=240,y=180)

    # create a gender label
    label_c = Label(window,text = "Gender",font=f2)
    label_c.place(x=90,y=230)
    # create 'Radio button' widget and uses place() method
    gender = IntVar()
    gender.set(1)
    Radiobutton(window, text="Male",font=("bold", 11),padx = 5, variable=gender, value=1).place(x=235,y=230)
    Radiobutton(window, text="Female",font=("bold", 11),padx = 20, variable=gender, value=2).place(x=295,y=230)

    # list of interest category
    list_category=("Arts", "Vehicles", "Beauty", "Fitness", "Business", "Electronics", "Finance", "Food & Drink", "Games", "Home", "Internet", "Jobs", "Education")

    # create a interest category label
    label_d = Label(window,text = "Interest Category 1",font=f2)
    label_d.place(x=90,y=280)
    # create list of interest available in the dropdownlist
    entry_category1 = Combobox(window, values=list_category, width=17)
    entry_category1.place(x=240,y=280)

    # create a interest category label
    label_e = Label(window,text = "Interest Category 2",font=f2)
    label_e.place(x=90,y=330)
    # create list of interest available in the dropdownlist
    entry_category2 = Combobox(window, values=list_category, width=17)
    entry_category2.place(x=240,y=330)

    # create a interest category label
    label_f = Label(window,text = "Interest Category 3",font=f2)
    label_f.place(x=90,y=380)
    # create list of interest available in the dropdownlist
    entry_category3 = Combobox(window, values=list_category, width=17)
    entry_category3.place(x=240,y=380)

    # create a Submit Button and place into the window
    Button(window, text='Submit',font=f3,width=20,bg='maroon',fg='ivory',command=ui_run).place(x=160,y=450)

    # run the mainloop
    window.mainloop()


def ui_run():
    # draw UI
    draw_ui()
        
    #while True:
    # Take in form input
    # if the form is submitted, save as variable
    # Append to people list
    while True: 

        name=draw_ui().name.get()
        codeId=draw_ui().entry_id.get()
        gender=draw_ui().gender.get()
        interest1=draw_ui().entry_category1.get()
        interest2=draw_ui().entry_category2.get()
        interest3=draw_ui().entry_category3.get()
            
        # if user not fill any entry
        # then print "empty input"
        if (name == "" and
            codeId == "" and
            gender == "" and
            interest1 == "" and
            interest2 == "" and
            interest3 == ""):
                
            print("empty input")
    
        else: 
            list = []
            list.append( name, codeId, gender, interest1, interest2, interest3)
            return list 

if __name__ == "__main__":
    ui_run()
