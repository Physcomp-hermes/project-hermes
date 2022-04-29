import cv2
import numpy as np
import math

class Marker:
    """
    Marker class to contain and process information about each marker
    It uses the coordinate system of the camera
    """
    
    
    def __init__(self):
        # width of the marker in metres
        self.width = 0.05
        # angle threshold to determine whether it's facing something or not
        self.face_threshold = 10
        # centre coordinate 
        self.centre_coord = np.zeros(3)
        # frontal vector
        self.vec_front = np.zeros(3)

    def __calculate_angle(self, target_coord):
        """
        Calculate the angle between the front of the marke and given target coordinate.
        The target coordinate is also in camera coordinate system
        """
        front_norm = np.linalg.norm(self.vec_front)
        target_norm = np.linalg.norm(target_coord)
        angle_rad = np.arccos(np.dot(self.vec_front, target_coord) / (front_norm * target_norm))
        angle_deg = angle_rad * 180 / math.pi
        return angle_deg
    
    def __calculate_vector(self, target_coord):
        '''
        Calculate 3d vector between centre of this marker and target coordinate.
        The target coordinate should be given as camera coordinate 
        returns a 1d array with 3 elements (x,y,z)
        '''
        vec = np.subtract(target_coord, self.centre_coord)
        return np.transpose(vec)

    def get_location(self):
        '''
        Getter for centre coordinate of the marker
        '''
        return self.centre_coord

    def update_location(self, tvec, rvec):
        '''
        Update the locations of the marker using given tvec and rvec.
        tvec: (1x3 2-axis array) transformation vector from marker to camerea coordinate
        rvec: (1x3 2-axis array) rvec used to calculate rotation vector from marker to camera coordinate
        '''
        
        # Calculate projection matrix
        rod, jac = cv2.Rodrigues(rvec)
        tmp_matrix = np.c_[rod, np.matrix.transpose(tvec)]
        extrinsic_matrix = np.r_[tmp_matrix, np.zeros((1,4))]
        origin = [[0], [0], [0], [1]]
        front = [[0], [1], [0], [0]]
        # Update centre coordinate and frontal vector
        self.centre_coord = np.delete(np.matmul(extrinsic_matrix, origin), 3, 0)
        frontal_coord = np.delete(np.matmul(extrinsic_matrix, front), 3, 0)
        self.vec_front = self.__calculate_vector(frontal_coord)
    
    def is_facing(self, coordinate):
        '''
        Function to tell if it's facing other marker.
        coordinate: target coordinate to check
        '''

        return self.__calculate_angle(coordinate) < self.face_threshold


        


