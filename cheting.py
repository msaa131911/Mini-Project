import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

#cap=cv2.VideoCapture(r'E:\ALL_IN_ONE\OPEN CV\video\clip3.mp4')

cap=cv2.VideoCapture(0)

color=(0,255,0)
text="loyal gf"

while True:
    _,frame=cap.read()
    objects=model.predict(frame,verbose=False)
    people=[]
    for object in objects:
        for box in object.boxes:
            #print("box",int(box.cls[0]))
            if int(box.cls[0])==0:
                x1,y1,x2,y2=map(int,box.xyxy[0])
                people.append(x1)
                cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)


    if len(people)==2:
        distance=abs(people[0]-people[1])
        if distance<100:
            color=(0,0,255)
            text="danger"
                     
                     

                #print("person detected",x1,box.xyxy[0])
    cv2.putText(frame,text,(50,40),cv2.FONT_HERSHEY_SIMPLEX,1.4,color,2)
    cv2.imshow("video",frame)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break 
