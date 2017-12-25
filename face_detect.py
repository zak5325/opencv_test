import numpy as np
import cv2
import os
test='image'
os.makedirs(test)
os.chdir(os.getcwd()+'/'+test)
c=1
face_cascade=cv2.CascadeClassifier('/Users/lirt/workspace/opencv_test/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
	ret, frame = cap.read()

	#frame stands for you get the next frame from cap.read function with the camera
	#ret stands for true or flase, for checking whether the frame can get value or not 
	faces=face_cascade.detectMultiScale(frame,1.3,5)
	#detect the picture with face_cascade model with 1.3 stands for scaleFactor and 5 stands for minNeighbors
	#scalefactor:Detection of particle size.The larger the value,the faster the detection speed, but the less accurate.
	#minNeighbors:The detected number of detected frames
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imwrite(str(c)+'.jpg',frame)
		c=c+1
		#deploy a rectangle with (x,y) to (x+w,y+h) size's,and color(255,0,0),2 stands for thickness of that rectangle
	cv2.imshow('frame',frame)
	#show what camera get and the rectangle you put etc.
	if cv2.waitKey(1) & 0xFF == ord('q'):  #press q to exit
		break
cap.release()
cv2.destroyAllWindows()
#release the memory and destory the windows which cv2 show