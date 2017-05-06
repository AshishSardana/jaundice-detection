
# Required modules
import cv2
import numpy
from colorthief import ColorThief

# Constants for finding range of skin color in YCrCb
min_YCrCb = numpy.array([0,133,77],numpy.uint8)
max_YCrCb = numpy.array([255,173,127],numpy.uint8)


# Create a window to display the camera feed
cv2.namedWindow('Camera Output')

# Get pointer to video frames from primary device
# videoFrame = cv2.VideoCapture(0)

# Process the video frames
keyPressed = -1 # -1 indicates no key pressed

while(keyPressed < 0): # any key pressed has a value >= 0

    # Grab video frame, decode it and return next video frame
    # readSucsess, sourceImage = videoFrame.read()
    sourceImage = cv2.imread('try.jpg')
    # print sourceImage.shape
    
    # Convert image to YCrCb
    imageYCrCb = cv2.cvtColor(sourceImage,cv2.COLOR_BGR2YCR_CB)

    # Find region with skin tone in YCrCb image
    skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

    #Morphology
    #se = numpy.ones((1,1), dtype='uint8')
    #image_close = cv2.morphologyEx(skinRegion, cv2.MORPH_CLOSE, se)
    #cv2.imshow('camera_ouput', image_close)
    #cv2.waitKey(0)  

    # Do contour detection on skin region
    contours, hierarchy = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contour on the source image
    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        if area > 1000:
            cv2.drawContours(sourceImage, contours, i, (0, 255, 0), 3)

    # Display the source image
    cv2.imshow('Camera Output',sourceImage)
    color_thief = ColorThief('try.jpg')
    
    dominant_color = color_thief.get_color(quality=1)
    print dominant_color

    # Check for user input to close program
    keyPressed = cv2.waitKey(2) # wait 2 millisecond in each iteration of while loop

# Close window and camera after exiting the while loop
cv2.destroyWindow('Camera Output')
videoFrame.release()
