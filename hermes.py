#importing other parts
from typing import OrderedDict
from src import Locator, Person
from threading import Thread
from tkinter import *

from src.ui import ui_run
from src import server_start

# Dictionary for participants
participants = OrderedDict()

window = Tk()
window.title("Hermes")
window.geometry('425x600')
window.configure(bg='white')
def main():
    """
    This is the main function for hermes application. 
    """
    # start()
    ### initialisation
    participant_init()
    # UI initialisation
    locator = Locator(participants, window)
    server_thread = Thread(target=server_start, args=(participants, ))
    locator.run_locator()
    ui_run(window, participants, locator.calibrate_extrinsics)
    # start the server
    server_thread.start()
    
    # callbacks are attached to this window... sigh
    # it's an infinite loop btw
    window.mainloop()
    
def participant_init():
    # placeholder for participant 0
    # Used because system currently doesn't recognise marker 1
    person = Person(0)
    participants[person.get_id()] = person
    person.add_interest(" ")
    person.add_interest(" ")
    person.add_interest(" ")

if __name__ == "__main__":
    main()