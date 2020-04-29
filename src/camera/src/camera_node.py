#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def camera():
	rospy.init_node('camera', anonymous = True)
	rate = rospy.Rate(30)

	vcap = cv2.VideoCapture("http://192.168.2.107:8080/video")
	if not vcap.isOpened():
		return "can not open stream"

	videoRaw = rospy.Publisher('VideoRaw', Image, queue_size = 10)
		
	while vcap.isOpened():

		ret, frame = vcap.read()
		cv2.imshow('VIDEO', frame)
		msg_frame = CvBridge().cv2_to_imgmsg(frame)
		videoRaw.publish(msg_frame)
		cv2.waitKey(1)

	vcap.release()
	cv2.destroyAllWindows()






if __name__ == '__main__':
	try:
		camera()
	except rospy.ROSInterruptException:
		pass

