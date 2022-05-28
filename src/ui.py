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
    main_font = tkFont.Font(family="Roboto", size=20)

    # list of interest category
    list_id=("1", "2", "3", "4","5")
    category_dict = OrderedDict()
    category_dict["Year level"] = ["First", "Second", "Third & after", "Postgrad"]
    category_dict["Major"] = ["Computer science", "Electrical engineering", "Information technology", "Mechatronics engineering", "Software engineering", "Other"]
    category_dict["Library in campus"] = ["Architecture library", "BSL library", "Central library", "Dorothy hill", "Law library"]
    category_dict["Coffee in campus"] = ["Bagel boys", "Beans engineered", "Darwins", "Lakeside cafe", "Merlos in great court", "Nano cafe", "Phiyzz cafe", "Red bull", "The one in mains"]
    
    # frame.pack(expand=True)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # title
    # Label(frame, text="Registration Form",font=f1).grid(row = 0, columnspan=2,pady=(30,20))
    Label(frame, text="Registration Form",font=main_font).grid(row = 0, columnspan=2,pady=(30,20))
    
    field_row = 1
    for labelText, content in field_dict.items():
        # Label(frame,text = labelText, font=f2).grid(sticky=W, padx=(55,0),pady=(5,0))
        # if labelText == "ID":
        #     optionMenu = OptionMenu(frame, content, *list_id)
        #     optionMenu.config(width=50)
        #     optionMenu.grid(sticky=W,padx=55,pady=(0,10))

        Label(frame,text = labelText, font=f2, bg='white').grid(sticky=W, padx=(55,0),pady=(5,0))
        if labelText == "ID":
            optionMenu = OptionMenu(frame, content, *list_id)
            optionMenu.config(width=150)
            optionMenu.grid(columnspan=2,sticky=W,padx=55,pady=(0,10))
        else:
            optionMenu = OptionMenu(frame, content, *category_dict[labelText])
            optionMenu.config(width=150)
            optionMenu.grid(columnspan=2,sticky=W,padx=55,pady=(0,10))
        field_row += 1

    # create a Submit Button and place into the window
    # Button(frame, text='Submit',font=f3, command=callback, bg = "deepskyblue", fg = "white").grid(row = 12, columnspan=2,pady=30,ipadx=20,ipady=5)
    Button(frame,text='Submit',font=main_font, command=callback, highlightbackground='#3E4149', fg = "white").grid(row = 12, column=0,sticky=W,padx=(80,0),pady=(30,50),ipadx=25,ipady=3)
    Button(frame, text='Calibrate',font=main_font, command=callback, bg = "deepskyblue", fg = "white").grid(row = 12, column=1,sticky=E,padx=(0,80),pady=(30,50),ipadx=20,ipady=3)


def ui_run(frame, people_dict, update_callback):
    
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
    window.geometry('425x550')
    def callback_print():
        print("Button pressed")
    people = OrderedDict()
    ui_run(window, people, callback_print)
    window.mainloop()