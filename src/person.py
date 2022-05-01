from .marker import Marker
# This is the class for each person during the event

class Person:
    def __init__(self, id, device=False):
        '''
        Initialise the person class
        id: ID of this person
        category: category (for prototyping purpose)
        '''
        self._id = id
        self.device = device
        self._interests = []
        # marker associated with this person.
        self.marker = Marker()
        # whether this person is present in the scene
        self.present = False
        # This the person this percon is currently facing at. 
        # 0 means facing at no one
        self.facing = 0
        # vibration strength
        # self.vib_strength = 0

    def has_device(self):
        '''
        Returns true if this person has device
        return false if doesn't
        '''
        if self.device:
            return True
        else:
            return False

    def get_facing(self):
        '''
        Returns the id of person this person is facing at
        '''
        return self.facing

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
    
    def get_id(self):
        '''
        Returns the id of this participant
        '''
        return self._id
    
    def add_interest(self, interest):
        self._interests.append(interest)
    
    def get_interests(self):
        return self._interests.copy()
    
    def vib_strength(self, target):
        """
        calculate vibration strength between self and given person
        target: a person instance
        """
        strength = 0
        if self._id == target.get_id():
            return strength

        for my_interest in self._interests:
            for target_interest in target.get_interests():
                if my_interest == target_interest:
                    strength += 1
        
        return strength


