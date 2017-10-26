#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os
import random
import ConfigParser
import subprocess
import time
import base64
import urllib2
import urllib
import json
import re
from sys import argv
import sqlite3
import sys

global APIIP

APIIP="118.190.204.182:5000"


def connect_device():

	info=os.popen('adb connect 127.0.0.1:21503')
	print(info.read())

def start_device():

	pwd=getinfo()

	os.chdir(pwd)
	cmd="MEmuConsole.exe MEmu"

	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)




def close_device():


	cmd="taskkill /f /t /im MEmu*"
	subprocess.call(cmd, shell=True)

def getinfo():

    config = ConfigParser.ConfigParser()
    path = 'conf_menu.conf'
    config.read(path)
    return config.get('MEmu', 'MEmuname')


def getsn():
	sn = 'TlRRMlREVTFRMjg9'
	return sn

def get_request_info():
	global APIIP

	url="http://"+str(APIIP)+"/getinfo?sn="+getsn()+"&username="+argv[1]
	print(url)
	headers=[]
	headers.append(('User-Agent' , '673b34113cbd60dfb16ef9459614fc89_lhwylp'))
	opener = urllib2.build_opener()
	opener.addheaders=headers
	res=opener.open(url)
	updateinfo(res.read())

def get_request_info_API(username):
	global APIIP
	
	url="http://"+str(APIIP)+"/getinfo?sn="+getsn()+"&username="+str(username)
	print(url)
	headers=[]
	headers.append(('User-Agent' , '673b34113cbd60dfb16ef9459614fc89_lhwylp'))
	opener = urllib2.build_opener()
	opener.addheaders=headers
	res=opener.open(url)
	updateinfo(res.read())

def get_plan(channelname,game_id):
	global APIIP
	url="http://"+str(APIIP)+"/getplan?channel_type="+str(channelname)+"&sn="+getsn()+"&game_id="+str(game_id)
	print(url)
	headers=[]
	headers.append(('User-Agent' , '673b34113cbd60dfb16ef9459614fc89_lhwylp'))
	opener = urllib2.build_opener()
	opener.addheaders=headers
	res=opener.open(url)
	res=json.loads(res.read())["body"]
	return res

def write_log(account_id,status,des):
	global APIIP
	url="http://"+str(APIIP)+"/update_status?account_id="+str(account_id)+"&status="+str(status)+"&des="+str(des)
	print(url)
	headers=[]
	headers.append(('User-Agent' , '673b34113cbd60dfb16ef9459614fc89_lhwylp'))
	opener = urllib2.build_opener()
	opener.addheaders=headers
	res=opener.open(url)
	res=json.loads(res.read())["status"]
	return res

def update_sqlite_for_zilong():
	while 1:
		print('waiting for andorid start...')
		cmd='adb pull /data/data/com.android.providers.settings/databases/settings.db'
		
		process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		if process==0:
			break
	conn=sqlite3.connect('settings.db')
	cur=conn.cursor()
	cur.execute("DELETE FROM system where name='cymgdeviceid'")
	conn.commit()
	conn.close()
	while 1:
		print('waiting for andorid start...')
		cmd='adb remount'
		process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		cmd='adb push settings.db /data/data/com.android.providers.settings/databases/'
		process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

		if process==0:
			break		
def updateinfo(jsondata):
	info=json.loads(jsondata)["body"]
	#print(getinfo()+"\MemuHyperv VMs\MEmu\MEmu.memu")

	file=open(getinfo()+"\MemuHyperv VMs\MEmu\MEmu.memu")
	filenode=file.read()
	file.close()
	#filenode.replace('MACAddress="666666666666"','MACAddress="'+info[0]["macaddress"]+'"')
	strinfo=re.compile('MACAddress=\"([^\"]*)\"')
	temp=strinfo.sub('MACAddress="'+info[0]["macaddress"]+'"',filenode)
	strinfo=re.compile('name="hmac" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="hmac" value="'+info[0]["hmac"]+'"',temp)
	strinfo=re.compile('name="imei" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="imei" value="'+info[0]["imei"]+'"',temp)
	strinfo=re.compile('name="imsi" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="imsi" value="'+info[0]["imsi"]+'"',temp)
	strinfo=re.compile('name="linenum" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="linenum" value="'+info[0]["linenum"]+'"',temp)
	strinfo=re.compile('name="microvirt_vm_brand" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="microvirt_vm_brand" value="'+info[0]["microvirt_vm_brand"]+'"',temp)
	strinfo=re.compile('name="microvirt_vm_manufacturer" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="microvirt_vm_manufacturer" value="'+info[0]["microvirt_vm_manufacturer"]+'"',temp)
	strinfo=re.compile('name="microvirt_vm_model" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="microvirt_vm_model" value="'+info[0]["microvirt_vm_model"]+'"',temp)
	strinfo=re.compile('name="operator_network" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="operator_network" value="'+info[0]["operator_network"]+'"',temp)
	strinfo=re.compile('name="resolution_height" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="resolution_height" value="'+info[0]["resolution_height"]+'"',temp)
	strinfo=re.compile('name="resolution_width" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="resolution_width" value="'+info[0]["resolution_width"]+'"',temp)
	strinfo=re.compile('name="simserial" value=\"([^\"]*)\"')
	temp=strinfo.sub('name="simserial" value="'+info[0]["simserial"]+'"',temp)
	file=open(getinfo()+"\MemuHyperv VMs\MEmu\MEmu.memu","w")
	file.write(temp)
	file.close()
def getprop():
	cmd='adb shell getprop wifi.interface.mac'
	print('wifi mac:')
	subprocess.call(cmd, shell=True)
	cmd='adb shell getprop microvirt.imei'
	print('imei:')
	subprocess.call(cmd, shell=True)
	cmd='adb shell getprop microvirt.linenum'
	print('linenum:')
	subprocess.call(cmd, shell=True)
	cmd='adb shell getprop microvirt.simserial'
	print('sn:')
	subprocess.call(cmd, shell=True)
	cmd='adb shell getprop ro.product.brand'
	print('brand:')
	subprocess.call(cmd, shell=True)
	cmd='adb shell getprop ro.product.model'
	print('model:')
	subprocess.call(cmd, shell=True)
def main(user):
	close_device()
	get_request_info_API(user)
	start_device()
	update_sqlite_for_zilong()
	getprop()
if __name__ == '__main__':
	close_device()
	get_request_info()
	start_device()
	update_sqlite_for_zilong()
	getprop()