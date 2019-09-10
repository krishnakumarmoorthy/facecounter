import cv2 as cv
import numpy as np
# trained file
face_training = cv.CascadeClassifier('training-image/haarcascade_frontalface_default.xml')
# Read input file
img = cv.imread('training-image/1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_training.detectMultiScale(gray, 1.3, 5)
count=len(faces)
li=[]
for x,y,w,h in faces:
	li.append(x)
li=sorted(li)
i=0
x1=0
x2=0
y1=0
y2=0
for x,y,w,h in faces:
	if(x==li[1]):
		li=[]
		x1 = faces[i][0]
		y1 = faces[i][1]
		x2 = faces[i][0] + faces[i][2]
		y2 = faces[i][1] + faces[i][3]
		li.append(x)
		li.append(y)
		li.append(w)
		li.append(h)
		break	
	i+=1
cv.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
cv.imwrite("my.png",img)
cv.imshow("lalala",img)
output = str(count) + "\n" + str(li)
fil = open("output.txt","w")
fil.write(output)
print(output)
fil.close()
