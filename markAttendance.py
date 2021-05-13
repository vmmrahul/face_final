import cv2
import numpy as np
import face_recognition
import os
from connections import makeConnections
import datetime


path = "Images"
images = []
classNames = []
myList = os.listdir(path)


def getPersionName(id):
    query ="select name from student where id={} ".format(id)
    conn = makeConnections()
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchone()
    return result[0]

def markAttendace(id):
    date = datetime.date.today()
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    query = f"INSERT INTO `Attendance`(`employ`, `dateOfAttendace`, `timeOfRigister`) VALUES ('{id}','{date}','{current_time}')"




for cl in myList:
    curImage = cv2.imread(f'{path}/{cl}')
    images.append(curImage)
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
print("Encoding Complete...")

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    print(success)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faceCurFrame = face_recognition.face_locations(imgS)
    print(faceCurFrame)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDistance)
        if matches[matchIndex]:
            # name = getPersionName(classNames[matchIndex].upper())
            name = 'name'
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            cv2.waitKey(1)

    cv2.imshow('WebCame', img)
    cv2.waitKey(1)
