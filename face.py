import cv2 
path = ""
img = cv2.imread(path)
classifier = cv2.CascadeClassifier('haarcascade_frontalface2.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = classifier.detectMultiScale(gray)
print(len(faces))
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
