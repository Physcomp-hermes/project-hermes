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
        self.__update_frame()
    
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
        self.__update_frame()
        frame = self.frame.copy()
        cv2.aruco.drawDetectedMarkers(frame, self.corners, self.ids)
        cv2.imshow('frame', frame)

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