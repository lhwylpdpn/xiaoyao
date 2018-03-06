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
import shutil
global APIIP
global pwd
pwd=os.getcwd()
APIIP="118.190.204.182:5000"


def connect_device(device_url_port):
		print(33333)

		print('waiting for andorid connect...')
		cmd='adb connect '+str(device_url_port)
		
		p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		while  p.poll() is None:
				line=p.stdout.readline()
				line=line.strip()
				print(line)
				if "already connected" in str(line):
					print line
					break


def start_device(memu_name):

	pwd=getinfo()
	if not  os.path.exists(getinfo()+"\MemuHyperv VMs\\"+str(memu_name)+"\\"+str(memu_name)+".memu"):

		#shutil.copyfile(getinfo()+"\MemuHyperv VMs\\"+str(memu_name)+"\\"+str(memu_name)+".memu",getinfo()+"\MemuHyperv VMs\\"+str(memu_name)+"\\"+str(memu_name)+".memu_back")

		shutil.copyfile(getinfo()+"\MemuHyperv VMs\\"+str(memu_name)+"\\"+str(memu_name)+".memu_back",getinfo()+"\MemuHyperv VMs\\"+str(memu_name)+"\\"+str(memu_name)+".memu")

	os.chdir(pwd)
	cmd="MEmuConsole.exe "+str(memu_name)
	print(cmd)
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)




def close_device():


	cmd="taskkill /f /t /im MEmu*"
	subprocess.call(cmd, shell=True)

def getinfo():
	global pwd
	config = ConfigParser.ConfigParser()
	path = 'conf_menu.conf'
	config.read(pwd+"\\"+path)
	print(pwd+"\\"+path)
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
	updateinfo(res.read(),"MEmu")

def get_request_info_API(username,memu_name):
	global APIIP
	
	url="http://"+str(APIIP)+"/getinfo?sn="+getsn()+"&username="+str(username)
	print(url)
	headers=[]
	headers.append(('User-Agent' , '673b34113cbd60dfb16ef9459614fc89_lhwylp'))
	opener = urllib2.build_opener()
	opener.addheaders=headers
	res=opener.open(url)
	updateinfo(res.read(),memu_name)

def get_plan(channelname,game_id):
	global APIIP
	url="http://"+str(APIIP)+"/getplan?channel_type="+str(channelname)+"&sn="+getsn()+"&game_id="+str(game_id)
	print(url)
	headers=[]
	headers.append(('User-Agent' , '673b34113cbd60dfb16ef9459614fc89_lhwylp'))
	opener = urllib2.build_opener()
	opener.addheaders=headers
	res=opener.open(url)
	jsons=json.loads(res.read())
	if jsons["status"]=='200':
		
		res=jsons["body"]
	else:
		res='404'

	return res

def write_log(account_id,status,des):
	global APIIP
	url="http://"+str(APIIP)+"/update_status?account_id="+str(account_id)+"&status="+str(status)+"&des='"+str(des)+"'"
	print(url)
	headers=[]
	headers.append(('User-Agent' , '673b34113cbd60dfb16ef9459614fc89_lhwylp'))
	opener = urllib2.build_opener()
	opener.addheaders=headers
	res=opener.open(url)
	res=json.loads(res.read())["status"]
	return res

def update_sqlite_for_zilong(device_url_port):
	while 1:
		#print('waiting for andorid start step1...')
		cmd='adb  -s '+str(device_url_port)+' pull /data/data/com.android.providers.settings/databases/settings.db'
		
		process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		if process==0:
			break
	conn=sqlite3.connect('settings.db')
	cur=conn.cursor()
	cur.execute("DELETE FROM system where name='cymgdeviceid'")
	conn.commit()
	conn.close()
	while 1:
		#print('waiting for andorid start step2...')
		cmd='adb  -s '+str(device_url_port)+' remount'
		process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		if process==0:
			break
	while 1:
		#print('waiting for andorid start step3...')
		cmd='adb  -s '+str(device_url_port)+' push settings.db /data/data/com.android.providers.settings/databases/'
		process = subprocess.call(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

		if process==0:
			break		
def updateinfo(jsondata,memu_name):
	print(jsondata)
	info=json.loads(jsondata)["body"]
	#print(getinfo()+"\MemuHyperv VMs\MEmu\MEmu.memu")

	file=open(getinfo()+"\MemuHyperv VMs\\"+str(memu_name)+"\\"+str(memu_name)+".memu")
	print(getinfo()+"\MemuHyperv VMs\\"+str(memu_name)+"\\"+str(memu_name)+".memu")
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
	file=open(getinfo()+"\MemuHyperv VMs\\"+str(memu_name)+"\\"+str(memu_name)+".memu","w")
	file.write(temp)
	file.close()
def getprop(device_url_port):
	cmd='adb -s '+str(device_url_port)+' shell getprop wifi.interface.mac'
	print('wifi mac:')
	subprocess.call(cmd, shell=True)
	cmd='adb -s '+str(device_url_port)+' shell getprop microvirt.imei'
	print('imei:')
	subprocess.call(cmd, shell=True)
	cmd='adb -s '+str(device_url_port)+' shell getprop microvirt.linenum'
	print('linenum:')
	subprocess.call(cmd, shell=True)
	cmd='adb -s '+str(device_url_port)+' shell getprop microvirt.simserial'
	print('sn:')
	subprocess.call(cmd, shell=True)
	cmd='adb -s '+str(device_url_port)+' shell getprop ro.product.brand'
	print('brand:')
	subprocess.call(cmd, shell=True)
	cmd='adb -s '+str(device_url_port)+' shell getprop ro.product.model'
	print('model:')
	subprocess.call(cmd, shell=True)
def main(user,memu_name,device_url_port):
	close_device()
	get_request_info_API(user,memu_name)
	start_device(memu_name)
	connect_device(device_url_port)
	update_sqlite_for_zilong(device_url_port)
	getprop(device_url_port)
if __name__ == '__main__':
	main('18626838764','MEmu_1','127.0.0.1:21513')