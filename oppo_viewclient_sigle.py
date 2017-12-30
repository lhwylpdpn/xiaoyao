#coding=utf-8
from sys import argv
import sys
from com.dtmilano.android.viewclient import ViewClient, View
import re
from com.dtmilano.android.adb.adbclient import AdbClient
import time
import types
import os
import datetime
import subprocess


global device
global serialno
global vc
global tag

def init(ser):
	global device
	global serialno
	global vc
	global tag

	tag=-1


	print('init',ser)
	device,serialno = ViewClient.connectToDeviceOrExit(serialno=ser)

	vc = ViewClient(device=device,serialno=serialno)
def step0_game_start(ser,componentName):
	#print(vc.IS_FOCUSED_PROPERTY )
	global device
	global serialno
	global vc
	global tag

	#try:
	close_game(ser,componentName)

	FLAG_ACTIVITY_NEW_TASK = 0x10000000
	device.startActivity(component=componentName, flags=FLAG_ACTIVITY_NEW_TASK)
	tag=1
	#except:
		#tag=-1
def step_1_login_game_fs(componentName):
	global device
	global serialno
	global vc
	global tag

	if device.getFocusedWindowName()==componentName:
		device.touch(640,650,'DOWN_AND_UP')#进入到主页面2----封神
		tag=3


def step_2_login_game_fs():
	global device
	global serialno
	global vc
	global tag
	i=0
	while i<=3:
		i+=1
		device.touch(1238,560,'DOWN_AND_UP')#点击切换账号----封神
		#device.touch(1230,140,'DOWN_AND_UP')#点击切换账号-全民
		#device.touch(1227,146,'DOWN_AND_UP')#点击切换账号-jiuzhou
		vc.dump()
		print(33,vc.findViewById('com.nearme.game.service:id/switch_btn'))

		if   vc.findViewById('com.nearme.game.service:id/switch_btn'):
			
			if  vc.findViewById('com.nearme.game.service:id/switch_btn'):
				vc.findViewById('com.nearme.game.service:id/switch_btn').touch()
				
				


		vc.dump()
		print(44,vc.findViewById('com.nearme.game.service:id/nmgc_switch_account_tx'))

		print(55,vc.findViewById('com.nearme.game.service:id/btn_login'))
		if  vc.findViewById('com.nearme.game.service:id/btn_login') is not None:
			tag=4
			break
		if  vc.findViewById('com.nearme.game.service:id/nmgc_switch_account_tx'):
			vc.findViewById('com.nearme.game.service:id/nmgc_switch_account_tx').touch()

		else:
			device.press('KEYCODE_BACK')

def step_3_change_userinfo_channel_oppo(user,pwd):

	global t_ad_event
	global device
	global serialno
	global vc
	global tag
	vc.dump()
	print("a1",tag)
	if  vc.findViewById('com.nearme.game.service:id/btn_login'):
		
		vc.findViewById('com.nearme.game.service:id/multi_autocomple_text').touch()
		for x in xrange(1,20):
			device.press("KEYCODE_DEL")
		device.type(user)
		vc.findViewById('com.nearme.game.service:id/edit_input_content').touch()
		device.type(pwd)
		time.sleep(1)
		
		vc.findViewById('com.nearme.game.service:id/btn_login').touch()
		time.slee(4)
		if vc.findViewById('com.nearme.game.service:id/btn_login'):
			tag=100
		else:
			tag=5
	
	#close_ad_channel_oppo(5)

def close_game(ser,componentName):
	print('dddd',ser,componentName)
	cmd='adb -s '+str(ser)+' shell am force-stop '+str(componentName.split('/')[0])
	print(cmd)
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	
	cmd='adb -s '+str(ser)+' shell am force-stop com.vivo.sdkplugin'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	print(cmd)
# def restart_ADB():
# 	cmd='adb kill-server'
# 	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# 	cmd='adb start-server'
# 	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def drag(x,y,x1,y1):
	global ser
	cmd='adb -s '+str(ser)+' shell input swipe '+str(x)+' '+str(y)+' '+str(x1)+' '+str(y1)
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def clear(ser,componentName):
	cmd='adb -s '+str(ser)+' shell pm clear '+str(componentName.split('/')[0])
	print(cmd)
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	
def close_ad_channel_oppo(tag_next,comName):
	global t_ad_event
	global device
	global vc   
	global tag
	tag_private=0
	test_count=0
	while test_count<11:
		try:
			vc.dump()
		except:
			pass
		print(test_count,"test_count")
	#	print(device.getFocusedWindowName())
		if  device.getFocusedWindowName()==str(comName.split('/')[0])+"/com.nearme.game.sdk.component.proxy.ProxyActivity" :
			print('d1',vc.findViewById('com.nearme.game.service:id/tips_realname_verify'))	
			print('e1',vc.findViewById('com.nearme.game.service:id/closeBtn'))
 

			try:
                
				if vc.findViewById('com.nearme.game.service:id/tv_get_prize_btn') is not None:
					
						device.press('KEYCODE_BACK')
						print('close ad success3')
						tag_private=1
				if vc.findViewById('com.nearme.game.service:id/closeBtn') is not None:
					
					if vc.findViewById('com.nearme.game.service:id/closeBtn').isClickable():
						device.press('KEYCODE_BACK')
						print('close ad success1')
						tag_private=1
				if vc.findViewById('com.nearme.game.service:id/tips_realname_verify') is not None:				   
					#if vc.findViewById('com.nearme.game.service:id/tips_realname_verifys').isClickable(): 
										
						device.press('KEYCODE_BACK')
						print('close ad success2')
						tag_private=1
				if vc.findViewById('com.nearme.game.service:id/close') is not None:
					#if vc.findViewById('com.nearme.game.service:id/tips_realname_verifys').isClickable(): 
										
						device.press('KEYCODE_BACK')
						print('close ad success4')
						tag_private=1
				if vc.findViewById('com.nearme.game.service:id/get_it') is not None:
					#if vc.findViewById('com.nearme.game.service:id/tips_realname_verifys').isClickable(): 
										
						device.press('KEYCODE_BACK')
						print('close ad success5')
						tag_private=1

			except:
				print('f')
				pass

		else:
			test_count+=1
	if tag_private==1:
		tag=tag_next



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

def main(user_,pass_,ser,comName):
	time.sleep(2)
	print('eeee',ser)
	while 1:
		print('ffff',ser)
		try:

			print(ser)
			init(ser)
			print("test"+ser)
			clear(ser,comName)#清理防止充值的信息
			break;
		except BaseException,e:
			print("error,"+ser)
			print(e.message)
			
	i=0
	while 1:
			
			i+=1
			print(i,tag)

			if tag==-1:
				step0_game_start(ser,comName)
			if tag>=0:
				Refreshdump()
				
			if tag==1:
				close_ad_channel_oppo(2,comName)
			if tag==2:
				step_1_login_game_fs(comName)
			if tag==3:
				step_2_login_game_fs()
			if tag==4:
				step_3_change_userinfo_channel_oppo(str(user_),str(pass_))

			if tag==5:
				close_ad_channel_oppo(6,comName)
			if tag==6:
				return "ok"
			if i>30:
				return tag
			if tag==100:
				return tag
def main_test(user_,pass_,ser):

	# while 1:
		# try:
	init(ser)
			# print("test"+ser)
			#break;
		# except BaseException,e:
			# print("error,"+ser)
			# print(e.message)
			# sys.exit()

	step0_game_start()




if __name__ == '__main__':
		main('18374124604','egtr1463','127.0.0.1:21513','com.zlongame.fs.nearme.gamecenter/com.amazing.flex.GameActivity')
		