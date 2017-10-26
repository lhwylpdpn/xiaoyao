#!/usr/bin/python
# -*- coding: UTF-8 -*- 
from sys import argv
import sys
import signal
import re
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
import time
import types
import os
import datetime
import subprocess
import threading

path='/image_levelup/'
path_money='/image_money/'
if not os.path.exists(path):
	os.mkdir(path)
if not os.path.exists(path_money):
	os.mkdir(path_money)


global device
global eDevice
global hViewer
global threads
global t_ad_event
threads = []

device=mr.waitForConnection() 
if not device:
    print("Please connect a device to start!")
  
else:
    print("Device Connected successfully!")
time.sleep(2)
eDevice=EasyMonkeyDevice(device)
hViewer = device.getHierarchyViewer()
global LOG
LOG=" ".join(argv[1:len(argv)])+"\n"
def login_vivo():
	global device
	global eDevice
	global hViewer

		#device.startActivity("com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity")
	device.startActivity("com.vivo.game/com.vivo.game.ui.GameTabActivity")
	time.sleep(3)
	#跳转到我的页面
 
	v=hViewer.findViewById('id/tabs')
	view=hViewer.getAbsoluteCenterOfView(v.children[3])
	device.touch(view.x,view.y,'DOWN_AND_UP')
	#跳转到登录页面
	v=hViewer.findViewById('id/account_login_btn')
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	time.sleep(3)
	#输入用户名
	v=hViewer.findViewById('id/content').children[0].children[1]
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	time.sleep(3)
	for x in xrange(1,20):
		device.press("KEYCODE_DEL",md.DOWN)
	device.type('13650210126')
	#输入密码
	v=hViewer.findViewById('id/content').children[0].children[2]
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	for x in xrange(1,20):
		device.press("KEYCODE_DEL",md.DOWN)
	device.type('ejst8931')
	#登录
	v=hViewer.findViewById('id/account_login')
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	while hViewer.findViewById('id/account_login'):

		time.sleep(1)
		device.touch(view.x,view.y,'DOWN_AND_UP')

def logout_vivo():
	global device
	global eDevice
	global hViewer

	device.startActivity("com.vivo.game/com.vivo.game.ui.GameTabActivity")
	time.sleep(3)
 
	v=hViewer.findViewById('id/tabs')
	view=hViewer.getAbsoluteCenterOfView(v.children[3])
	device.touch(view.x,view.y,'DOWN_AND_UP')
	v=hViewer.findViewById('id/account_nickname')
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	time.sleep(3)
	while eDevice.exists(By.id('id/account_nickname')):
		time.sleep(1)
		device.touch(view.x,view.y,'DOWN_AND_UP')
		print(0)

	while not  eDevice.exists(By.id('id/game_personal_page_account_name')):
		time.sleep(3)
		print('????')
	v=hViewer.findViewById('id/game_personal_page_account_name')
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	while not  eDevice.exists(By.id('id/logout')):
		time.sleep(3)
		print(2)
	v=hViewer.findViewById('id/logout')
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	while not  eDevice.exists(By.id('id/button1')):
		time.sleep(3)
		print(3)	
	v=hViewer.findViewById('id/button1')
	view=hViewer.getAbsoluteCenterOfView(v)
	v2=hViewer.findViewById('id/parentPanel')
	view2=hViewer.getAbsolutePositionOfView(v2)
	ptop=int(v.paddingTop)
	v_h=int(v2.height)
	v_w=int(v2.width)
 
	
	display_h=int(device.getProperty('display.height'))
	display_w=int(device.getProperty('display.width'))
 
	device.touch((display_w-v_w)/2+view.x,(display_h-v_h)/2+ptop+view.y,'DOWN_AND_UP')
	time.sleep(3)

	while eDevice.exists(By.id('id/button1')):
		time.sleep(1)
		device.touch((display_w-v_w)/2+view.x,(display_h-v_h)/2+ptop+view.y,'DOWN_AND_UP')

