#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import cv2
import tello_new as tello
import threading
import time


def control1():
	###########################
	#开发使用,加入你自己的代码
	###########################
	
	#drone.send_command("ap jz jiangzhuo123")#这里单独运行ap指令然后重启飞机
	
	drone1.send_command("takeoff")
	time.sleep(3)
	drone1.send_command("up 25")
	drone1.send_command("stop")
	time.sleep(3)
	drone1.send_command("curve 60 60 0 0 120 0 20")
	drone1.send_command("cw 360")
	drone1.send_command("flip b")
	drone1.send_command("curve -60 -60 0 0 -120 0 20")
	drone1.send_command("flip f")
	drone1.send_command("land")
	
def control2():
	###########################
	#开发使用,加入你自己的代码
	###########################
	
	#drone.send_command("ap jz jiangzhuo123")
	
	drone2.send_command("takeoff")
	time.sleep(3)
	drone2.send_command("up 25")
	drone2.send_command("stop")
	time.sleep(3)
	drone2.send_command("curve 60 60 0 0 120 0 20")
	drone2.send_command("cw 360")
	drone2.send_command("flip b")
	drone2.send_command("curve -60 -60 0 0 -120 0 20")
	drone2.send_command("flip f")
	drone2.send_command("land")
	
	#print drone.send_command("battery?")
	#print drone.send_command("sn?")
	#print drone.send_command("sdk?")
	#drone.send_command("go 0 0 25 10")


drone1= tello.Tello('', 8888,tello_ip='192.168.43.8')#四个参数必须不能一样，tello_ip通过链接的路由器来查看
drone2= tello.Tello('', 8887,tello_ip='192.168.43.175',local_video_port=22222,local_state_port=12345)
con_thread1 = threading.Thread(target=control1)
con_thread1.start()
con_thread2 = threading.Thread(target=control2)
con_thread2.start()
try:
	while True:
		pass
except KeyboardInterrupt:
	pass

