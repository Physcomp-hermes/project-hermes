import cv2, os
from cv2 import Rodrigues
import numpy as np
import math

class Locator:
    def __init__(self, people_list):
        '''
        Locator class to update what each people are looking at
        '''
        print("Locator initiated...\n")
        self.marker_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
        self.marker_params = cv2.aruco.DetectorParameters_create()
        self.people_list = people_list
        self.cam = cv2.VideoCapture(0)
        # Rotation and translation vectors for markers
        self.rvecs = np.zeros(3)
        self.tvecs = np.zeros(3)
        # self.__update_frame()
        self.camera_matrix, self.dist_coeffs = self.calibrate()
    
    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()
        
    def calibrate(self):
        '''
        Calibrate the camera used. Returns camera matrix.   
        Code based on https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/sandbox/ludovic/aruco_calibration_rotation.html
        '''
        print("Calibrating camera.")
        datadir = "../../data/"
        images = np.array([datadir + f for f in os.listdir(datadir) if f.endswith(".png") ])
        all_corners = []
        all_ids = []
        decimator = 0
        # SUB PIXEL CORNER DETECTION CRITERION
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.00001)
        # Board used for calibration
        board = cv2.aruco.CharucoBoard_create(7,5,1,.8,self.marker_dict)

        for im in images:
            # print("Processing image {0}", format(im))
            # Read image
            frame = cv2.imread(im)
            frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners, ids, rej = cv2.aruco.detectMarkers(frame_bw, self.marker_dict)

            if len(corners) > 0:
                # SUB PIXEL DETECTION
                for corner in corners:
                    cv2.cornerSubPix(frame_bw, corner, winSize = (3,3), zeroZone = (-1,-1), criteria = criteria)
                res2 = cv2.aruco.interpolateCornersCharuco(corners,ids,frame_bw, board)
                if res2[1] is not None and res2[2] is not None and len(res2[1])>3 and decimator%1==0:
                    all_corners.append(res2[1])
                    all_ids.append(res2[2])

            decimator+=1

        imsize = frame_bw.shape
        camera_matrix_init = np.array([[ 1000.,    0., imsize[0]/2.],
                                    [    0., 1000., imsize[1]/2.],
                                    [    0.,    0.,           1.]])

        dist_coeffs_init = np.zeros((5,1))
        flags = (cv2.CALIB_USE_INTRINSIC_GUESS + cv2.CALIB_RATIONAL_MODEL + cv2.CALIB_FIX_ASPECT_RATIO)
        #flags = (cv2.CALIB_RATIONAL_MODEL)
        (ret, camera_matrix, dist_coeffs, r_vec, t_vec, std_dev_in, std_dev_ex, per_view_err) = cv2.aruco.calibrateCameraCharucoExtended(
            charucoCorners=all_corners,
            charucoIds=all_ids,
            board=board,
            imageSize=imsize,
            cameraMatrix=camera_matrix_init,
            distCoeffs=dist_coeffs_init,
            flags=flags,
            criteria=(cv2.TERM_CRITERIA_EPS & cv2.TERM_CRITERIA_COUNT, 10000, 1e-9))

        print("Camera matrix:")
        print(camera_matrix)
        return camera_matrix, dist_coeffs


    def __update_frame(self):
        '''
        Method to update frame in locator
        Detects and saves corners and ids
        '''
        ret, self.frame = self.cam.read()
        (self.corners, self.ids, self.rejected) = cv2.aruco.detectMarkers(self.frame, self.marker_dict, parameters=self.marker_params)
        # for set in self.corners:
            # print(set)
    
    def __convert_camera_coordinate(self, coordinate, rvec, tvec):
        '''
        Convert the given 3D local coordinate to 3D coordinate in camera coordinate system
        coordinate: coordinate to be transformed
        rvec: rvec to convert the coordinate
        tvec: tvec to convert the coordinate
        '''
        # calculate rotational matrix
        rod, jac = Rodrigues(rvec)
        tmp_matrix = np.c_[rod, tvec]
        extrinsic_matrix = np.r_[tmp_matrix, np.zeros((1,4))]
        
        return np.matmul(extrinsic_matrix, coordinate)

        
    

    def get_frame(self):
        self.__update_frame()
        return self.frame
    
    
    def show_markers(self):
        '''
        Display markers on the scene
        '''
        self.__update_frame()
        frame = self.frame.copy()
        cv2.aruco.drawDetectedMarkers(frame, self.corners, self.ids)
        # Marker side length in metres.
        marker_len = 0.05
        rvecs, tvecs, obj = cv2.aruco.estimatePoseSingleMarkers(self.corners, marker_len, self.camera_matrix, self.dist_coeffs)
        
        if self.ids != None:
            print(len(self.ids))
            # rvecs = rvecs / math.pi * 180
            for i in range(0, len(self.ids)):
                print("ID: ", self.ids[i])
                print("Corners", self.corners[i])

                cv2.drawFrameAxes(frame, self.camera_matrix, self.dist_coeffs, rvecs[i], tvecs[i], 0.1)
        cv2.imshow('frame', frame)
    
    def test_markers(self):
        
        self.__update_frame()
        frame = self.frame.copy()
        if self.ids != None:
            for id in range(0, len(self.ids)):
                if id == 0:
                    self.__calculate_reverse_projection(self.corners[id])
        cv2.aruco.drawDetectedMarkers(frame, self.corners, self.ids)
        cv2.imshow('frame', frame)
            
    

    

# Get rotation and translation matrix to mpa them inside the coordinate system
# Use this to draw a line, see if it goes pass the square that was inputted 
# Simplest thing is to just to calcuate the coordinates then 

def main():
    # mat = np.ones((3,3))
    # print(mat)
    # mate = np.zeros((3,1))
    # print(mate)
    # com = np.c_[mat, mate]
    # print(com)
    locator = Locator([])
    
    # locator.calibrate()
    while True:
        # locator.test_markers()
        locator.test_markers()

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == "__main__":
    main()

# This is the main file to detect the location of different fiducial markers and their orientations