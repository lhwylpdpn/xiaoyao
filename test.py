#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
import time
import types
import os
import datetime
path='/image_levelup/'
if not os.path.exists(path):
	os.mkdir(path)
device=mr.waitForConnection() 
if not device:
    print("Please connect a device to start!")
  
else:
    print("Device Connected successfully!")
time.sleep(3)
eDevice=EasyMonkeyDevice(device)
hViewer = device.getHierarchyViewer()
def login_vivo():
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
	device.type('13794901454')
	#输入密码
	v=hViewer.findViewById('id/content').children[0].children[2]
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	for x in xrange(1,20):
		device.press("KEYCODE_DEL",md.DOWN)
	device.type('tscr0093')
	#登录
	v=hViewer.findViewById('id/account_login')
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	while hViewer.findViewById('id/account_login'):

		time.sleep(1)
		device.touch(view.x,view.y,'DOWN_AND_UP')

def logout_vivo():
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
		print(1)
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

def game_login_vivo(number,pwd,server_id):
 
	device.startActivity("com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity")
	time.sleep(2)

	while 1:#捕捉更换账号的地方
		print(1)

		if hViewer.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.vivo.unionsdk.ui.UnionActivity' and  eDevice.visible(By.id('id/0x7f0900c2')):
			device.touch(640,415,'DOWN_AND_UP')
			device.touch(640,415,'DOWN_AND_UP')
			device.touch(640,415,'DOWN_AND_UP')
			break
	time.sleep(3)
	while 1:#点击退出现有账号
		print(2)
		if hViewer.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.vivo.unionsdk.ui.UnionActivity' and  eDevice.exists(By.id('id/0x7f090185')):
 			print(4444)
			device.touch(490,261,'DOWN_AND_UP')
			break
	time.sleep(3)
	while 1:#输入用户名密码
		print(3)
		if hViewer.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.vivo.unionsdk.ui.UnionActivity' and  eDevice.exists(By.id('id/0x7f090005')):
 			print(555)
 			device.touch(700,298,'DOWN_AND_UP')
			for x in xrange(1,50):
				device.press("KEYCODE_DEL",md.DOWN)
			device.type(str(number))
 			device.touch(700,367,'DOWN_AND_UP')
			for x in xrange(1,50):
				device.press("KEYCODE_DEL",md.DOWN)
			device.type(str(pwd))
 			device.touch(640,444,'DOWN_AND_UP')
			break

	time.sleep(3)

	while 1:#跳过游戏公告 
		print(3335)
		if hViewer.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.vivo.unionsdk.ui.UnionActivity' and  eDevice.exists(By.id('id/content')):
			break
	v=hViewer.findViewById('id/content')
	view=hViewer.getAbsoluteCenterOfView(v.children[0].children[0].children[1])
	v2=hViewer.findViewById('id/content')
	view2=hViewer.getAbsolutePositionOfView(v2)

	v_h=int(v2.height)
	v_w=int(v2.width)
 
	
	display_h=int(device.getProperty('display.height'))
	display_w=int(device.getProperty('display.width'))
 
	device.touch((display_w-v_w)/2+view.x,(display_h-v_h)/2+view.y,'DOWN_AND_UP')

	while 1:#点击进入选取服务器页面
		if hViewer.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity':
			break
	device.touch(640,650,'DOWN_AND_UP')
	time.sleep(3)
	while 1:#打开选服页面
		if hViewer.getFocusedWindowName()=='com.zlongame.fszhs.vivo/com.amazing.flex.GameActivity':
			device.touch(798,563,'DOWN_AND_UP') 
			break	
	time.sleep(3)
	choose_server(int(server_id))
	time.sleep(3)	
	device.touch(640,645,'DOWN_AND_UP') #开始游戏的大按钮

