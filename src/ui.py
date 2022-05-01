from multiprocessing.sharedctypes import Value
import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import Combobox
from collections import OrderedDict

from src.person import Person




# form ui
def draw_ui(frame, field_dict, callback):
    """
    field_dict: ordered dictionary containing field label and content
    callback: callback function to be executed when button is clicked
    """
    

    # set font design
    f1 = tkFont.Font(family='URW Gothic L', size=20)
    f2 = tkFont.Font(family='Ubuntu Mono', size=12)
    f3 = tkFont.Font(family='Sawasdee', size=11)

    # list of interest category
    list_id=("1", "2", "3", "4","5")
    list_category=("Arts", "Vehicles", "Beauty", "Fitness", "Business", "Electronics", "Finance", "Food & Drink", "Games", "Home", "Internet", "Jobs", "Education")

    # frame.pack(expand=True)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # title
    Label(frame, text="Registration Form",font=f1).grid(row = 0, columnspan=2)

    field_row = 1
    for labelText, content in field_dict.items():
        Label(frame,text = labelText,font=f2).grid(row = field_row, column = 0)
        if labelText == "ID":
            OptionMenu(frame, content, *list_id).grid(row = field_row, column= 1,sticky='ew')
        else:
            OptionMenu(frame, content, *list_category).grid(row = field_row, column= 1,sticky='ew')
        field_row += 1
    
    # create a Submit Button and place into the window
    Button(frame, text='Submit',font=f3, command=callback).grid(row = 5, columnspan=2)


def ui_run(frame, people_dict, update_callback):
    
    #initialise dictionary used to save variable
    field_dict = OrderedDict([
        ("ID", IntVar(frame)),
        ("Interest 1", StringVar(frame)),
        ("Interest 2", StringVar(frame)),
        ("Interest 3", StringVar(frame))
        ])

    def ui_callback():

        person = Person(field_dict["ID"].get())
        people_dict[person.get_id()] = person
        person.add_interest(field_dict["Interest 1"].get())
        person.add_interest(field_dict["Interest 2"].get())
        person.add_interest(field_dict["Interest 3"].get())
        update_callback()
    
    # draw UI
    draw_ui(frame, field_dict, ui_callback)
