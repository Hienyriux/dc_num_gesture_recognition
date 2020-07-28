# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:59:00 2020

@author: Lenovo
"""

import socket
import numpy as np
import cv2 as cv

#host = socket.gethostname()
#ip = socket.gethostbyname(host)

def nothing(x):
	pass

# 请换成你的无线局域网IP
ip_port = ('192.168.0.77', 8800)

while True:
	
	s = socket.socket()
	s.bind(ip_port)
	s.listen(1)
	conn, addr = s.accept()
	print('Connected by', addr)
	file_data = bytes()
	while True:
		data = conn.recv(1024)
		if not data: break
		file_data += data
	if len(file_data) < 64:
		conn.close()
		s.close()
		break
	
	with open('recv.jpg', 'wb') as frecv:
		frecv.write(file_data)
	
	frame = cv.imread('recv.jpg')
	cv.imshow('original', frame)
	
	frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	channels = cv.split(frame)
	frame = channels[0]
	
	frame = cv.medianBlur(frame, 11)
	
	min_val = 3
	max_val = 20
	frame = cv.inRange(frame, min_val, max_val)
	
	kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
	frame = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
	
	contours, hierachy = cv.findContours(frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
	draw = np.zeros(shape = frame.shape, dtype = np.uint8)
	
	max_area = 0
	idx = 0
	for i, cur in enumerate(contours):
		cur_area = cv.contourArea(cur)
		if cur_area > max_area:
			max_area = cur_area
			idx = i
	draw = cv.drawContours(draw, contours[idx], -1, 255)
	
	mycontour = contours[idx]
	mmt = cv.moments(mycontour, True)
	mc_x = round(mmt['m10'] / mmt['m00'])
	mc_y = round(mmt['m01'] / mmt['m00'])
	cv.circle(draw, (mc_x, mc_y), 8, 255, 3)
	
	max_dis = 0
	cnt = 0
	idx = 0
	finger_tips = []
	interval = 160
	x_off = 50
	
	for i in range(len(mycontour)):
		cur_x = mycontour[i][0][0]
		cur_y = mycontour[i][0][1]
		dis = (cur_x - mc_x) * (cur_x - mc_x) + (cur_y - mc_y) * (cur_y - mc_y)
		if dis > max_dis:
			max_dis = dis
			idx = i
		if dis != max_dis:
			cnt += 1
			if cnt > interval:
				cnt = 0
				max_dis = 0
				diff_too_small = False
				if mycontour[idx][0][1] > mc_y:
					continue
				for ft in finger_tips:
					if abs(mycontour[idx][0][0] - ft[0]) < x_off:
						diff_too_small = True
						break
				if not diff_too_small:
					finger_tips.append(mycontour[idx][0])
	
	max_dis = max([(ft[0] - mc_x) * (ft[0] - mc_x) + (ft[1] - mc_y) * (ft[1] - mc_y) for ft in finger_tips])	
	threshold = max_dis // 2
	finger_tips = list(filter(lambda x : (x[0] - mc_x) * (x[0] - mc_x) + (x[1] - mc_y) * (x[1] - mc_y) >= threshold, finger_tips))
	for ft in finger_tips:
		cv.circle(draw, (ft[0], ft[1]), 6, 255, 3)
		cv.line(draw, (mc_x, mc_y), (ft[0], ft[1]), 255, 1)
	
	cv.imshow('result', draw)
	
	res = len(finger_tips)
	if res == 0:
		res = 1
	elif res > 5:
		res = 5
	
	conn.send(bytes(str(res) + '\n\0', 'ascii'))
	conn.close()
	s.close()
	
	cv.waitKey(1)

cv.destroyAllWindows()



