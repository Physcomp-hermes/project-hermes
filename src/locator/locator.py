import cv2



def main():
    # main for debugging purposes
    print("Loading the camera...\n")
    markerDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
    # this is the detector parameters
    markerParams = cv2.aruco.DetectorParameters_create()
    cam = cv2.VideoCapture(1)
    while(True):
        
        show_markers(markerDict, markerParams, cam)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

def show_markers(markerDict, markerParams, cam):
    ret, frame = cam.read()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, markerDict, parameters=markerParams)
    cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    cv2.imshow('frame', frame)


if __name__ == "__main__":
    main()

# This is the main file to detect the location of different fiducial markers and their orientations