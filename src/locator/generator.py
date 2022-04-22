import cv2
from cv2 import _OutputArray_DEPTH_MASK_16F
import numpy as np

# The dictionary used to generate markers. 
# 6x6 part specifies resolution of the marker. Smaller the resolution is, it's easier to read
# but has less distance between markers
# the number at the end is the number of markers that could be generated from this dictionary
markerDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)

# path for generated markers to be stored
outputDir = "../../img"

def main():
    """
    This function generates the AruCO markers to be used for the projects.
    saves them in png format.
    """

    generate_board()

def generate_markers():
    marker = np.zeros((300,300,1), dtype="uint8")
    for id in range(10):
        cv2.aruco.drawMarker(markerDict, id, 300, marker, 1)
        outputPath = outputDir + "/marker" + str(id) + ".png"
        cv2.imwrite(outputPath, marker)

def generate_board():
    # cv2.aruco.GridBoard.draw((1000, 1500), board)
    board = cv2.aruco.CharucoBoard_create(7,5,1,.8,markerDict)
    board_img = board.draw((2000,2000))
    outputPath = outputDir + "/board" + ".png"
    cv2.imwrite(outputPath, board_img)

if __name__ == "__main__":
    main()

