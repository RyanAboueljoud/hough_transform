import cv2  # Import openCV
import numpy as np

# Select Camera Device
cap = cv2.VideoCapture(0)   # Input device ID: 0-3

print("Press esc to Quit")

if cap.isOpened():
    # Read in a new video frame
    success, img = cap.read()
    img = cv2.resize(img, (480, 240))
    img_lines = img.copy()

    # Convert to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the edges in the image using canny detector
    edges = cv2.Canny(gray, 50, 200)

    hough_lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, 
                                  threshold=30, minLineLength=5,
                                  maxLineGap=6)

    if hough_lines is not None:
        for line in hough_lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img_lines, (x1,y1), (x2,y2), (0,255,0), 3)

    cv2.imshow("Original Image", img)
    cv2.imshow("Gray Image", gray)
    cv2.imshow("Detected Edges", edges)
    cv2.imshow("Hough Lines", img_lines)

cv2.waitKey(0)
cap.release()   # Release camera


