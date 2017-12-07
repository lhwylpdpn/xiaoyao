#coding=utf-8
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


global device
global serialno
global vc
global tag
global ser

def init(ser):
	global device
	global serialno
	global vc
	global tag

	tag=-1


	print('init',ser)
	device,serialno = ViewClient.connectToDeviceOrExit(serialno=ser)

	vc = ViewClient(device=device,serialno=serialno)
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
def Refreshdump():
	global t_ad_event
	global device
	global vc	
	global tag

	try:

		vc.dump()


	except:
		pass


def into_recharge(comName):
	global t_ad_event
	global device
	global vc
	global tag

	click(17,75)
	time.sleep(1)
	click(17,75)
	time.sleep(1)
	try:
		vc.dump()
	except:
		pass
		#点完充值页面的
	if	device.getFocusedWindowName()==str(comName):
			if  vc.findViewById('com.nearme.game.service:id/kebi_charge'):
				print('d1',vc.findViewById('com.nearme.game.service:id/kebi_charge'))	

			try:
				if vc.findViewById('com.nearme.game.service:id/kebi_charge') is not None:
					if vc.findViewById('com.nearme.game.service:id/kebi_charge').isClickable():
						vc.findViewById('com.nearme.game.service:id/kebi_charge').touch()
						tag=1
			except:
				pass
	else:
		print('cant into recharge page')
def choose_junka():
	global t_ad_event
	global device
	global vc
	global tag
	time.sleep(1)
	try:
		vc.dump()
	except:
		pass
	if 	vc.findViewById('com.nearme.atlas:id/tv_show_more'): # 新版本更多支付
		vc.findViewById('com.nearme.atlas:id/tv_show_more').touch()
		print(333)
	if 	vc.findViewById('com.nearme.atlas:id/gg'): # 旧版本更多支付
		vc.findViewById('com.nearme.atlas:id/gg').touch()
		print(333)
	if vc.findViewWithText('游戏点卡'):
		vc.findViewWithText('游戏点卡').touch()
		vc.findViewWithText('立即支付').touch()
		tag=2
def insert_money_pre(price):
	global t_ad_event
	global device
	global vc
	global tag
	time.sleep(1)
	try:
		vc.dump()
	except:
		pass
	if vc.findViewWithText(str(price)):
			vc.findViewWithText(str(price)).touch()
	time.sleep(1)
	if vc.findViewById('com.nearme.atlas:id/btn_bottom'):
			vc.findViewById('com.nearme.atlas:id/btn_bottom').touch()
			tag=3
	if vc.findViewById('com.nearme.atlas:id/f7'):#旧版本
			vc.findViewById('com.nearme.atlas:id/f7').touch()
			tag=3

def insert_money(card_,pwd_):
	global t_ad_event
	global device
	global vc
	global tag

	time.sleep(1)
	try:
		vc.dump()
	except:
		pass
	if vc.findViewById('com.nearme.atlas:id/edit_number') and vc.findViewById('com.nearme.atlas:id/edit_pswd'):
			vc.findViewById('com.nearme.atlas:id/edit_number').touch()
			device.type(card_)
			vc.findViewById('com.nearme.atlas:id/edit_pswd').touch()
			device.type(pwd_)
	if vc.findViewById('com.nearme.atlas:id/btn_bottom'):
			vc.findViewById('com.nearme.atlas:id/btn_bottom').touch()
			tag=4
	if vc.findViewById('com.nearme.atlas:id/bw') and vc.findViewById('com.nearme.atlas:id/bz'):#兼容旧版本
			vc.findViewById('com.nearme.atlas:id/bw').touch()
			device.type(card_)
			vc.findViewById('com.nearme.atlas:id/bz').touch()
			device.type(pwd_)
	if vc.findViewById('com.nearme.atlas:id/f7'):
			vc.findViewById('com.nearme.atlas:id/f7').touch()
			tag=4
def insert_money_check(price):
	global t_ad_event
	global device
	global vc
	global tag
	money_insert=""
	money_balance=""
	time.sleep(1)
	try:
		vc.dump()
	except:
		pass

	if vc.findViewById('com.nearme.atlas:id/tv_result_state') and vc.findViewById('com.nearme.atlas:id/tv_result_state')==vc.findViewWithText('充值成功'):
			if 	vc.findViewById('com.nearme.atlas:id/tv_order_amount')==vc.findViewWithText(str(price)):
				money_insert=str(price)
			while 1:
				if vc.findViewById('com.nearme.atlas:id/btn_bottom'):
					vc.findViewById('com.nearme.atlas:id/btn_bottom').touch()
					
					try:
						vc.dump()
					except:
						pass
					break;


	if vc.findViewWithText('充值成功'):
		money_insert=str(price)
		while 1:
			if 	vc.findViewById('com.nearme.atlas:id/f7') or vc.findViewWithText('完成'):
				if vc.findViewById('com.nearme.atlas:id/f7'):
					vc.findViewById('com.nearme.atlas:id/f7').touch()
					
					try:
						vc.dump()
					except:
						pass
					break;
				if vc.findViewWithText('完成'):
					vc.findViewWithText('完成').touch()
					
					try:
						vc.dump()
					except:
						pass
					break;
	if 	vc.findViewById('com.nearme.game.service:id/kebi_num'):
		money_balance=vc.findViewById('com.nearme.game.service:id/kebi_num').gettext()

		tag=5
		return [money_insert,re.sub("\D","",money_balance)]
	if 	vc.findViewById('com.nearme.game.service:id/kebi_count'):
		money_balance=vc.findViewById('com.nearme.game.service:id/kebi_count').gettext()

		tag=5
		return [money_insert,re.sub("\D","",money_balance)]	
	
def money_import(price,user_,pass_,ser_,comName):
	global tag
	global ser
	ser=ser_
	import_result=[]
	init(ser)
	i=0
	while 1:
			
			i+=1
			print(i,tag)

			if tag==-1:
				into_recharge(comName)
			if tag>=0:
				Refreshdump()
			if tag==1:
				choose_junka()
			if tag==2:
				insert_money_pre(price)
			if tag==3:
				insert_money(str(user_),str(pass_))
			if tag==4:
				import_result=insert_money_check(price)
			if tag==5:
				return import_result
			if i>30:
				return "faild"
if __name__ == '__main__':
	result=money_import('10','1609130298012146','9785100421124445','127.0.0.1:21513','com.pokercity.bydrqp.nearme.gamecenter/com.nearme.game.sdk.component.proxy.ProxyActivity')
	print result