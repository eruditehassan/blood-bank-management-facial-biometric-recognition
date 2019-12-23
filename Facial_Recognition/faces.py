import cv2
import pickle

def facial_recognition():
    return_name = ""
    face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")
    labels = {}
    with open("labels.pickle","rb") as f:
        labels_in = pickle.load(f)
    labels = {y:x for x,y in labels_in.items()}
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for a,b,c,d in faces:
            roi_gray = gray[b:b+d,a:a+c]
            roi_color = frame[b:b+d,a:a+c]
            #print(a,b,c,d)
            id_,conf = recognizer.predict(roi_gray)
            if conf>=45 and conf<=75:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_COMPLEX
                name = labels[id_]
                return_name = name
                color = (255,255,255)
                stroke = 2
                cv2.putText(frame, name, (a,b),font,1,color,stroke,cv2.LINE_AA)

            img = "currentImage.png"
            cv2.imwrite(img,roi_color)
            color = (255,0,0)
            stroke = 2
            cv2.rectangle(frame,(a,b),(a+c,b+d),color,stroke)
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            return return_name
            break
    #cap.release()
    #cap.destroyAllWindows()
facial_recognition()