import cv2
import threading
import time



open = False
close = False
timer_close = False
def count_close(count):
    global close, timer_close, start
    if(count):
        print("cc")
        if(not close):
           timer_close=True
        if(timer_close):
            start=time.time()
            timer_close=False
        close = True
        
        end=time.time()
        print("time: ", end-start)
    else:
        print("dd")
        close = False
        
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError('cannot open the cam')
while cap:
    ret, frame=cap.read()
    cv2.imshow('test', frame)
    
    
    k=cv2.waitKey(1)
    if k == ord('q'):
        print("close")
        count_close(True)
        #if(not close):
        #    timer_close=True
        #if(timer_close):
        #    start=time.time()
        #    timer_close=False
        #close = True
        
        #end=time.time()
        #print("time = ", end-start)
    elif k == ord('w'):      
        count_close(False)
        #close = False
        print("open")
    elif k == ord('e'):
        break
    
cap.release()
cv2.destroyAllWindows()