def account_need_createRole():
	for x in xrange(1,10):#创建角色
		device.touch(1100,660,'DOWN_AND_UP')
		time.sleep(1)
	for x in xrange(1,10):#跳过剧情
		device.touch(1130,27,'DOWN_AND_UP')
		time.sleep(1)

	for x in xrange(1,5):#跳过剧情
		device.touch(1135,255,'DOWN_AND_UP')#点击任务
		device.drag((170,565),(40,565),1,1)#拖动下位置，停止任务
		device.touch(65,65,'DOWN_AND_UP')#点击头像
		time.sleep(1)
		device.touch(1050,435,'DOWN_AND_UP')#点击复制roleid
	device.press('KEYCODE_HOME', md.DOWN_AND_UP)
	time.sleep(1)
	v=hViewer.findViewById('id/show_text')
	view=hViewer.getAbsoluteCenterOfView(v)
	device.touch(view.x,view.y,'DOWN_AND_UP')
	time.sleep(1)
	v=hViewer.findViewById('id/editText')
	view=hViewer.getAbsoluteCenterOfView(v)
 
	device.touch(view.x,view.y,md.DOWN)
	time.sleep(2)
	device.touch(view.x,view.y,md.UP)
	device.touch(160,170,'DOWN_AND_UP')
	device.touch(160,170,'DOWN_AND_UP')
	v=hViewer.findViewById('id/editText')
	print(hViewer.getText(v).encode('UTF8'))

def get_exp(number,server_id):

	time.sleep(10)
	device.touch(390,110,'DOWN_AND_UP')	#打开经验邮件
	time.sleep(5)
	device.touch(640,615,'DOWN_AND_UP')#领取经验
	time.sleep(5)
	device.touch(1050,435,'DOWN_AND_UP')
	img=device.takeSnapshot()
	img.writeToFile(path+str(number)+"_"+str(server_id)+"_"+str(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))+".jpg",'jpg')
def game_close_vivo():
	# device.touch(65,65,'DOWN_AND_UP')
	# time.sleep(1)
	# device.touch(655,505,'DOWN_AND_UP')
	# time.sleep(1)
	# device.touch(640,485,'DOWN_AND_UP')	
	device.press("KEYCODE_BACK",md.DOWN_AND_UP)
	time.sleep(1)
	device.touch(546,423,'DOWN_AND_UP')	
def choose_server(serverid):
	server_id=int(serverid)
	server_list_1=(350,575)#顺序第七位，目前是硬核一区
	server_list_2=(350,505)#顺序第六位，目前是硬核二区，以后可能下移
	server_list_3=(350,435)#顺序第五位，目前是硬核三区，以后可能下移
	server_list_4=(350,365)#顺序第四位，目前是硬核四区，以后可能下移
	server_list_5=(350,295)#顺序第三位，目前是硬核五区，以后可能下移
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
		device.touch(server_list_1[0],server_list_1[1],'DOWN_AND_UP')
		time.sleep(3)
		device.touch(server_position[server_id-5][0],server_position[server_id-5][1],'DOWN_AND_UP') 
	if server_id<=4 and server_id>=1:
		device.touch(server_list_1[0],server_list_1[1],'DOWN_AND_UP')
 
		time.sleep(3)
		device.drag(server_position[0],server_position[10],1,1)
		time.sleep(3)
		device.touch(server_position[server_id-1][0],server_position[server_id-1][1],'DOWN_AND_UP') 
		#list2
	if server_id<=32 and server_id>=21:

		device.touch(server_list_2[0],server_list_2[1],'DOWN_AND_UP')
		time.sleep(3)
		device.touch(server_position[server_id-21][0],server_position[server_id-21][1],'DOWN_AND_UP') 
	if server_id<=20 and server_id>=17:
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



if __name__ == '__main__':
	number=[]
	pwd=[]
	server_id=[]
	number.append('13014946429')
	number.append('18392375794')
	number.append('18248499374')
	number.append('18429002416')
	number.append('13058372064')
	number.append('18729247743')
	number.append('13650392137')
	number.append('13537087363')
	number.append('13650493465')

	pwd.append('mrot8089')
	pwd.append('vsbf6803')
	pwd.append('ifyr3667')
	pwd.append('lvkm4613')
	pwd.append('fglo1081')
	pwd.append('icme6690')
	pwd.append('kjat9288')
	pwd.append('dbqw3702')
	pwd.append('cert1391')

	server_id.append(6)
	server_id.append(27)
	server_id.append(42)
	server_id.append(38)
	server_id.append(28)
	server_id.append(36)
	server_id.append(11)
	server_id.append(38)
	server_id.append(46)
	for x in xrange(0,len(number)):
		
		game_login_vivo(number[x],pwd[x],server_id[x])
		get_exp(number[x],server_id[x])
		game_close_vivo()


