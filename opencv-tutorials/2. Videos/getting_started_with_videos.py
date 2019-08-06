import cv2


#Either we can mention file name in argument 
# or we can specify 0 or -1 for livestream (inbuilt camera)

cap = cv2.VideoCapture(0)

#saving the video to a file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#third argument is Frame per second
# fourth is size of the video 
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1280,720))

#ret will be +ve if frame is available
#frame will capture the frame

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # we can get the properties of the video from cap variable    
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        #video saved in the out variable
        out.write(frame)
        
        # changing from color to grey scale
        gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        # quit the camera by pressing q
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break   

# release the resources
cap.release()
out.realease()


cv2.destroyAllWindows()
