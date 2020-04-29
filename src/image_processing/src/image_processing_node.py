#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def callback(image):
	msg_frame = CvBridge().imgmsg_to_cv2(image)
	cv2.imshow('ReceivedImage', msg_frame)
	cv2.waitKey(1)

	
def image_processing():
	rospy.init_node('imageProcessing', anonymous = True)
	rospy.Subscriber('VideoRaw', Image, callback)
	rospy.spin()


if __name__ == '__main__':
	image_processing()
