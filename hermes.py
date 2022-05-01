#importing other parts
from turtle import window_width
from typing import OrderedDict
from wsgiref.validate import PartialIteratorWrapper
from src import Locator, Person
from threading import Thread
from tkinter import *

from src.ui import ui_run
from src import start


# Dictionary for participants
participants = OrderedDict()
vib_strengths = []

def main():
    """
    This is the main function for hermes application. 
    """
    # start()
    ### initialisation
    # UI initialisation
    window = Tk()
    window.title("Hermes")
    window.geometry('300x500')

    # Dictionary for participants
    # participants = OrderedDict()
    # vib_strengths = [[]]
    # people locator
    locator = Locator(participants, window)
    # start locator loop
    locator.run_locator()
    # set the ui
    ui_run(window, participants, update_strengths)
    
    # Start the UI
    # callbacks are attached to this window... sigh
    # it's an infinite loop btw
    window.mainloop()
    
def update_strengths():
    """
    update vibration strengths between people
    """
    vib_strengths.clear()
    sub_strengths = []
    for this_id, this_person in participants.items():
        for target_id, target_person in participants.items():
            sub_strengths.append(this_person.vib_strength(target_person))
        vib_strengths.append(sub_strengths)
    print(vib_strengths)
    
        
    
    
if __name__ == "__main__":
    main()