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
        self._interests_string = []
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
        # print(self._interests)
        self._interests.append(interest)
    
    def add_interest_string(self, interest):
        self._interests_string.append(interest)
    
    def get_interests(self):
        return self._interests_string.copy()
    
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

        for my_interest in self._interests_string:
            for target_interest in target.get_interests():
                if my_interest == target_interest:
                    # print(f"Interests {my_interest} {target_interest}")
                    strength += 1
        
        return strength

    def get_colour(self):
        '''
        Returns the colour in a form of string
        '''
        colour_string = ""
        colour_string += str(self._interests[2])
        colour_string += str(self._interests[0])
        colour_string += str(self._interests[3])
        colour_string += str(self._interests[1])
        # for interest in self._interests:
        #     colour_string += str(interest)
        return colour_string

    def is_facing_2D(self, target):
        return self.marker.is_facing_2D(target.marker.get_location_2D())
    