def vivo_close_gonggao():
	global device
	global eDevice
	global hViewer
	global LOG
	i=0
	time.sleep(2)

	while i<5:#跳过游戏公告 
		print(3335)
		i=i+1
		time.sleep(2)

		print(hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity')
		print(hViewer.visible(hViewer.findViewById('id/vivo_acts_mutitxt_dialog_close')))
		print(hViewer.visible(hViewer.findViewById('id/vivo_acts_singletxt_dialog_close')))
		if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and  (hViewer.visible(hViewer.findViewById('id/vivo_acts_mutitxt_dialog_close')) or hViewer.visible(hViewer.findViewById('id/vivo_acts_singletxt_dialog_close'))):
			
			LOG=LOG+'跳过公告成功'+'\n'
			break

	while 1:
		if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity':
			time.sleep(1)
			if hViewer.visible(hViewer.findViewById('id/vivo_acts_singletxt_dialog_close')):
				v=hViewer.findViewById('id/vivo_acts_singletxt_dialog_close')
			if hViewer.visible(hViewer.findViewById('id/vivo_acts_mutitxt_dialog_close')):
				v=hViewer.findViewById('id/vivo_acts_mutitxt_dialog_close')
			view=hViewer.getAbsoluteCenterOfView(v)
			v2=hViewer.findViewById('id/content')
			view2=hViewer.getAbsolutePositionOfView(v2)

			v_h=int(v2.height)
			v_w=int(v2.width)
		 


			display_h=int(720)#经常读取不到，索性写死
			display_w=int(1280)
		 	print((display_w-v_w)/2+view.x,(display_h-v_h)/2+view.y)
		 	time.sleep(2)
			device.touch((display_w-v_w)/2+view.x,(display_h-v_h)/2+view.y,'DOWN_AND_UP')
		else:
			break
		print(344555)
	time.sleep(1)
	#到这应该跳过了游戏公告
def game_login_vivo():
	global device
	global eDevice
	global hViewer
 	global LOG
 	global t_ad_event
	device.startActivity("com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity")

	while 1:

		if t_ad_event.isSet():
			if hViewer.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity':
				device.touch(640,650,'DOWN_AND_UP')#进入到主页面2
				break;
	time.sleep(3)#进入游戏的两个页面之间的跳转完全不可控

	change_user_info()
	close_test()
	# time.sleep(2)

	# while 1:#点击进入选取服务器页面
	# 	if hViewer.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity':
	# 		print(222)
	# 		LOG=LOG+'进入服务器选择页面成功B'+'\n'
	# 		break
	# print(33333)
	# time.sleep(2)
	# device.touch(640,650,'DOWN_AND_UP')

	# print("click fuwuqi ok")
	# time.sleep(2)
	


	# while 1:#捕捉更换账号的地方

	# 	device.touch(1238,560,'DOWN_AND_UP')#点击切换账号部分
def change_user_info():
	global t_ad_event
	signal.signal(signal.SIGINT, exitGracefully)
	while 1:
		try:
			if t_ad_event.isSet():
				device.touch(1238,560,'DOWN_AND_UP')#点击切换账号



				if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and  hViewer.visible(hViewer.findViewById('id/vivo_login_loading_switch')):
					device.touch(640,415,'DOWN_AND_UP')
			
		  		if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and  hViewer.visible(hViewer.findViewById('id/sublist_account_exit')):
		 			print(333333)
		 			break;



		except:
			print('change_user_info  error ')
			global device
			global eDevice
			global hViewer
			print('error 1')

			print('errror 100')
			device.shell('killall com.android.commands.monkey')
			device=mr.waitForConnection() 
			if not device:
			    print("Please connect a device to start!")
			  
			else:
			    print("Device Connected successfully!")
			print('error 2')
			eDevice=EasyMonkeyDevice(device)
			print('error 3')
			hViewer = device.getHierarchyViewer()
			print('error 4')

			continue;
	# 	print( hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity')
	# 	print( hViewer.visible(hViewer.findViewById('id/sublist_account_exit')))	
	# 	if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and  hViewer.visible(hViewer.findViewById('id/sublist_account_exit')):
 # 			i2=1
	# 		device.touch(490,261,'DOWN_AND_UP')
	# 		LOG=LOG+'退出vivo账号成功'+'\n'
		
	# 	if i1==1 and i2==1:
	# 		break
	# 	else:
	# 		vivo_close_gonggao()
	# while 1:#输入用户名密码
	# 	print(3)
	# 	time.sleep(2)
	# 	if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and  hViewer.visible(hViewer.findViewById('id/account_num_input')):
 # 			print(555)
 # 			device.touch(700,298,'DOWN_AND_UP')
	# 		for x in xrange(1,50):
	# 			device.press("KEYCODE_DEL",md.DOWN)
	# 		device.type(str(number))
 # 			device.touch(700,367,'DOWN_AND_UP')
	# 		for x in xrange(1,50):
	# 			device.press("KEYCODE_DEL",md.DOWN)
	# 		device.type(str(pwd))
 # 			device.touch(640,444,'DOWN_AND_UP')
 # 			LOG=LOG+'重新输入用户名密码成功'+'\n'
	# 		break

	# vivo_close_gonggao()

	# while 1:#打开选服页面
	# 	if hViewer.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity':
	# 		device.touch(798,563,'DOWN_AND_UP') 
	# 		LOG=LOG+'打开选择服务器页面成功'+'\n'
	# 		break	
	# time.sleep(2)
	# choose_server(int(server_id))
	# LOG=LOG+'选择服务器成功'+'\n'
	# time.sleep(2)	
	# device.touch(640,645,'DOWN_AND_UP') #开始游戏的大按钮
	# LOG=LOG+'进入游戏成功'+'\n'
def account_need_createRole():
	global device
	global eDevice
	global hViewer
	global LOG
	for x in xrange(1,10):#创建角色
		device.touch(1100,660,'DOWN_AND_UP')
		time.sleep(1)
	for x in xrange(1,10):#跳过剧情
		device.touch(1130,27,'DOWN_AND_UP')
		time.sleep(1)
	device.touch(895,185,'DOWN_AND_UP')
	for x in xrange(1,5):#跳过剧情
		device.touch(1135,255,'DOWN_AND_UP')#点击任务
		device.drag((170,565),(40,565),1,1)#拖动下位置，停止任务
		device.touch(65,65,'DOWN_AND_UP')#点击头像
		time.sleep(1)
		device.touch(1050,435,'DOWN_AND_UP')#点击复制roleid
	# device.press('KEYCODE_HOME', md.DOWN_AND_UP)
	# time.sleep(1)
	# v=hViewer.findViewById('id/show_text')
	# view=hViewer.getAbsoluteCenterOfView(v)
	# device.touch(view.x,view.y,'DOWN_AND_UP')
	# time.sleep(1)
	# v=hViewer.findViewById('id/editText')
	# view=hViewer.getAbsoluteCenterOfView(v)
	# device.touch(view.x,view.y,'DOWN_AND_UP')
	# for x in xrange(1,50):
	# 	device.press("KEYCODE_DEL",md.DOWN)
	# device.touch(view.x,view.y,md.DOWN)
	# time.sleep(2)
	# device.touch(view.x,view.y,md.UP)
	# device.touch(160,170,'DOWN_AND_UP')
	# device.touch(160,170,'DOWN_AND_UP')
	# v=hViewer.findViewById('id/editText')
	# print(hViewer.getText(v).encode('UTF8'))
	# device.startActivity("com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity")
	# time.sleep(3)
	device.touch(1125,100,'DOWN_AND_UP')	
	# LOG=LOG+'创建角色或者记录ID成功'+' '+str(hViewer.getText(v).encode('UTF8'))+'\n'
def get_exp(number,server_id):
	global device
	global eDevice
	global hViewer

	time.sleep(10)
	device.touch(390,110,'DOWN_AND_UP')	#打开经验邮件
	time.sleep(5)
	device.touch(640,615,'DOWN_AND_UP')#领取经验
	time.sleep(5)
	device.touch(1050,435,'DOWN_AND_UP')
	img=device.takeSnapshot()
	img.writeToFile(path+str(number)+"_"+str(server_id)+"_"+str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))+".jpg",'jpg')
	LOG=LOG+'领取经验成功'+'\n'
