#!/usr/bin/python
# -*- coding: UTF-8 -*- 
from sys import argv
import sys
from com.dtmilano.android.viewclient import ViewClient, View
import re

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
device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device=device, serialno=serialno)
def game_login_vivo():
	#print(vc.IS_FOCUSED_PROPERTY )
	global device
	global serialno
	global vc
	componentName="com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity"
	FLAG_ACTIVITY_NEW_TASK = 0x10000000
	device.startActivity(component=componentName, flags=FLAG_ACTIVITY_NEW_TASK)


	while 1:

		if not t_ad_event.isSet():

			print(device.isScreenOn())
			# if device.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity':
			# 	device.touch(640,650,'DOWN_AND_UP')#进入到主页面2
			# 	break;
	time.sleep(1)
	change_user_info()
	# close_test()
	# time.sleep(2)

	# while 1:#点击进入选取服务器页面
	# 	if device.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity':
	# 		print(222)
	# 		LOG=LOG+'进入服务器选择页面成功B'+'\n'
	# 		break
	# print(33333)
	# time.sleep(2)
	# device.touch(640,650,'DOWN_AND_UP')

	# print("click fuwuqi ok")
	# time.sleep(2)
	


	# while 1:#捕捉更换账号的地方

	# device.touch(1238,560,'DOWN_AND_UP')#点击切换账号部分
def change_user_info():
	global t_ad_event
	global device
	global serialno
	global vc
	while 1:
			print('ttt')
			if t_ad_event.isSet():
				time.sleep(6)

				device.touch(1238,560,'DOWN_AND_UP')#点击切换账号

				try:
					if device.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and  vc.findViewById('com.vivo.sdkplugin:id/vivo_login_loading_switch'):
						device.touch(640,415,'DOWN_AND_UP')
				
			  		if device.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and  vc.findViewById('com.vivo.sdkplugin:id/sublist_account_exit'):
			 			print(333333)
			 			break;
			 	except:
			 		print('change_user_info error')
			 		continue




def close_test():
	cmd='adb shell am force-stop com.zlongame.fszhs.vivo'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	cmd='adb shell am force-stop com.vivo.sdkplugin'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def restart_ADB():
	cmd='adb kill-server'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	cmd='adb start-server'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def close_vivo_ad():
	global t_ad_event
	global device
	global vc	
	#这个线程负责实时dump
	while 1:
			try:
				try:
					vc.dump()

				except:
					pass


				if  device.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity':
					if  vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_mutitxt_dialog_close') or vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_singletxt_dialog_close'):
						try:
							if vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_mutitxt_dialog_close').isClickable():

								device.press('KEYCODE_BACK')
								print('close ad success')
								t_ad_event.set()
								continue;
							if vc.findViewById('com.vivo.sdkplugin:id/vivo_acts_singletxt_dialog_close').isClickable():
								
								device.press('KEYCODE_BACK')
								print('close ad success')
								t_ad_event.set()
								continue;
						except:
							pass
			except:
				print('close_vivo_ad error')
				continue

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
# def exitGracefully(signum, frame):
# 	global eDevice
# 	global hViewer
# 	global device
# 	signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
# 	device.shell('killall com.android.commands.monkey')
# 	print(333)

# 	print('exitGracefully  error ')
# 	device=mr.waitForConnection() 
# 	if not device:
# 	    print("Please connect a device to start!")
	  
# 	else:
# 	    print("Device Connected successfully!")
# 	print('error 1')

# 	print('errror 100')
# 	print('error 2')
# 	eDevice=EasyMonkeyDevice(device)
# 	print('error 3')
# 	hViewer = device.getHierarchyViewer()
# 	print('error 4')
# 	print('exitGracefully  error ')
def test():
	global t_ad_event
	global device
	global vc	

	while 1:
		vc.dump()
if __name__ == '__main__':
	 #做一个信号标记，一旦出状况就清理掉monkey

	 	for x in xrange(1,2):
	 		print(x)
			t_ad_event = threading.Event() #建立关闭公告的标记事件
			t_main=threading.Thread(target=game_login_vivo)#主线程，进入游戏
			threads.append(t_main)
			t_main.setDaemon(True)
			t_main.start()
			t_ad=threading.Thread(target=close_vivo_ad) #关闭公告的线程
			threads.append(t_ad)
			#t_ad.start() #关闭公告的线程启动的时候，不要用setdaemon


			# t_dump=threading.Thread(target=vcdump) #关闭公告的线程
			# threads.append(t_dump)
			# t_dump.start() #关闭公告的线程启动的时候，不要用setdaemon
			t_main.join()
