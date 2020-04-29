#!/usr/bin/env python

import rospy
import cv2
def camera():
	rospy.init_node('camera', anonymous = True)
	rate = rospy.Rate(30)

	vcap = cv2.VideoCapture("http://192.168.2.107:8080/video")
	if not vcap.isOpened():
		return "can not open stream"

		
	while vcap.isOpened():
		ret, frame = vcap.read()
		cv2.imshow('VIDEO', frame)

		# break if pressed any key
		if cv2.waitKey(1) != -1:
			break
	vcap.release()
	cv2.destroyAllWindows()





if __name__ == '__main__':
	try:
		camera()
	except rospy.ROSInterruptException:
		pass

