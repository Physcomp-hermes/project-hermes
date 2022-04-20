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

    # Do misc. initialisation   
    
    # Adding people for testing purposes
    add_person(1,4)
    add_person(2,4)

    # Start input thread
    
    # Set up the server
    # i.e. server.start()

    while True:
        # This is the main processing loop

        # Update who's facing who
        # i.e. Locator.update(people_list)
        
        # Send signal strength to other people
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
    
def add_person(id, category):
    '''
    Function to add people in people list.
    This should be called with when UI enters
    '''
    # TODO: Make sure there are no id duplicate
    person = Person(id, category)
    people_list.append(person)

if __name__ == "__main__":
    main()