from typing import OrderedDict
import cv2, os
import numpy as np
from scipy import stats 

# people_dict = {1:Person(1, True), 2:Person(2,True), 3:Person(3,False)}

# TODO: calibration
class Locator:
    def __init__(self, people_dict, ui_frame):
        '''
        Locator class to update what each people are looking at
        '''
        print("Locator initiated...\n")
        # Marker parameters
        self.marker_size = 0.1
        self.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
        self.aruco_params = cv2.aruco.DetectorParameters_create()
        self.people_dict = people_dict
        # self.marker_dict = {}
        # camera stream that will be used 
        self.cam = cv2.VideoCapture(0)
        self.centres_camera = np.empty((1,))
        # calcualte camera matrix and distortion coefficients
        self.camera_matrix, self.dist_coeffs = calibrate()

        self.ui_frame = ui_frame
        # cam_width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        # cam_height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # print("camera w: ", cam_width, "h: ", cam_height)
        # self.ui_frame.config(width=cam_width, height=cam_height)

    
    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()

    def __update_frame(self):
        '''
        Method to update frame in locator
        Detects and saves corners and ids
        '''
        ret, self.frame = self.cam.read()
        if ret:
            (self.corners, self.ids, self.rejected) = cv2.aruco.detectMarkers(self.frame, self.aruco_dict, parameters=self.aruco_params)
        else:
            print("Video reading failed")
            
    def __get_facing(self):
        """
        Update who each person is looking at. Only considers participants present in the scene
        returns a dictionary in the form of:
        id: id of target
        """
        facing_dict = {}
        for id_subject in self.people_dict:
            # Check for each of the markers. 
            subject = self.people_dict[id_subject]
            if not subject.present:
                continue
            for id_target in self.people_dict:
                target = self.people_dict[id_target]
                
                if id_subject == id_target or not target.present:
                    continue
                # print(f"Checking {id_subject} and {id_target}")
                if subject.is_facing(target):
                    facing_dict[id_subject] = id_target
                    # print(id_subject, " Facing ", id_target)
                    # subject.set_facing(target)
        return facing_dict

    def __sample_frames(self, frames):
        """
        Sample video frames and return the 'facing' dictionary for people
        present in the scene
        frames: Number of frames to be sampled
        """
        facing_dict = {}
        # list to buffer facing 
        facing_buffer = np.zeros((len(self.people_dict), frames))
        for i in range(frames):
            self.__update_frame()
            rvecs, tvecs, obj = cv2.aruco.estimatePoseSingleMarkers(
                self.corners, self.marker_size, self.camera_matrix, self.dist_coeffs)
            for id, person in self.people_dict.items():
                person.set_presence(False)
            # Note: Marker id 0 doesn't work with np.any
            if np.any(self.ids):
                for j in range(len(self.ids)):
                    id = self.ids[j][0]
                    if id in self.people_dict:
                        person = self.people_dict[id]
                        person.marker.update_location(rvecs[j], tvecs[j])
                        person.set_presence(True)
            
            frame_facing = self.__get_facing()
            for key, value in frame_facing.items():
                facing_buffer[key][i] = value
                
        # print(facing_buffer)
        for key in self.people_dict:
            mode = stats.mode(facing_buffer[key])
            facing_dict[key] = int(mode[0][0])
        # print(facing_dict)
        return facing_dict

    def __process_next_interval(self):
        """
        Update and process the next frame. Doesn't accept marker id 0
        """
        facing_dict = self.__sample_frames(5)
        for id, person in self.people_dict.items():
            if id in facing_dict:
                person.set_facing(self.people_dict[facing_dict[id]])
                
            
            # reset presence value
                
        # facing_dict = self.__sample_frames(5)

        # Debugging code
        # self.__update_frame()
        # display frame for debugging
        display_frame = self.frame.copy()
        # draw detected markers 
        cv2.aruco.drawDetectedMarkers(display_frame, self.corners, self.ids)
        # rvecs, tvecs, obj = cv2.aruco.estimatePoseSingleMarkers(self.corners, self.marker_size, self.camera_matrix, self.dist_coeffs)
        
            
        # Note: Marker id 0 doesn't work with np.any
        # if np.any(self.ids):

        #     for i in range(len(self.ids)):
        #         cv2.drawFrameAxes(display_frame, self.camera_matrix, self.dist_coeffs, rvecs[i], tvecs[i],0.1)
        #         id = self.ids[i][0]
        #         if id in self.people_dict:
        #             person = self.people_dict[id]
        #             # update the location of this marker
        #             person.marker.update_location(rvecs[i], tvecs[i])
        #             # person.present = True

        #     self.__update_targets()
        #     # self.print_strengths()
        # self.print_strengths()
        cv2.imshow('frame', display_frame)
                    
    
    def run_locator(self):
        """
        Run locator. This function calls itself over the main ui window.
        """
        self.__process_next_interval()
        self.print_strengths()
        self.ui_frame.after(100, self.run_locator)
    
    def show_markers(self):
        frame = self.__update_frame()
        cv2.aruco.drawDetectedMarkers(frame, self.corners, self.ids)
        cv2.imshow("Frame", frame)
    
    def print_strengths(self):
        strengths = "[Strengths: "
        facing = "[Facing: "
        for id, person in self.people_dict.items():
            if id == 0:
                continue
            strengths += str(person.get_strength())
            strengths += " | "
            facing += str(person.get_facing())
            facing += " | "
        strengths += " ]"
        facing += " ]"
        # print(strengths)
        print(facing)

            


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


def main():
    people_dict = OrderedDict()
    locator = Locator(people_dict)
    
    while True:
        locator.show_markers()
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()

# This is the main file to detect the location of different fiducial markers and their orientations