#!/usr/bin/python
# -*- coding: UTF-8 -*- 
from sys import argv
import sys
from com.dtmilano.android.viewclient import ViewClient, View
import re
from com.dtmilano.android.adb.adbclient import AdbClient
import cv2
import numpy as np
import time
import types
import os
import datetime
import subprocess
import threading


global threads
threads=[]
global device
global serialno
global vc
global tag
tag=-1
device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device=device, serialno=serialno)
def step0_game_start():
	#print(vc.IS_FOCUSED_PROPERTY )
	global device
	global serialno
	global vc
	global tag
	try:
		close_game()
		componentName="com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity"
		FLAG_ACTIVITY_NEW_TASK = 0x10000000
		device.startActivity(component=componentName, flags=FLAG_ACTIVITY_NEW_TASK)
		tag=1
	except:
		tag=-1
def step_1_login_game_fs():
	global device
	global serialno
	global vc
	global tag

	if device.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity':
		device.touch(640,650,'DOWN_AND_UP')#进入到主页面2
		time.sleep(3)
		tag=3

def step_2_login_game_fs():
	global device
	global serialno
	global vc
	global tag
	i=0
	while i<=3:
		i+=1
		device.touch(1238,560,'DOWN_AND_UP')#点击切换账号
		vc.dump()
		print(33,vc.findViewById('com.vivo.sdkplugin:id/vivo_login_loading_switch'))

		if   vc.findViewById('com.vivo.sdkplugin:id/vivo_login_loading_switch'):
			
			device.touch(640,415,'DOWN_AND_UP')

		vc.dump()
		print(44,vc.findViewById('com.vivo.sdkplugin:id/sublist_account_exit'))
		if  vc.findViewById('com.vivo.sdkplugin:id/sublist_account_exit'):
			vc.findViewById('com.vivo.sdkplugin:id/sublist_account_exit').touch()
			print(333333)
			tag=4
			return 0
		else:
			device.press('KEYCODE_BACK')

def step_3_change_userinfo_channel_vivo(user,pwd):

	global t_ad_event
	global device
	global serialno
	global vc
	vc.dump()

	if  vc.findViewById('com.vivo.sdkplugin:id/vivo_login_total_layout'):
		print(2)
		vc.findViewById('com.vivo.sdkplugin:id/clean_account_btn').touch()
		device.type(user)
		vc.findViewById('com.vivo.sdkplugin:id/account_password_input').touch()
		device.type(pwd)
		time.sleep(3)
		print(3)
		vc.findViewById('com.vivo.sdkplugin:id/account_login').touch()
		print(4)

	close_ad_channel_vivo(5)

def close_game():
	cmd='adb shell am force-stop com.zlongame.fszhs.vivo'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	cmd='adb shell am force-stop com.vivo.sdkplugin'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def restart_ADB():
	cmd='adb kill-server'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	cmd='adb start-server'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def drag(x,y,x1,y1):
	cmd='adb shell input swipe '+str(x)+' '+str(y)+' '+str(x1)+' '+str(y1)
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def close_ad_channel_vivo(tag_now):
	global t_ad_event
	global device
	global vc	
	global tag
	#print( device.getFocusedWindowName())
	if  device.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity':
		#print(vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_mutitxt_dialog_close'))
		#print(vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_singletxt_dialog_close'))
		if  vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_mutitxt_dialog_close') or vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_singletxt_dialog_close'):
			try:
				if vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_mutitxt_dialog_close').isClickable():
					device.press('KEYCODE_BACK')
					print('close ad success')
					tag=tag_now
				if vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_singletxt_dialog_close').isClickable():							
					device.press('KEYCODE_BACK')
					print('close ad success')
					tag=tag_now
			except:
				pass


			# if device.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and vc.findViewById('com.vivo.sdkplugin:id/vivo_app_exit_dialog_txt_layout'):
			# 	device.press('KEYCODE_BACK')
			# 	print('close esc success')
 		# 		continue;


			# if device.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and  vc.findViewById('com.vivo.sdkplugin:id/vivo_title_bar'):
			# 	device.press('KEYCODE_BACK')
			# 	print('close esc success')
 		# 		continue;

			# global device
			# global eDevice
			# global hViewer
			# print('error 1')

			# print('errror 100')
			# device.shell('killall com.android.commands.monkey')
			# device=mr.waitForConnection() 
			# if not device:
			#     print("Please connect a device to start!")
			  
			# else:
			#     print("Device Connected successfully!")
			# print('error 2')
			# eDevice=EasyMonkeyDevice(device)
			# print('error 3')
			# hViewer = device.getHierarchyViewer()
			# print('error 4')

			# continue;

def Refreshdump():
	global t_ad_event
	global device
	global vc	
	global tag

	try:

		vc.dump()


	except:
		pass
def choose_server(server_id):
	pass


def choose_opencv_init():
	# global t_ad_event
	# global device
	# global serialno
	# global vc	
	# global tag
	menu_start_x=255
	menu_start_y=655
	menu_cont_y=68
	area_1=(menu_start_x,menu_start_y)
	area_2=(menu_start_x,menu_start_y+menu_cont_y)
	area_3=(menu_start_x,menu_start_y+2*menu_cont_y)
	area_4=(menu_start_x,menu_start_y+3*menu_cont_y)
	area_5=(menu_start_x,menu_start_y+4*menu_cont_y)
	area_6=(menu_start_x,menu_start_y+5*menu_cont_y)
	area_7=(menu_start_x,menu_start_y+6*menu_cont_y)


	# vc.dump()
	# drag(350,625,350,100)#整屏幕拖动
	# drag(350,625,350,100)#整屏幕拖动，确保到最底下
	# drag(350,625,350,100)#整屏幕拖动，确保到最底下
	# drag(350,625,350,100)#整屏幕拖动，确保到最底下
	device.takeSnapshot().save('testtt.png', 'PNG')
	img = cv2.imread('testtt.png')
	pic2 = img[20:150, -180:-50]
	cv2.imshow('Detected',pic2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
if __name__ == '__main__':

			tag=5

			
			if tag==-1:
				step0_game_start()
			if tag>=0:
				Refreshdump()
			if tag==1:
				close_ad_channel_vivo(2)
			if tag==2:
				step_1_login_game_fs()
			if tag==3:
				step_2_login_game_fs()
			if tag==4:
				step_3_change_userinfo_channel_vivo(13186783347,'gkbs0257')
			if tag==5:
				choose_opencv_init()
				