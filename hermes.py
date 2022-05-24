#importing other parts
from typing import OrderedDict
from src import Locator, Person
from threading import Thread
from tkinter import *

from src.ui import ui_run
from src import server_start


# Dictionary for participants
participants = OrderedDict()
vib_strengths = [0, 2, 3]

def main():
    """
    This is the main function for hermes application. 
    """
    # start()
    ### initialisation
    # UI initialisation
    window = Tk()
    window.title("Hermes")
    window.geometry('425x550')
    # locator = Locator(participants, window)
    # server_thread = Thread(target=server_start, args=(vib_strengths, ))
    # people locator
    # locator.run_locator()

    # set the ui
    ui_run(window, participants, update_strengths)
    # start the server
    # server_thread.start()
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