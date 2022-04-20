
# This is the class for each person during the event

class Person:
    def __init__(self, id, category):
        '''
        Initialise the person class
        id: ID of this person
        category: category (for prototyping purpose)
        '''
        self.id = id
        self.category = category
        
        # This the person this percon is currently facing at. 
        # -1 means facing at no one
        self.facing = -1

    def set_facing(self, id):
        '''
        Update who this person is facing at
        id: ID of the person this person is facing at
        '''
        self.facing = id

    def get_facing(self):
        '''
        Returns the id of person this person is facing at
        '''
        return self.facing
    
    def get_id(self):
        '''
        Returns the id of this participant
        '''
        return self.id
    
    def get_commonality(self, target_category):
        '''
        Returns the signal strength 
        '''
        
        if target_category == self.category:
            return 1
        else:
            return 0



