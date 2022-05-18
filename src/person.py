from turtle import color
from .marker import Marker
# This is the class for each person during the event
# This class is used to store the information of people in the event.

class Person:
    def __init__(self, id):
        '''
        Initialise the person class
        id: ID of this person
        category: category (for prototyping purpose)
        '''
        self._id = id
        # list that stores interests. This would need to be modified
        self._interests = []
        # marker associated with this person.
        self.marker = Marker()
        # whether this person is present in the scene
        self.present = False
        # This the person this percon is currently facing at. 
        # 0 means facing at no one
        self.facing = 0
        # vibration strength
        self.vib_strength = 0
        

    def get_facing(self):
        '''
        Returns the id of person this person is facing at
        '''
        return self.facing

    def set_facing(self, target):
        '''
        Update who this person is facing at. Skip still looking at same person
        target: Person object this person is facing at

        '''
        prev_face = self.facing
        if prev_face == target.get_id():
            return
        else:
            self.facing = target.get_id()
            self.vib_strength = self.calc_strength(target)
    
    def set_presence(self, presence):
        self.present = presence

    def is_facing(self, target):
        """
        Check if this person is facing the target person
        """
        return self.marker.is_facing(target.marker.get_location())
    
    def update_facing(self, target):
        """
        Check if this person is currently facing the target
        """
        if self.marker.is_facing(target.marker.get_location()):
            pass
        else:
            print("Not facing target marker")
    
    def get_id(self):
        '''
        Returns the id of this participant
        '''
        return self._id
    
    def add_interest(self, interest):
        self._interests.append(interest)
    
    def get_interests(self):
        return self._interests.copy()
    
    def get_strength(self):
        return self.vib_strength
    
    def calc_strength(self, target):
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

    def get_colour(self):
        '''
        Returns the colour in a form of string
        '''
        colour_string = ""
        for interest in self._interests:
            colour_string += str(interest)
        return colour_string
