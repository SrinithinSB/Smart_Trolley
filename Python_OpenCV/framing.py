import cv2
import numpy as np
import serial
import time



######### SERIAL CONNECTION  ###############

ser=serial.Serial(port='COM4',baudrate=9600,timeout=1)
ser.flush()
def write_read(x):
    ser.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
    data = ser.readline()
    return data
#############################################


#############  VIDEO CAPTURING ##############
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap=cv2.VideoCapture(0)
cap.set(3,360)
cap.set(4,110)

_, frame=cap.read()
rows,cols,_=frame.shape
x_medium=int(cols/2)
center=int(cols/2)
position=90

while True:
    _, frame = cap.read()
    hsv_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
    #BLUE_COLOR
    low_blue = np.array([94, 80, 2])
    High_blue = np.array([126, 255, 255])
    blue_mask=cv2.inRange(hsv_frame, low_blue, High_blue)
    contours,hierarchy= cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
    
    ########### TRACKING THE OBJECT #############
    for cnt in contours:
        (x,y,w,h)=cv2.boundingRect(cnt)
        x_medium = int((x+x+w)/2)
        break
    
    #Drawing Line on detected Object
    cv2.line(frame, (x_medium, 0),(x_medium,480),(0,255,0),2)
    cv2.imshow("Frame",frame)
    
    
    key=cv2.waitKey(1)
    
    if key==27:
        break
    
    ##############################################
    
    
    ########### DIRECTION DETECTION ##############
            
    if x_medium < center-55:
        write_read("left\n")  #blue
        print("left")
    elif x_medium >center+55:
        write_read("right\n")  #red
        print("right")
    else:
        write_read("center\n")  #center
        print("center") 
        
    ###############################################      
    
               
cap.release() 
cv2.destroyAllWindows()  