def game_close_vivo():
	global device
	global eDevice
	global hViewer
	# device.touch(65,65,'DOWN_AND_UP')
	# time.sleep(1)
	# device.touch(655,505,'DOWN_AND_UP')
	# time.sleep(1)
	# device.touch(640,485,'DOWN_AND_UP')	
	device.press("KEYCODE_BACK",md.DOWN_AND_UP)
	time.sleep(2)
	device.touch(546,423,'DOWN_AND_UP')	
	time.sleep(2)
def choose_server(serverid):
	server_id=int(serverid)
	server_list_4=(350,575)#顺序第七位，
	server_list_5=(350,505)#顺序第六位，
	server_list_6=(350,435)#顺序第五位，
	server_list_7=(350,365)#顺序第四位，
	server_list_8=(350,295)#顺序第三位，

	server_list_1=(350,625)#向上拖动后，第一位置
	server_list_2=(350,555)#向上拖动后，第二位置
	server_list_3=(350,485)#向上拖动后，第三位置

	#每个list有16个server ，但是显示区默认分12个位置
	# 12,11
	# 10,9
	# 8,7
	# 6,5
	# 4,3
	# 2,1
	server_position=[]
	server_position.append((883,615))
	server_position.append((603,615))
	server_position.append((883,530))
	server_position.append((603,530))
	server_position.append((883,445))
	server_position.append((603,445))
	server_position.append((883,360))
	server_position.append((603,360))
	server_position.append((883,275))
	server_position.append((603,275))
	server_position.append((883,200))
	server_position.append((603,200))
 
 
	#最后一组略有位移动，最后这个补齐下
    #list1
	if server_id<=16 and server_id>=5:
		device.drag((350,625),(350,100),1,1) #拖到底，让最底下是硬核一区
		time.sleep(3)
		device.touch(server_list_1[0],server_list_1[1],'DOWN_AND_UP')
 
		time.sleep(3)
		device.touch(server_position[server_id-5][0],server_position[server_id-5][1],'DOWN_AND_UP') 
	if server_id<=4 and server_id>=1:
		device.drag((350,625),(350,100),1,1) #拖到底，让最底下是硬核一区
		time.sleep(3)
		device.touch(server_list_1[0],server_list_1[1],'DOWN_AND_UP')
 
		time.sleep(3)
		device.drag(server_position[0],server_position[10],1,1)
		time.sleep(3)
		device.touch(server_position[server_id-1][0],server_position[server_id-1][1],'DOWN_AND_UP') 
		

		#list2
	if server_id<=32 and server_id>=21:
		device.drag((350,625),(350,100),1,1) #拖到底，让最底下是硬核一区
		time.sleep(3)
		device.touch(server_list_2[0],server_list_2[1],'DOWN_AND_UP')
		time.sleep(3)
		device.touch(server_position[server_id-21][0],server_position[server_id-21][1],'DOWN_AND_UP') 
	if server_id<=20 and server_id>=17:
		device.drag((350,625),(350,100),1,1) #拖到底，让最底下是硬核一区
		time.sleep(3)

		device.touch(server_list_2[0],server_list_2[1],'DOWN_AND_UP')
 
		time.sleep(3)
		device.drag(server_position[0],server_position[10],1,1)
		time.sleep(3)
		device.touch(server_position[server_id-17][0],server_position[server_id-17][1],'DOWN_AND_UP') 

		#list3
	if server_id<=48 and server_id>=37:
		device.touch(server_list_3[0],server_list_3[1],'DOWN_AND_UP')
		time.sleep(3)
		device.touch(server_position[server_id-37][0],server_position[server_id-37][1],'DOWN_AND_UP') 
	if server_id<=36 and server_id>=33:
		device.touch(server_list_3[0],server_list_3[1],'DOWN_AND_UP')
 
		time.sleep(3)
		device.drag(server_position[0],server_position[10],1,1)
		time.sleep(3)
		device.touch(server_position[server_id-33][0],server_position[server_id-33][1],'DOWN_AND_UP') 


		#list4
	if server_id<=64 and server_id>=53:
		device.touch(server_list_4[0],server_list_4[1],'DOWN_AND_UP')
		time.sleep(3)
		device.touch(server_position[server_id-53][0],server_position[server_id-53][1],'DOWN_AND_UP') 
	if server_id<=52 and server_id>=49:
		device.touch(server_list_4[0],server_list_4[1],'DOWN_AND_UP')
 
		time.sleep(3)
		device.drag(server_position[0],server_position[10],1,1)
		time.sleep(3)
		device.touch(server_position[server_id-49][0],server_position[server_id-49][1],'DOWN_AND_UP') 


		#list5
	if server_id<=80 and server_id>=69:
		device.touch(server_list_5[0],server_list_5[1],'DOWN_AND_UP')
		time.sleep(3)
		device.touch(server_position[server_id-69][0],server_position[server_id-69][1],'DOWN_AND_UP') 
	if server_id<=68 and server_id>=65:
		device.touch(server_list_5[0],server_list_5[1],'DOWN_AND_UP')
 
		time.sleep(3)
		device.drag(server_position[0],server_position[10],1,1)
		time.sleep(3)
		device.touch(server_position[server_id-65][0],server_position[server_id-65][1],'DOWN_AND_UP') 


		#list6
	if server_id<=96 and server_id>=85:
		device.touch(server_list_6[0],server_list_6[1],'DOWN_AND_UP')
		time.sleep(3)
		device.touch(server_position[server_id-85][0],server_position[server_id-85][1],'DOWN_AND_UP') 
	if server_id<=84 and server_id>=81:
		device.touch(server_list_6[0],server_list_6[1],'DOWN_AND_UP')
 
		time.sleep(3)
		device.drag(server_position[0],server_position[10],1,1)
		time.sleep(3)
		device.touch(server_position[server_id-81][0],server_position[server_id-81][1],'DOWN_AND_UP') 
		
		#list7
	if server_id<=112 and server_id>=101:
		device.touch(server_list_7[0],server_list_7[1],'DOWN_AND_UP')
		time.sleep(3)
		device.touch(server_position[server_id-101][0],server_position[server_id-101][1],'DOWN_AND_UP') 
	if server_id<=100 and server_id>=97:
		device.touch(server_list_7[0],server_list_7[1],'DOWN_AND_UP')
 
		time.sleep(3)
		device.drag(server_position[0],server_position[10],1,1)
		time.sleep(3)
		device.touch(server_position[server_id-97][0],server_position[server_id-97][1],'DOWN_AND_UP') 
		


