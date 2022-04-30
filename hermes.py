#importing other parts
from turtle import window_width
from src import Locator, Person
from threading import Thread
from tkinter import *

from src.ui import ui_run


def main():
    """
    This is the main function for hermes application. 
    """
    ### initialisation
    # UI initialisation
    window = Tk()
    window.title("Hermes")
    window.geometry('300x500')

    frame_form = Frame(window, width=200)
    frame_form.place(anchor="w")
    frame_form.pack(expand=True, side=LEFT)
    frame_cam = Frame(window)
    participants = {} # Dictionary for participants
    # Do some initialisation initialisation   
    
    # This is the application window
    
    # Adding people for testing purposes
    
    # Start input thread. This thread will use to run UI and add people in the system.
    # DW about how to run threading for now. We can handle it at some point
    # The UI class should update 
    locator = Locator(participants, frame_cam)
    locator.run_locator()
    # Set up the server
    ui_run(frame_form, participants)
    # Start the UI
    # callbacks are attached to this window... sigh
    # it's an infinite loop btw
    window.mainloop()
    

if __name__ == "__main__":
    main()