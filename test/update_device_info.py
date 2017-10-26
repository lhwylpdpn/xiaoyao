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
def randint_num(num):
	r=""
	for x in xrange(0,num):
		r=str(random.randint(0,9))+r
	print(r)
	return r

def setproperty():
	#prop=[]#[imei,imsi,linenum,simserial,pwd,serverid]
	#prop.append([123456789012344,123456789012345,'+8618600547032',12345678901234567890,'mrot8089',6])
	imei=str(randint_num(15))
	imsi=str(randint_num(15))
	linenum=str("+86186"+str(randint_num(8)))
	simserial='89860070200779921015'
	mac=str(mac_rand())
	os.popen('adb shell setprop microvirt.imei '+imei)
	os.popen('adb shell setprop microvirt.imsi '+imsi)
	os.popen('adb shell setprop microvirt.linenum '+linenum)
	os.popen('adb shell setprop microvirt.simserial '+simserial)
	os.popen('adb shell setprop wifi.interface.mac '+mac)
	print(imei)
	print(imsi)
	print(linenum)
	print(simserial)
	print(mac)
if __name__ == '__main__':
	setproperty()