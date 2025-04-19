
import numpy
import cv2
import imutils
import datetime
# cascade classifier is used to specify the file "xml" where the data is will be used
gun_cascade=cv2.CascadeClassifier('cascade.xml')
# here we are giving video axis to our camara
camera=cv2.VideoCapture(0)
# when the frame will catch some gun it will change some value from none
firstFrame=None
gun_exist=None
# this loop is going to give  infinite loop,because it should run for all the images
while True:
    # the camera is going to read out and detect the gun
    ret,frame=camera.read()
    # resize the function imutils ,my frame to the width of 500
    frame=imutils.resize(frame,width=500)
    #we are converting BGR/RGB image into gray image and also used a color converting function
    # BGR=blue,gree,gray
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gun=gun_cascade.detectMultiScale(gray,1.3,5,minSize=(100,100))
    # condition where if it detects any gun the variable will be true
    if len(gun)>0:
        gun_exist=True
    # the value of the x,y,width,height for gun variable
    for (x,y,w,h) in gun:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

    #setting up a first frame as gray
    if firstFrame is None:
        firstFrame=gray
        continue
    # if the image on the frame is shown it will show the particular string the function
    cv2.imshow("security feed",frame)
    key=cv2.waitKey(1)& 0xFF
    if key==ord('q'):
        break
if gun_exist:
    print("guns detected")
else:
    print("gun didn't detected")

camera.release()
cv2.destroyAllWindows()





