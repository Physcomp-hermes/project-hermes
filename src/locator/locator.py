import cv2

markerDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
# this is the detector parameters
markerParams = cv2.aruco.DetectorParameters_create()
cam = cv2.VideoCapture(1)

def main():
    # main for debugging purposes
    print("Loading the camera...\n")
    while(True):
        ret, frame = cam.read()
        
        (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, markerDict, parameters=markerParams)
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        cv2.imshow('frame', frame)
        # print(ids)
        # print(corners)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()

# This is the main file to detect the location of different fiducial markers and their orientations