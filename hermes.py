#importing other parts
from typing import OrderedDict
from src import Locator, Person
from threading import Thread
from tkinter import *

from src.ui import ui_run
from src import server_start


# Dictionary for participants
participants = OrderedDict()
# matrix containing vibration strength from each to other participants
vib_strength_matrix = []

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
    person = Person(0)
    participants[person.get_id()] = person
    person.add_interest(" ")
    person.add_interest(" ")
    person.add_interest(" ")

    # set the ui
    ui_run(window, participants, update_strengths)
    # start the server
    server_thread.start()
    # inc_vib()
    # Start the UI
    # callbacks are attached to this window... sigh
    # it's an infinite loop btw
    window.mainloop()
    
def inc_vib():
    if vib_strengths[2] == 9:
        vib_strengths[2] = 1
    else:
        vib_strengths[2] += 1
    window.after(1000, inc_vib)
    print("str: ", vib_strengths[2])

def update_strengths():
    """
    update vibration strengths between people
    """
    vib_strength_matrix.clear()
    return
    for this_id, this_person in participants.items():
        sub_strengths = []
        for target_id, target_person in participants.items():
            # vib_strengths[this_id][target_id] = this_person.vib_strength(target_person)
            sub_strengths.append(this_person.calc_strength(target_person))
        vib_strength_matrix.append(sub_strengths.copy())
    print(vib_strength_matrix)    
    
    
if __name__ == "__main__":
    main()