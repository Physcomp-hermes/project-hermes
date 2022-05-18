import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from collections import OrderedDict
from unicodedata import category

from .person import Person

# list of interest category
list_id=["1", "2", "3", "4","5"]
category_dict = OrderedDict()
category_dict["Year level"] = ["First", "Second", "Third & after", "Postgrad"]
category_dict["Major"] = ["Computer science", "Electrical engineering", "Information technology", "Mechatronics engineering", "Software engineering", "Other"]
category_dict["Library in campus"] = ["Architecture library", "BSL library", "Central library", "Dorothy hill", "Law library"]
category_dict["Coffee in campus"] = ["Bagel boys", "Beans engineered", "Darwins", "Lakeside cafe", "Merlos in great court", "Nano cafe", "Phiyzz cafe", "Red bull", "The one in mains"]

# form ui
def draw_ui(frame, field_dict, callback):
    """
    field_dict: ordered dictionary containing field label and content
    callback: callback function to be executed when button is clicked
    """
    # set font design
    f1 = tkFont.Font(family="URW Gothic L", size=20)
    f2 = tkFont.Font(family="Ubuntu Mono", size=12)
    f3 = tkFont.Font(family="Sawasdee", size=11)
    
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # title
    Label(frame, text="Registration Form",font=f1).grid(row = 0, columnspan=2,pady=10)

    field_row = 1
    for labelText, content in field_dict.items():
        Label(frame,text = labelText, font=f2).grid(row = field_row, column = 0,sticky=W, padx=(55,0),pady=10)
        if labelText == "ID":
            OptionMenu(frame, content, *list_id).grid(row = field_row, column= 1,sticky=E,padx=(0,55),pady=10,ipadx=2)
        else:
            OptionMenu(frame, content, *category_dict[labelText]).grid(row = field_row, column= 1,sticky=E,padx=(0,55),pady=10,ipadx=5)
        field_row += 1
    
    # create a Submit Button and place into the window
    Button(frame, text='Submit',font=f3, command=callback).grid(row = 6, columnspan=2,pady=(40,60),ipadx=20,ipady=5)


def ui_run(frame, people_dict):
    
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
        for key in field_dict:
            if key == "ID":
                continue
            field_value = field_dict[key].get()
            person.add_interest(category_dict[key].index(field_value))
        # print(person.get_interests())
    # draw UI
    draw_ui(frame, field_dict, ui_callback)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hermes")
    window.geometry('300x450')
    def callback_print():
        print("Button pressed")
    people = OrderedDict()
    ui_run(window, people, callback_print)
    window.mainloop()