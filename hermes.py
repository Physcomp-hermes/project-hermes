#importing other parts
from typing import OrderedDict
from src import Locator, Person
from threading import Thread
from tkinter import *

from src.ui import ui_run
from src import server_start


# Dictionary for participants
participants = OrderedDict()

# List containig current vibration strength of each participants
vib_strengths = [0, 1, 2]

window = Tk()
window.title("Hermes")
window.geometry('435x500')
def main():
    """
    This is the main function for hermes application. 
    """
    # start()
    ### initialisation
    # UI initialisation
    locator = Locator(participants, window)
    server_thread = Thread(target=server_start, args=(participants, ))
    # people locator
    locator.run_locator()

    # placeholder for participant 0
    # Used because system currently doesn't recognise marker 1
    
    person = Person(0)
    participants[person.get_id()] = person
    person.add_interest(" ")
    person.add_interest(" ")
    person.add_interest(" ")

    # set the ui
    ui_run(window, participants)
    # start the server
    server_thread.start()
    # Start the UI
    # callbacks are attached to this window... sigh
    # it's an infinite loop btw
    window.mainloop()
    
if __name__ == "__main__":
    main()