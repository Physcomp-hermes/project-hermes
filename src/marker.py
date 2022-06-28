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
        self.width = 0.1
        # angle threshold to determine whether it's facing something or not
        self.face_threshold = 15
        # 3D coordinates
        self.centre_coord = np.zeros(3)
        self.frontal_coord = np.zeros(3)
        # 2D coordinates
        self.frontal_coord_2D = np.zeros(2)
        self.centre_coord_2D = np.zeros(2)
        # frontal vector
        self.vec_front = np.zeros(3)

    
    def __calculate_angle_2D(self, target_coord, extrinsics):
        '''
        calculate the angle by converting it to 2D using given extrinsics
        '''
        # convert coordinates to 2D
        self_2D = self.centre_coord * extrinsics
        target_2D = target_coord * extrinsics
        # Remove height
        # calcuate angle in 2D
        pass
    
    def get_location(self):
        '''
        Getter for centre coordinate of the marker
        '''
        return self.centre_coord
    
    def get_location_2D(self):
        '''
        return centre coordinate in 2D
        '''
        return self.centre_coord_2D
    
    def __calculate_angle(self, coord_target):
        """
        Calculate the angle between the front of the marke and given target coordinate.
        The target coordinate is also in camera coordinate system
        """
        vec_front = np.subtract(self.frontal_coord, self.centre_coord)
        vec_target = np.subtract(coord_target, self.centre_coord)        
        # vec_target = np.transpose(vec_target)
        vec_front = np.transpose(vec_front)
        front_norm = np.linalg.norm(vec_front)
        target_norm = np.linalg.norm(vec_target)
        
        angle_rad = np.arccos(np.dot(vec_front, vec_target) / (front_norm * target_norm))
        angle_deg = angle_rad * 180 / math.pi
        # print("angle")
        # print(angle_deg)
        return angle_deg
    
    def update_location(self, rvec, tvec):
        '''
        Update the locations of the marker using given tvec and rvec.
        tvec: (1x3 2-axis array) transformation vector from marker to camerea coordinate
        rvec: (1x3 2-axis array) rvec used to calculate rotation vector from marker to camera coordinate
        '''
        
        # Calculate projection matrix
        rod, jac = cv2.Rodrigues(rvec)
        tmp_matrix = np.c_[rod, np.matrix.transpose(tvec)]
        extrinsic_matrix = np.r_[tmp_matrix, [[0,0,0,1]]]
        origin = [[0], [0], [0], [1]]
        front = [[0], [0.05], [0], [1]]
        # Update centre coordinate and frontal vector
        self.centre_coord = np.delete(np.matmul(extrinsic_matrix, origin), 3, 0)
        self.frontal_coord = np.delete(np.matmul(extrinsic_matrix, front), 3, 0)
        self.vec_front = np.subtract(self.frontal_coord, self.centre_coord)
        self.vec_front = np.transpose(self.vec_front)

    def update_location_2D(self, rvec, tvec, ref_extrinsic_inv):
        """
        Update the 2D location using given inverse of reference matrix
        """
        # Calculate projection matrix
        rod, jac = cv2.Rodrigues(rvec)
        tmp_matrix = np.c_[rod, np.matrix.transpose(tvec)]
        marker_to_camera = np.r_[tmp_matrix, [[0,0,0,1]]]
        origin = [[0], [0], [0], [1]]
        front = [[0], [0.05], [0], [1]]
        # convert centre coordinate and frontal coordinate
        combined_extrinsic = np.matmul(ref_extrinsic_inv, marker_to_camera)
        centre_coord = np.matmul(combined_extrinsic, origin)
        frontal_coord = np.matmul(combined_extrinsic, front)

        # remove the z coordinate and only save x,y cooridnate
        self.frontal_coord_2D = np.delete(frontal_coord, [2,3], 0)
        
        self.centre_coord_2D = np.delete(centre_coord, [2,3], 0)
        
        
        
    
    def is_facing(self, coordinate):
        '''
        Function to tell if it's facing other marker.
        coordinate: target coordinate to check
        '''
        return self.__calculate_angle(coordinate) < self.face_threshold

    def is_facing_2D(self, coordinate):
        
        return calculate_angle(self.centre_coord_2D, self.frontal_coord_2D, coordinate) < self.face_threshold

def calculate_angle(coord_centre, coord_front, coord_target):
        """
        Calculate the angle between the front of the marke and given target coordinate.
        The target coordinate is also in camera coordinate system
        This is assuming 2D coordinate system
        """
        vec_front = np.subtract(coord_front, coord_centre)
        vec_target = np.subtract(coord_target, coord_centre)        
        vec_front = np.transpose(vec_front)
        front_norm = np.linalg.norm(vec_front)
        target_norm = np.linalg.norm(vec_target)
        angle_rad = np.arccos(np.dot(vec_front, vec_target) / (front_norm * target_norm))
        angle_deg = angle_rad * 180 / math.pi
        # print(f"Angle: {angle_deg}")
        return angle_deg