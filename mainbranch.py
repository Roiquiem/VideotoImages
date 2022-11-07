
#import relevant libraries
import cv2 as cv

def extractFrames(videoPath, desiredPath, intervalInSeconds):
    count = 0
    cap = cv2.VideoCapture(videoPath)
    success, frame = cap.read()
    success = True
    while success:
        cap.set(cv2.CAP_PROP_POS_MSEC, count*1000*intervalInSeconds)
        success, frame = cap.read()
        print("read a new frame: ", success)
        cv2.imwrite(desiredPath + "\\frame%d.jpg" % count, frame)
        count = count + 1
        
# videoPath = the path of the video
# desiredPath = the path of the directory where you want your images to be saved in
# intervalInSeconds = the time interval between saved frames, in seconds  
