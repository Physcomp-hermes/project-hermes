import cv2

class Locator:
    def __init__(self, people_list):
        '''
        Locator class to update what each people are looking at
        '''
        print("Locator initiated...\n")
        self.markerDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
        self.markerParams = cv2.aruco.DetectorParameters_create()
        self.people_list = people_list
        self.cam = cv2.VideoCapture(0)
        # self.__update_frame()
    
    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()
        
    def __update_frame(self):
        '''
        Method to update frame in locator
        '''
        ret, self.frame = self.cam.read()
        (self.corners, self.ids, self.rejected) = cv2.aruco.detectMarkers(self.frame, self.markerDict, parameters=self.markerParams)
    
    def show_markers(self):
        '''
        This is like a prototyping function for showing markers
        '''
        self.__update_frame()
        frame = self.frame.copy()
        cv2.aruco.drawDetectedMarkers(frame, self.corners, self.ids)
        # Marker side length in metres.
        marker_len = 0.05
        rvecs, tvecs, obj = cv2.aruco.estimatePoseSingleMarkers(self.corners, marker_len, self.camera_matrix, self.dist_coeffs)
        
        rod = np.zeros((3,3))
        if np.any(self.ids):
            # print(len(self.ids))
            # rvecs = rvecs / math.pi * 180 
            for i in range(0, len(self.ids)):
                print("ID: ", self.ids[i])
                print("corners: ", self.corners[i])
                cv2.Rodrigues(rvecs[i], rod)
                # print("R: {0}", rvecs[i]/ math.pi * 180)
                # print("T: {0}", tvecs[i])
                # print("Rod: ", rod)
                # X: Red, Y: Green, Z: Blue
                cv2.drawFrameAxes(frame, self.camera_matrix, self.dist_coeffs, rvecs[i], tvecs[i], 0.1)
        cv2.imshow('frame', frame)
    
    # The top side of the marker is considered 'front'
    # def check_marker_facing(self):


    

# Get rotation and translation matrix to mpa them inside the coordinate system
# Use this to draw a line, see if it goes pass the square that was inputted 
# Simplest thing is to just to calcuate the coordinates then 

def main():
    locator = Locator([])
    while True:
        locator.show_markers()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == "__main__":
    main()

# This is the main file to detect the location of different fiducial markers and their orientations