def money_insert(money,number,server_id):
	global device
	global eDevice
	global hViewer
	global LOG

	server_position=[]
	server_position.append((420,600)) #左下角第一个 目前30
	server_position.append((950,600)) #右下角第二个 目前6
	server_position.append((420,420)) #中间左 目前198
	server_position.append((950,420)) #中间右 目前98
	server_position.append((420,230)) #上左 目前588
	server_position.append((950,230)) #上右 目前328



	if money==648:

		while 1:

			try:
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[5],server_position[3],1,10)
				time.sleep(1)
				device.drag(server_position[5],server_position[3],1,10)
				time.sleep(3)		
				device.touch(server_position[4][0],server_position[4][1],'DOWN_AND_UP')
				time.sleep(3)
				device.touch(640,510,'DOWN_AND_UP')#标准充值按钮位置

				break
			except:
				print('?')
		time.sleep(3)
		money_pay_V(money,number,server_id)

	if money==328:

		while 1:

			try:
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(3)		
				device.touch(server_position[5][0],server_position[5][1],'DOWN_AND_UP')
				time.sleep(3)
				device.touch(640,510,'DOWN_AND_UP')#标准充值按钮位置
				break
			except:
				print('?')
		time.sleep(3)
		money_pay_V(money,number,server_id)


	if money==588:

		while 1:

			try:
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(3)		
				device.touch(server_position[4][0],server_position[4][1],'DOWN_AND_UP')
				time.sleep(3)
				device.touch(640,510,'DOWN_AND_UP')#标准充值按钮位置
				break
			except:
				print('?')
		time.sleep(3)
		money_pay_V(money,number,server_id)


	if money==98:

		while 1:

			try:
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(3)		
				device.touch(server_position[3][0],server_position[3][1],'DOWN_AND_UP')
				time.sleep(3)
				device.touch(640,510,'DOWN_AND_UP')#标准充值按钮位置
				break
			except:
				print('?')
		time.sleep(3)
		money_pay_V(money,number,server_id)
	if money==30:

		while 1:

			try:
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(3)		
				device.touch(server_position[0][0],server_position[0][1],'DOWN_AND_UP')
				time.sleep(3)
				device.touch(640,510,'DOWN_AND_UP')#标准充值按钮位置
				break
			except:
				print('?')
		time.sleep(3)
		money_pay_V(money,number,server_id)
	if money==198:

		while 1:
			try:
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(3)		
				device.touch(server_position[2][0],server_position[2][1],'DOWN_AND_UP')
				time.sleep(3)
				device.touch(640,510,'DOWN_AND_UP')#标准充值按钮位置
				break
			except:
				print('?')
		time.sleep(3)
		money_pay_V(money,number,server_id)
	if money==6:

		while 1:
			try:
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(1)
				device.drag(server_position[0],server_position[5],1,1)
				time.sleep(3)		
				device.touch(server_position[1][0],server_position[1][1],'DOWN_AND_UP')
				time.sleep(3)
				device.touch(640,510,'DOWN_AND_UP')#标准充值按钮位置
				break
			except:
				print('?')
		time.sleep(3)
		money_pay_V(money,number,server_id)
