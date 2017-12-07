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
import com.android.hierarchyviewerlib.models.ViewNode


global device
global eDevice
global hViewer
global ser

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


def drag(x,y,x1,y1):
	global ser
	cmd='adb -s '+str(ser)+' shell input swipe '+str(x)+' '+str(y)+' '+str(x1)+' '+str(y1)
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def click(x,y):
	global ser

	cmd='adb -s '+str(ser)+' shell input tap '+str(x)+' '+str(y) 
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
def close_game():
	global ser
	cmd='adb -s '+str(ser)+' shell am force-stop com.zlongame.fszhs.vivo'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	cmd='adb -s '+str(ser)+' shell am force-stop com.vivo.sdkplugin'
	process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
def save_html(data):
	file=open("s.txt", "wb")
	file.write(data)
	file.flush()
	file.close()
def choose_junka():
	global device
	global eDevice
	global hViewer
	time.sleep(3)
	v=hViewer.findViewById('id/vivo_personal_vdiamond_item_recharge')
	view=hViewer.getAbsoluteCenterOfView(v)
	click(view.x,view.y)
	
	time.sleep(3)
	v2=hViewer.findViewById('id/content')
	v2=hViewer.getAbsoluteCenterOfView(v2)
	display_h=int(device.getProperty('display.height'))
	display_w=int(device.getProperty('display.width'))
	v=hViewer.findViewById('id/vivo_payment_channel_list').children
	vx=""
	for x in v:
		#print(x)
		for y in x.children:
			#print("y",y)
			for z in y.children:
				#print("z",z)
				if str(hViewer.getText(z))=="骏卡":
					vx=hViewer.getAbsoluteCenterOfView(z)
	print(vx,1)

	if vx=="":
		drag(display_w/2-v2.x+100,display_h/2-v2.y+100,display_w/2-v2.x+100,2000)

		v=hViewer.findViewById('id/vivo_payment_channel_list').children
		for x in v:
			#print(x)
			for y in x.children:
				#print("y",y)
				for z in y.children:
					#print("z",z)
					if str(hViewer.getText(z))=="骏卡":
						vx=hViewer.getAbsoluteCenterOfView(z)

	print(vx,2)
	if vx=="":
		drag(display_w/2-v2.x+100,display_h/2-v2.y+100,display_w/2-v2.x+100,0)
		v=hViewer.findViewById('id/vivo_payment_channel_list').children
		for x in v:
			#print(x)
			for y in x.children:
				#print("y",y)
				for z in y.children:
					#print("z",z)
					if str(hViewer.getText(z))=="骏卡":
						vx=hViewer.getAbsoluteCenterOfView(z)
	print(vx,3)
	if vx=="":
		print('no junka')
		



	click(display_w/2-v2.x+vx.x,display_h/2-v2.y+vx.y)
	print('choose junka',display_w/2-v2.x+vx.x,display_h/2-v2.y+vx.y)
	v=hViewer.findViewById('id/vivo_payment_btn_submit')
	v=hViewer.getAbsoluteCenterOfView(v)
	click(display_w/2-v2.x+v.x,display_h/2-v2.y+v.y)	
def into_recharge():
	global device
	global eDevice
	global hViewer

	click(3,231)
	time.sleep(3)
	click(97,231)
	time.sleep(2)


def insert_money(card_name,card_pwd):
	global device
	global eDevice
	global hViewer

	v=hViewer.findViewById('id/vivo_payment_card_recharge_number')
	v=hViewer.getAbsoluteCenterOfView(v)
	device.touch(v.x,v.y,'DOWN_AND_UP')

	device.type(str(card_name))
	v=hViewer.findViewById('id/vivo_payment_card_recharge_pwd')
	v=hViewer.getAbsoluteCenterOfView(v)
	device.touch(v.x,v.y,'DOWN_AND_UP')
	device.type(str(card_pwd))
	v=hViewer.findViewById('id/vivo_payment_btn_submit')
	v=hViewer.getAbsoluteCenterOfView(v)
	click(v.x,v.y)
	time.sleep(3)
def insert_money_check():
	global device
	global eDevice
	global hViewer
	v=hViewer.findViewById('id/vivo_personal_vdiamond_item_recharge')
	v2=hViewer.findViewById('id/vivo_payment_result_title')
	if v is not None:
		return -1
	elif v2 is not None:
		while 1:
			v2=hViewer.findViewById('id/vivo_payment_result_title')
			time.sleep(1)
			print("ttt")
			print(str(hViewer.getText(v2)))
			if str(hViewer.getText(v2))=='充值成功':
				print('eeee')
				money_insert=str(re.sub("\D","",hViewer.getText(hViewer.findViewById('id/vivo_payment_result_content'))))
				money_balance=str(re.sub("\D","",hViewer.getText(hViewer.findViewById('id/vivo_payment_result_user_balance'))))
				v=hViewer.findViewById('id/vivo_payment_result_btn1')
				v=hViewer.getAbsoluteCenterOfView(v)
				click(v.x,v.y)
				return [money_insert,money_balance]

def test():
	money_insert='3'
	money_balance='4'
	return [money_insert,money_balance]
def save_log(status,name,money,balance):

	file_object = open(os.getcwd()+'/ttt_log.txt','a')
	file_object.write(str(status)+" "+str(name)+" "+str(money)+"" +str(balance))
	file_object.close()
	print("log is write")

def main(use,card,pwd):
	global device
	global eDevice
	global hViewer
	into_recharge()
	choose_junka()
	insert_money(str(card),str(pwd))
	res=insert_money_check()

	if res==-1:
	 	print('error -chongzhi')
	 	save_log('wrong,error',use,card,pwd)
	else:
		print(res)
		save_log('wrong,error',use,res[0],res[1])
if __name__ == '__main__':
	global ser
	ser=sys.argv[3]
	print("into_recharge_pre")
	into_recharge()
	print("into_recharge_next")
	res=sys.argv[1]
	result=""
	user=sys.argv[2]


	device=mr.waitForConnection(10,ser) 
	if not device:
	    print("Please connect a device to start!")
	else:
	    print("Device Connected successfully!")
	

	hViewer = device.getHierarchyViewer()
	res=res.split(",")
	for r in res:
		r=r.split("_")
		print("choose_junka_pre")
		choose_junka()
		print("choose_junka_next")
		print(str(r[0]),str(r[1]))
		time.sleep(3)
		insert_money(str(r[0]),str(r[1]))
		print("eeee")
		result=insert_money_check()
		if result==-1:
	 			print('error -chongzhi')
	 			save_log('wrong,error',user,r[0],r[1])
		else:
				print(result)
				print("card_reacharge_success|"+str(result[0])+"|"+str(result[1])+"|"+str(r[0])+"|"+str(r[1]))
				save_log('success',user,result[0],result[1])
