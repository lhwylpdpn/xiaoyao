#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os
import random

def open_device():

	info=os.popen('adb connect 127.0.0.1:21513')
	print(info.read())
def mac_rand():
	Maclist=[]
	for i in range(1,7):
		RANDSTR = "".join(random.sample("0123456789ABCDEF",2))
		Maclist.append(RANDSTR)
	RANDMAC = ":".join(Maclist)
	print RANDMAC
def setproperty(prop):
	#prop=[]#[imei,imsi,linenum,simserial,pwd,serverid]
	#prop.append([123456789012344,123456789012345,'+8618600547032',12345678901234567890,'mrot8089',6])

	os.popen('adb shell setprop microvirt.imei '+str(prop[0][0]))
	os.popen('adb shell setprop microvirt.imsi '+str(prop[0][1]))
	os.popen('adb shell setprop microvirt.linenum '+str("+86"+prop[0][2]))
	os.popen('adb shell setprop microvirt.simserial '+str(prop[0][3]))
	#os.popen('adb shell setprop wifi.interface.mac '+str(mac_rand()))