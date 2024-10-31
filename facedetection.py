import cv2

#loading pre trained data from opencv
trained_face_data = cv2.CascadeClassifier(r" haarcascadefrontl.xml")

#detecting face with camera
#detecting faces in real time
webcam = cv2.VideoCapture(0)

#looping in video stream to keep detection working
while True:
  succesful_frame_read, frame = webcam.read()

  #graysale convertion
  gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  #detecting face in image
  face_coordinates = trained_face_data.detectMultiScale(frame)

  #drawing the rectangle on image
  for (x,y,w,h) in face_coordinates:
   
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
  cv2.imshow('camera face detection',frame) 
  key=cv2.waitKey(1)
  #quitting the program by pressing Q
  if key== 81 or key== 113:
    break  

#Release video capture object
webcam.release()