def money_pay_V(money,number,server_id):
	global device
	global eDevice
	global hViewer
	tag=0
	global LOG
	while 1:
		print("check page ")
		if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and eDevice.exists(By.id('id/vivo_payment_btn_submit')):
			tag=tag+1
			LOG=LOG+'check page'+str(money)+'\n'
			break;
	while 1:
		print('check price ')
		if tag==1 and hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and hViewer.visible(hViewer.findViewById('id/vivo_payment_order_balance')) and  hViewer.visible(hViewer.findViewById('id/vivo_payment_order_price')) and  hViewer.visible(hViewer.findViewById('id/vivo_payment_btn_submit')):
			v=hViewer.findViewById('id/vivo_payment_order_price')
			order_price=hViewer.getText(v)
			v=hViewer.findViewById('id/vivo_payment_order_balance')
			balance_price=hViewer.getText(v)
			print(re.sub("\D","",balance_price))		
			if len(order_price)>0 and len(re.sub("\D","",balance_price))>0:
				LOG=LOG+'check price'+str(money)+'\n'
				tag=tag+10
				break;
	while 1:
		print('check balance,check price')
		print(tag==11)
		print(re.sub("\D","",order_price)==str(money))
		print(balance_price>=re.sub("\D","",order_price))
		if tag==11 and str(re.sub("\D","",order_price))==str(money) and balance_price>=re.sub("\D","",order_price):
			tag=tag+100
			LOG=LOG+'check balance'+str(money)+'\n'
			break;


	while 1:
		print('click insert')
		if  tag==111 and  hViewer.visible(hViewer.findViewById('id/vivo_payment_btn_submit')):
			device.touch(650,435,'DOWN_AND_UP')#标准v钻消费的点击位置
			tag=tag+1000
			LOG=LOG+'点击充值最后一步成功'+str(money)+'\n'
			break

	while 1:
		print('check result')

		if tag==1111 and hViewer.visible(hViewer.findViewById('id/vivo_payment_result_title')) and hViewer.visible(hViewer.findViewById('id/vivo_payment_result_content')) and hViewer.visible(hViewer.findViewById('id/vivo_payment_result_user_balance')) and  hViewer.visible(hViewer.findViewById('id/vivo_payment_result_btn1')):

			v=hViewer.findViewById('id/vivo_payment_result_user_balance')
			balance_price_result=hViewer.getText(v)
			print(re.sub("\D","",balance_price_result))
			v=hViewer.findViewById('id/vivo_payment_result_content')
			order_price_result=hViewer.getText(v)
			#因为礼卷问题暂停
			#if str(re.sub("\D","",order_price_result))==str(money) and int(re.sub("\D","",balance_price_result))+int(re.sub("\D","",order_price_result))==int(re.sub("\D","",balance_price)):
			if 1:
				tag=tag+10000
				print('insert ok')

				img=device.takeSnapshot()
				img.writeToFile(path_money+str(number)+"_"+str(server_id)+"_"+str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))+".jpg",'jpg')
				v=hViewer.findViewById('id/vivo_payment_result_btn1')

				view=hViewer.getAbsoluteCenterOfView(v)
				device.touch(view.x,view.y,'DOWN_AND_UP')
				LOG=LOG+'充值成功'+str(money)+'\n'
				break
