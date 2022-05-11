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
    
    # set font design
    # TODO: Include the style in repository so it works on other devices too
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
    Label(frame, text="Registration Form",font=f1).grid(row = 0, columnspan=2,pady=10)

    field_row = 1
    for labelText, content in field_dict.items():
        Label(frame,text = labelText,font=f2).grid(row = field_row, column = 0,sticky=W, padx=60,pady=10)
        if labelText == "ID":
            OptionMenu(frame, content, *list_id).grid(row = field_row, column= 1,sticky=E,padx=60,pady=10,ipadx=2)
        else:
            OptionMenu(frame, content, *list_category).grid(row = field_row, column= 1,sticky=E,padx=60,pady=10,ipadx=5)
        field_row += 1
    
    # create a Submit Button and place into the window
    Button(frame, text='Submit',font=f3, command=callback).grid(row = 5, columnspan=2, pady=60,ipadx=20,ipady=5)


def ui_run(frame, people_dict):
    '''
    Run the UI. The window main loop needs to be started from somewhere else. 
    frame: Tkinter object that this UI is in
    people_dict: people dictionary to save the user data.
    '''
    #initialise dictionary used to save variable
    # it is ordered dictionary because the order is important when 
    field_dict = OrderedDict([
        ("ID", IntVar(frame,1)),
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
        print(f"Person {person.get_id()} added to system")
    
    # draw UI
    draw_ui(frame, field_dict, ui_callback)


if __name__ == "__main__":
    window = Tk()
    window.title("Hermes")
    window.geometry('435x500')
    def callback_print():
        print("Button pressed")
    people = OrderedDict()
    ui_run(window, people, callback_print)
    window.mainloop()