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
def connect_device():

	info=os.popen('adb connect 127.0.0.1:21503')
	print(info.read())

def start_device():

	pwd=getinfo()

	os.chdir(pwd)
	cmd="MEmuConsole.exe MEmu"

	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)




def close_device():


	cmd="taskkill /f /t /im ME*"
	subprocess.call(cmd, shell=True)

def getinfo():

    config = ConfigParser.ConfigParser()
    path = 'conf_menu.conf'
    config.read(path)
    return config.get('MEmu', 'MEmuname')


def getsn():
	sn = 'Y2FvaGFu'
	return sn

def get_request_info():
	print(1)
	url="http://120.26.162.150:5000/getinfo?sn="+getsn()+"&username="+argv[1]
	print(url)






	headers=[]
	headers.append(('User-Agent' , '673b34113cbd60dfb16ef9459614fc89_lhwylp'))
	opener = urllib2.build_opener()
	opener.addheaders=headers
	res=opener.open(url)
	updateinfo(res.read())

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
if __name__ == '__main__':
	close_device()