def get_balance():
	global device
	global eDevice
	global hViewer
	global LOG

	server_position=[]
	server_position.append((420,600)) #左下角第一个 目前30
	server_position.append((950,600)) #右下角第二个 目前6
	server_position.append((420,420)) #中间左 目前198
	server_position.append((950,420)) #中间右 目前98
	server_position.append((420,230)) #上左 目前588
	server_position.append((950,230)) #上右 目前328



	while 1:
		try:
			device.drag(server_position[0],server_position[5],1,1)
			time.sleep(1)
			device.drag(server_position[0],server_position[5],1,1)
			time.sleep(1)
			device.drag(server_position[0],server_position[5],1,1)
			time.sleep(3)		
			device.touch(server_position[1][0],server_position[1][1],'DOWN_AND_UP')
			time.sleep(3)
			device.touch(640,510,'DOWN_AND_UP')#标准充值按钮位置
			break
		except:
			print('?')
		time.sleep(3)
	while 1:
		if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and hViewer.visible(hViewer.findViewById('id/vivo_payment_order_balance')) and  hViewer.visible(hViewer.findViewById('id/vivo_payment_order_price')) and  hViewer.visible(hViewer.findViewById('id/vivo_payment_btn_submit')):
			v=hViewer.findViewById('id/vivo_payment_order_balance')
			balance_price_result=hViewer.getText(v)
			print(re.sub("\D","",balance_price_result))
			LOG=LOG+'剩余金额'+str(re.sub("\D","",balance_price_result))+'\n'

			break
