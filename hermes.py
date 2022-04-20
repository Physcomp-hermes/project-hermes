#importing other parts
from src.person import Person
# import src.locator.locator
# import src.server.server

people_list = []

def main():
    """
    This is the main function for hermes application. 
    """

    ### initialisation

    # Do some initialisation initialisation   
    
    # Adding people for testing purposes
    add_person(1,4, True)
    add_person(2,4)

    # Start input thread. This thread will use to run UI and add people in the system.
    # DW about how to run threading for now. We can handle it at some point
    # The UI class should update 

    
    # Set up the server
    # i.e. server.start()

    ### Main processing loop. 
    while True:

        # Update who's facing who
        # i.e. Locator.update(people_list)
        
        # Send vibration signal to web clients (devices)
        # The person class has method has_device() that returns true if this person is holding a device
        # i.e. server.send(people_list)
        
        # We will need to put some delay in case processing can't keep up
        # delay(100)
        for person in people_list:
            print(person.get_id())
        break
    # Display UI

    # Establish connection with UI

    # Run the application
    
    print("This is the hermes project!\n")
    
    return
    
def add_person(id, category, device=False):
    '''
    Function to add people in people list.
    This should be called with when UI enters
    '''
    # TODO: Make sure there are no id duplicate
    person = Person(id, category, device)
    people_list.append(person)

def get_input():
    '''
    A class to get input from UI.
    This function will be used for threading?
    '''

    while True:
        ui_added()
        

def ui_added():
    '''
    event method that gets triggered when people save UI
    '''
    print("UI event\n")


if __name__ == "__main__":
    main()