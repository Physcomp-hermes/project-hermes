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
def draw_ui(frame, field_dict, register_callback, calib_callback):
    """
    field_dict: ordered dictionary containing field label and content
    callback: callback function to be executed when button is clicked
    """
    # set font design
    main_font = tkFont.Font(family="Roboto", size=20)
    content_font = tkFont.Font(family="Ubuntu Mono", size=12)

    # set the image 
    btn1= tk.PhotoImage(file='./img/button1.png')
    btn2= tk.PhotoImage(file='./img/button2.png')

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # title
    Label(frame, text="Registration Form",font=main_font,bg='white').grid(row = 0, columnspan=2,pady=(30,15))

    field_row = 1
    for labelText, content in field_dict.items():
        Label(frame,text = labelText, font=content_font, bg='white').grid(sticky=W, padx=(55,0),pady=(5,0))
        if labelText == "ID":
            optionMenu = OptionMenu(frame, content, *list_id)
            optionMenu.config(width=150,highlightthickness=1,highlightbackground="#3684c6")
            optionMenu.grid(columnspan=2,sticky=W,padx=55,pady=(0,10),ipady=5)
        else:
            optionMenu = OptionMenu(frame, content, *category_dict[labelText])
            optionMenu.config(width=150,highlightthickness=1,highlightbackground="#3684c6")
            optionMenu.grid(columnspan=2,sticky=W,padx=55,pady=(0,10),ipady=5)
        field_row += 1
    
    # create a Submit Button and place into the window
    Button(frame,image=btn1,command=register_callback,width="90",height="35",borderwidth=0).grid(row = 12, column=0,sticky=W,padx=(80,0),pady=(30,50))
    Button(frame,image=btn1,command=calib_callback,width="90",height="35",borderwidth=0).grid(row = 12, column=1,sticky=E,padx=(0,80),pady=(30,50))


def ui_run(frame, people_dict, calib_callback):
    
    #initialise dictionary used to save variable
    field_dict = OrderedDict([
        ("ID", IntVar(frame)),
        ("Year level", StringVar(frame, value="First")),
        ("Major", StringVar(frame, value="Computer science")),
        ("Library in campus", StringVar(frame, value="Architecture library")),
        ("Coffee in campus", StringVar(frame, value="Bagel boys")),
        ])

    def ui_callback():

        person = Person(field_dict["ID"].get())
        people_dict[person.get_id()] = person
        for key in field_dict:
            if key == "ID":
                continue
            field_value = field_dict[key].get()
            person.add_interest(category_dict[key].index(field_value))
        
    # draw UI
    draw_ui(frame, field_dict, ui_callback, calib_callback)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Hermes")
    window.geometry('425x600')
    def callback_print():
        print("Button pressed")
    people = OrderedDict()
    ui_run(window, people, callback_print)
    window.mainloop()