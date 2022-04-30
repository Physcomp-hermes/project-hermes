import cv2, os
import numpy as np

from .person import Person

# people_dict = {1:Person(1, True), 2:Person(2,True), 3:Person(3,False)}

# TODO: calibration
class Locator:
    def __init__(self, people_dict):
        '''
        Locator class to update what each people are looking at
        '''
        print("Locator initiated...\n")
        # Marker parameters
        self.marker_size = 0.05
        self.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
        self.aruco_params = cv2.aruco.DetectorParameters_create()
        self.people_dict = people_dict
        # self.marker_dict = {}
        # camera stream that will be used 
        self.cam = cv2.VideoCapture(0)
        self.centres_camera = np.empty((1,))
        # calcualte camera matrix and distortion coefficients
        self.camera_matrix, self.dist_coeffs = calibrate()
    
    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()

    def __update_frame(self):
        '''
        Method to update frame in locator
        Detects and saves corners and ids
        '''
        ret, self.frame = self.cam.read()
        (self.corners, self.ids, self.rejected) = cv2.aruco.detectMarkers(self.frame, self.aruco_dict, parameters=self.aruco_params)    
    
    def process_next_frame(self):
        """
        Update and process the next frame. Doesn't accept marker id 0
        """
        # TODO: Add sampling 
        # Debugging code
        self.__update_frame()
        # display frame for debugging
        display_frame = self.frame.copy()
        # draw detected markers 
        cv2.aruco.drawDetectedMarkers(display_frame, self.corners, self.ids)
        rvecs, tvecs, obj = cv2.aruco.estimatePoseSingleMarkers(self.corners, self.marker_size, self.camera_matrix, self.dist_coeffs)
        for id, person in self.people_dict.items():
            # reset presence value
            person.set_presence(False)
            
        # Note: Marker id 0 doesn't work with np.any
        if np.any(self.ids):

            for i in range(0, len(self.ids)):
                cv2.drawFrameAxes(display_frame, self.camera_matrix, self.dist_coeffs, rvecs[i], tvecs[i],0.1)
                id = self.ids[i][0]
                person = self.people_dict[id]
                # update the location of this marker
                person.marker.update_location(rvecs[i], tvecs[i])
                person.present = True

            self.update_targets()

        # cv2.imshow('frame', display_frame)
    
    def update_targets(self):
        """
        Update who each person is looking at. Only considers participants present in the scene
        """
        for id_subject in self.people_dict:
            # Check for each of the markers. 
            subject = self.people_dict[id_subject]
            if not subject.present:
                continue
            for id_target in self.people_dict:
                target = self.people_dict[id_target]
                
                if id_subject == id_target or not target.present:
                    continue
                if subject.is_facing(target):
                    subject.set_facing(id_target)
                    print(id_subject, " Facing ", id_target)
    
    def run_locator(self):
        
        while True:
            self.process_next_frame()
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break



def calibrate():
    '''
    Calibrate the camera used. Returns camera matrix.   
    Code based on https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/sandbox/ludovic/aruco_calibration_rotation.html
    '''
    print("Calibrating camera.")
    datadir = "./data/"
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
    # aruco_params = cv2.aruco.DetectorParameters_create()
    images = np.array([datadir + f for f in os.listdir(datadir) if f.endswith(".png") ])
    all_corners = []
    all_ids = []
    decimator = 0
    # SUB PIXEL CORNER DETECTION CRITERION
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.00001)
    # Board used for calibration
    board = cv2.aruco.CharucoBoard_create(7,5,1,.8,aruco_dict)

    for im in images:
        # Read image
        frame = cv2.imread(im)
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rej = cv2.aruco.detectMarkers(frame_bw, aruco_dict)

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
    (ret, camera_matrix, dist_coeffs, r_vec, t_vec, std_dev_in, std_dev_ex, per_view_err) = cv2.aruco.calibrateCameraCharucoExtended(
        charucoCorners=all_corners,
        charucoIds=all_ids,
        board=board,
        imageSize=imsize,
        cameraMatrix=camera_matrix_init,
        distCoeffs=dist_coeffs_init,
        flags=flags,
        criteria=(cv2.TERM_CRITERIA_EPS & cv2.TERM_CRITERIA_COUNT, 10000, 1e-9))

    print("Calibration complete")
    return camera_matrix, dist_coeffs


def main(people_dict):
    locator = Locator(people_dict)
    
    while True:
        locator.process_next_frame()
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()

# This is the main file to detect the location of different fiducial markers and their orientations