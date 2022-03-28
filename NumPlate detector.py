import cv2
imgWidth=640
imgHeight=480
NPCascade = cv2.CascadeClassifier("Test\haarcascade_russian_plate_number.xml")
cap=cv2.VideoCapture(0)
cap.set(3,imgWidth)
cap.set(4,imgHeight)
cap.set(10,150)


while True:
    success,img=cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = NPCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in plates:
        area=w*h
        if area>500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 1)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_ITALIC,1,(255,255,0),2)
            imgroi=img[y:y+h,x:x+w]
            cv2.imshow("Number Plate",imgroi)
    cv2.imshow("Number Plate Detected", img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break