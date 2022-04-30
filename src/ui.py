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

form_body = Frame(window)

# form ui
def draw_ui():

    # list of interest category
    list_id=("1", "2", "3", "4","5")
    list_category=("Arts", "Vehicles", "Beauty", "Fitness", "Business", "Electronics", "Finance", "Food & Drink", "Games", "Home", "Internet", "Jobs", "Education")

    form_body.pack(expand=True)
    form_body.grid_columnconfigure(0, weight=1)
    form_body.grid_rowconfigure(0, weight=1)

    # title
    label_title = Label(window, text="Registration Form",font=f1)
    label_title.place(x=150,y=53)

    # id
    label_b = Label(form_body,text = "Code Id",font=f2).grid(row = 0, column = 0)
    entry_id = Combobox(form_body, values=list_id, width=17).grid(row = 0, column = 1)

    # interest #1
    label_d = Label(form_body, text = "Interest Category 1",font=f2).grid(row = 1, column = 0)
    entry_category1 = Combobox(form_body, values=list_category, width=17).grid(row = 1, column= 1)

    # interest #2
    label_e = Label(form_body,text = "Interest Category 2",font=f2).grid(row = 2, column= 0)
    entry_category2 = Combobox(form_body, values=list_category, width=17).grid(row = 2, column= 1)

    # interest #3
    label_f = Label(form_body,text = "Interest Category 3",font=f2).grid(row = 3, column= 0)
    entry_category3 = Combobox(form_body, values=list_category, width=17).grid(row = 3, column= 1)

    # create a Submit Button and place into the window
    Button(window, text='Submit',font=f3,width=20,bg='maroon',fg='ivory',command=ui_run).place(x=160,y=450)

    # run the mainloop
    window.mainloop()


def ui_run():
    # draw UI
    draw_ui()

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


# Depreciated

    # # create a name label
    # label_a = Label(window,text = "Name",font=f2)
    # label_a.place(x=90,y=130)
    # # create a gender label
    # label_c = Label(window,text = "Gender",font=f2)
    # label_c.place(x=90,y=230)
    # # create 'Radio button' widget and uses place() method
    # gender = IntVar()
    # gender.set(1)
    # Radiobutton(window, text="Male",font=("bold", 11),padx = 5, variable=gender, value=1).place(x=235,y=230)
    # Radiobutton(window, text="Female",font=("bold", 11),padx = 20, variable=gender, value=2).place(x=295,y=230)
