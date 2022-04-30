from multiprocessing.sharedctypes import Value
import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import Combobox
from collections import OrderedDict

from src.person import Person


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
def draw_ui(field_dict, callback):
    """
    field_dict: ordered dictionary containing field label and content
    callback: callback function to be executed when button is clicked
    """
    # list of interest category
    list_id=("1", "2", "3", "4","5")
    list_category=("Arts", "Vehicles", "Beauty", "Fitness", "Business", "Electronics", "Finance", "Food & Drink", "Games", "Home", "Internet", "Jobs", "Education")

    form_body.pack(expand=True)
    form_body.grid_columnconfigure(0, weight=1)
    form_body.grid_rowconfigure(0, weight=1)

    # title
    label_title = Label(window, text="Registration Form",font=f1)
    label_title.place(x=150,y=53)

    field_row = 0
    for labelText, content in field_dict.items():
        Label(form_body,text = labelText,font=f2).grid(row = field_row, column = 0)
        if labelText == "ID":
            OptionMenu(form_body, content, *list_id).grid(row = field_row, column= 1,sticky='ew')
        else:
            OptionMenu(form_body, content, *list_category).grid(row = field_row, column= 1,sticky='ew')
        field_row += 1
    
    # create a Submit Button and place into the window
    Button(window, text='Submit',font=f3,width=20,bg='maroon',fg='ivory', command=callback).place(x=160,y=450)


def ui_run(people_dict):
    
    #initialise dictionary used to save variable
    field_dict = OrderedDict([
        ("ID", IntVar(window)),
        ("Interest 1", StringVar(window)),
        ("Interest 2", StringVar(window)),
        ("Interest 3", StringVar(window))
        ])

    def ui_callback():

        person = Person(field_dict["ID"].get())
        people_dict[person.get_id()] = person
        person.add_interest(field_dict["Interest 1"].get())
        person.add_interest(field_dict["Interest 2"].get())
        person.add_interest(field_dict["Interest 3"].get())
        pass
    
    # draw UI
    draw_ui(field_dict, ui_callback)

    # run the mainloop
    window.mainloop()


if __name__ == "__main__":
    ui_run()
