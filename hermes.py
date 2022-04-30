#importing other parts
from src import Locator, Person
from threading import Thread

people_list = []

def main():
    """
    This is the main function for hermes application. 
    """
    ### initialisation
    participants = {1:Person(1, True), 2:Person(2,True), 3:Person(3,False)} # Dictionary for participants
    
    # Do some initialisation initialisation   
    
    # Adding people for testing purposes
    
    # Start input thread. This thread will use to run UI and add people in the system.
    # DW about how to run threading for now. We can handle it at some point
    # The UI class should update 
    locator = Locator(participants)
    locator.run_locator()
    # locator_thread = Thread(target=locator.run_locator)
    # locator_thread.start()
    # Set up the server
    # ui_run(participants)
    # run_locator(participants)

    ### Main processing loop. 
    while True:
        # Check if the participants is modified.

        # Update who's facing who
        # i.e. Locator.update(people_list)
        # machines have id
        # request from id = 1 -> send vibration strength (0- 10) based on who this is facing

        # Send vibration signal to web clients (devices)
        # The person class has method has_device() that returns true if this person is holding a device
        # i.e. server.send(people_list)
        
        # print("This is the hermes project!\n")
        pass
    

if __name__ == "__main__":
    main()