from marker import Marker
# This is the class for each person during the event

class Person:
    def __init__(self, id, category, device=False):
        '''
        Initialise the person class
        id: ID of this person
        category: category (for prototyping purpose)
        '''
        self._id = id
        self.category = category
        self.device = device
        # marker associated with this person.
        self.marker = Marker()
        # whether this person is present in the scene
        self.present = False
        # This the person this percon is currently facing at. 
        # 0 means facing at no one
        self.facing = 0

    def has_device(self):
        '''
        Returns true if this person has device
        return false if doesn't
        '''
        if self.device:
            return True
        else:
            return False

    def set_facing(self, id):
        '''
        Update who this person is facing at
        id: ID of the person this person is facing at
        '''
        self.facing = id
    
    def set_presence(self, presence):
        self.present = presence

    def is_facing(self, target):
        """
        Check if this person is facing the target person
        """
        if self.marker.is_facing(target.marker.get_location()):
            return True
        return False
    
    def get_facing(self):
        '''
        Returns the id of person this person is facing at
        '''
        return self.facing
    
    def get_id(self):
        '''
        Returns the id of this participant
        '''
        return self._id
    
    def get_commonality(self, target_category):
        '''
        Returns the signal strength 
        '''
        
        if target_category == self.category:
            return 1
        else:
            return 0



