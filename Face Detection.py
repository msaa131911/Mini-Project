import cv2

model = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #images are converted to gray
    faces = model.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.putText(frame, 'alif', (x, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
webcam.release()
cv2.destroyAllWindows()