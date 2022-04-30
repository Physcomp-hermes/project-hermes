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

    # Dictionary for participants
    participants = {} 
    
    # people locator
    locator = Locator(participants, window)
    # start locator loop
    locator.run_locator()
    # Set up the server
    ui_run(window, participants)
    
    # Start the UI
    # callbacks are attached to this window... sigh
    # it's an infinite loop btw
    window.mainloop()
    

if __name__ == "__main__":
    main()