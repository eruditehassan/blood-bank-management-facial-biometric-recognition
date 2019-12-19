import os
import cv2
from PIL import Image
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
base = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base,"images")
y_labels = []
x_train = []
id = 0
label_ids = {}
for root, dirs, files in os.walk(image_path):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root,file)
            label = os.path.basename(root).replace(" ","-").lower()

            if not label in label_ids:
                label_ids[label] = id
                id+=1
            id_ = label_ids[label]
            #y_labels.append(label)
            #x_train.append(path)
            #print(label, path)
            pil_image = Image.open(path).convert("L")
            size = (550,550)
            final_image = pil_image.resize(size,Image.ANTIALIAS)
            image_array = np.array(pil_image,"uint8")
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            for x,y,w,h in faces:
                roi = image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
print(label_ids)
with open("labels.pickle", "wb") as f:
    pickle.dump(label_ids,f)

recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainer.yml")