def money_pay_other():
	return 0

def static_log(name):
	global device
	global eDevice
	global hViewer
	global LOG
	file_object = open(os.getcwd()+'/'+name+'_'+str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))+'_log.csv','w')
	file_object.write(LOG)
	file_object.close()
	print("log is "+name)


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

def threads_test():
	global threads
	t1=threading.Thread(target=ESC_key)
	threads.append(t1)
	t2=threading.Thread(target=game_login_vivo)
	threads.append(t2)	
def ESC_key():
		signal.signal(signal.SIGINT, exitGracefully)
		global edevice

		edevice=EasyMonkeyDevice(device)
		edevice.press('KEYCODE_BACK',md.DOWN_AND_UP)
	
def close_vivo_ad():
	signal.signal(signal.SIGINT, exitGracefully)
	global t_ad_event

		
	while 1:

		try:

			if  hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and  (hViewer.visible(hViewer.findViewById('id/vivo_acts_mutitxt_dialog_close')) or hViewer.visible(hViewer.findViewById('id/vivo_acts_singletxt_dialog_close'))):
				ESC_key()
				print('close ad success')
				t_ad_event.set()
				continue;


			if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and hViewer.visible(hViewer.findViewById('id/vivo_app_exit_dialog_txt_layout')):
				ESC_key()
				print('close esc success')
 				continue;


			if hViewer.getFocusedWindowName()=='com.vivo.sdkplugin/com.vivo.unionsdk.ui.UnionActivity' and hViewer.visible(hViewer.findViewById('id/vivo_title_bar')):
				ESC_key()
				print('close esc success')
 				continue;
		except :

			print('close_vivo_ad  error ')
			global device
			global eDevice
			global hViewer
			print('error 1')

			print('errror 100')
			device.shell('killall com.android.commands.monkey')
			device=mr.waitForConnection() 
			if not device:
			    print("Please connect a device to start!")
			  
			else:
			    print("Device Connected successfully!")
			print('error 2')
			eDevice=EasyMonkeyDevice(device)
			print('error 3')
			hViewer = device.getHierarchyViewer()
			print('error 4')

			continue;
def exitGracefully(signum, frame):
	global eDevice
	global hViewer
	global device
	signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
	device.shell('killall com.android.commands.monkey')
	print(333)

	print('exitGracefully  error ')
	device=mr.waitForConnection() 
	if not device:
	    print("Please connect a device to start!")
	  
	else:
	    print("Device Connected successfully!")
	print('error 1')

	print('errror 100')
	print('error 2')
	eDevice=EasyMonkeyDevice(device)
	print('error 3')
	hViewer = device.getHierarchyViewer()
	print('error 4')
	print('exitGracefully  error ')
if __name__ == '__main__':
	 #做一个信号标记，一旦出状况就清理掉monkey
	 	for x in xrange(1,10):
	 		
			t_ad_event = threading.Event() #建立关闭公告的标记事件
			t_main=threading.Thread(target=game_login_vivo)#主线程，进入游戏
			threads.append(t_main)
			t_main.setDaemon(True)
			t_main.start()
			t_ad=threading.Thread(target=close_vivo_ad) #关闭公告的线程
			threads.append(t_ad)
			t_ad.start() #关闭公告的线程启动的时候，不要用setdaemon
			t_main.join()
