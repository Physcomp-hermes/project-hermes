from os import getcwd
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from collections import OrderedDict
from unicodedata import category

from .person import Person

# list of interest category
list_id=["1", "2", "3", "4","5"]
category_dict = OrderedDict()
category_dict["Cat or dog?"] = ["Cat", "Dog", "None"]
category_dict["Favourite time of the day"] = ["Morning", "Afternoon", "Night"]
category_dict["If you were to watch a movie"] = ["Action", "Romance", "Comedy", "Horror"]
category_dict["Pineapple on Pizza?"] = ["Yes", "No"]

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
    global btn1, btn2
    btn1= tk.PhotoImage(file='./img/button3.png')
    btn2= tk.PhotoImage(file='./img/button4.png')

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    # title
    Label(frame, text="Registration Form",font=main_font,bg='white').grid(row = 0, columnspan=2,pady=(30,15))

    field_row = 1
    for labelText, content in field_dict.items():
        Label(frame,text = labelText, font=content_font, bg='white').grid(sticky=W, padx=(55,0),pady=(5,0))
        if labelText == "ID":
            optionMenu = OptionMenu(frame, content, *list_id)
            optionMenu.config(width=150,highlightthickness=1,highlightbackground="#3684c6", bg="white")
            optionMenu.grid(columnspan=2,sticky=W,padx=55,pady=(0,10),ipady=5)
        else:
            optionMenu = OptionMenu(frame, content, *category_dict[labelText])
            optionMenu.config(width=150,highlightthickness=1,highlightbackground="#3684c6", bg="white")
            optionMenu.grid(columnspan=2,sticky=W,padx=55,pady=(0,10),ipady=5)
        field_row += 1
    
    # create a Submit Button and place into the window
    Button(frame,image=btn1,command=register_callback,width="90",height="38",borderwidth=0, bg="white").grid(row = 12, column=0,sticky=W,padx=(80,0),pady=(30,50))
    Button(frame,image=btn2,command=calib_callback,width="90",height="38",borderwidth=0, bg="white").grid(row = 12, column=1,sticky=E,padx=(0,80),pady=(30,50))
    # Button(frame,command=register_callback,width="90",height="35",borderwidth=0).grid(row = 12, column=0,sticky=W,padx=(80,0),pady=(30,50))

def ui_run(frame, people_dict, calib_callback):
    
    #initialise dictionary used to save variable
    field_dict = OrderedDict([
        ("ID", IntVar(frame, value="1")),
        ("Cat or dog?", StringVar(frame, value="None")),
        ("Favourite time of the day", StringVar(frame, value="Morning")),
        ("If you were to watch a movie", StringVar(frame, value="Action")),
        ("Pineapple on Pizza?", StringVar(frame, value="Yes")),
        ])

    def ui_callback():

        person = Person(field_dict["ID"].get())
        people_dict[person.get_id()] = person
        for key in field_dict:
            if key == "ID":
                continue
            field_value = field_dict[key].get()
            # print(field_value)
            person.add_interest(category_dict[key].index(field_value))
            person.add_interest_string(field_value)
        print(person.get_interests())
        print(person.get_colour())
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