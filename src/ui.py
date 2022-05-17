import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from collections import OrderedDict

from .person import Person




# form ui
def draw_ui(frame, field_dict, callback):
    """
    field_dict: ordered dictionary containing field label and content
    callback: callback function to be executed when button is clicked
    """
    # just to make some difference

    # set font design
    f1 = tkFont.Font(family="URW Gothic L", size=20)
    f2 = tkFont.Font(family="Ubuntu Mono", size=12)
    f3 = tkFont.Font(family="Sawasdee", size=11)

    # list of interest category
    list_id=("1", "2", "3", "4","5")
    list_category_1=("First", "Second", "Third & after", "Postgrad")
    list_category_2=("Computer science", "Electrical engineering", "Information technology", "Mechatronics engineering", "Software engineering", "Other")
    list_category_3=("Architecture library", "BSL library", "Central library", "Dorothy hill", "Law library")
    list_category_4=("Bagel boys", "Beans engineered", "Darwins", "Lakeside cafe", "Merlos in great court", "Nano cafe", "Phiyzz cafe", "Red bull", "The one in mains")
    
    # frame.pack(expand=True)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # title
    Label(frame, text="Registration Form",font=f1).grid(row = 0, columnspan=2,pady=(30,20))

    field_row = 1
    for labelText, content in field_dict.items():
        Label(frame,text = labelText, font=f2).grid(sticky=W, padx=(55,0),pady=(5,0))
        if labelText == "ID":
            optionMenu = OptionMenu(frame, content, *list_id)
            optionMenu.config(width=50)
            optionMenu.grid(sticky=W,padx=55,pady=(0,10))
        
        if labelText == "Year level":
            optionMenu = OptionMenu(frame, content, *list_category_1)
            optionMenu.config(width=50)
            optionMenu.grid(sticky=W,padx=55,pady=(0,10))
        if labelText == "Major":
            optionMenu = OptionMenu(frame, content, *list_category_2)
            optionMenu.config(width=50)
            optionMenu.grid(sticky=W,padx=55,pady=(0,10))
        if labelText == "Library in campus":
            optionMenu = OptionMenu(frame, content, *list_category_3)
            optionMenu.config(width=50)
            optionMenu.grid(sticky=W,padx=55,pady=(0,10))
        elif labelText == "Coffee in campus":
            optionMenu = OptionMenu(frame, content, *list_category_4)
            optionMenu.config(width=50)
            optionMenu.grid(sticky=W,padx=55,pady=(0,10))
        field_row += 1

    # create a Submit Button and place into the window
    Button(frame, text='Submit',font=f3, command=callback, bg = "deepskyblue", fg = "white").grid(row = 12, columnspan=2,pady=30,ipadx=20,ipady=5)


def ui_run(frame, people_dict, update_callback):
    
    #initialise dictionary used to save variable
    field_dict = OrderedDict([
        ("ID", IntVar(frame)),
        ("Year level", StringVar(frame)),
        ("Major", StringVar(frame)),
        ("Library in campus", StringVar(frame)),
        ("Coffee in campus", StringVar(frame)),
        ])

    def ui_callback():

        person = Person(field_dict["ID"].get())
        people_dict[person.get_id()] = person
        person.add_interest(field_dict["Year level"].get())
        person.add_interest(field_dict["Major"].get())
        person.add_interest(field_dict["Library in campus"].get())
        person.add_interest(field_dict["Coffee in campus"].get())
        update_callback()
    
    # draw UI
    draw_ui(frame, field_dict, ui_callback)


if __name__ == "__main__":
    window = Tk()
    window.title("Hermes")
    window.geometry("300x600")
    def callback_print():
        print("Button pressed")
    people = OrderedDict()
    ui_run(window, people, callback_print)
    window.mainloop()