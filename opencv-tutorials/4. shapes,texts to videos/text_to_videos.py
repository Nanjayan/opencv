import cv2
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# properties can be named explicity or
# we can give the number of that property
# frame width - 3 rd property
# frame height - 4th property

cap.set(3,1200)
cap.set(4,700)

print(cap.get(3))
print(cap.get(4))


while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:' + str(cap.get(3)) + ' Height:' + str(cap.get(4))
        frame = cv2.putText(frame,text, (10,50),font,1,(0,255,255),2,cv2.LINE_AA)

        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame,datet, (700,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()