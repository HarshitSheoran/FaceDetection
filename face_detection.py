from imutils.video import VideoStream
from imutils import face_utils
import imutils
import dlib
import cv2
import time

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

print("[INFO] camera sensor warming up")
vs = VideoStream(usePiCamera=False).start()
time.sleep(2.0)

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	rects = detector(gray, 0)

	for rect in rects:
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		for (x, y) in shape:
			cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q") or key == 27:
		break

cv2.destroyAllWindows()
vs.stop()