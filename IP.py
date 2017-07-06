# coding=utf-8
import os
import urllib2
import urllib
from xml.dom.minidom import parse
import xml.dom.minidom
import random

def init():
	state=""
	opener = urllib2.build_opener()
	url='http://127.0.0.1:8222/getstate/'
	res = opener.open(url)

	save_html(res.read().decode("UTF-8"))
	DOMTree = xml.dom.minidom.parse("temp.html")
	root=DOMTree.documentElement
	state=root.getElementsByTagName('state')[0].firstChild.data
 
	if state>=0:
		return 1
	else:
		return root.getElementsByTagName('info')[0].firstChild.data

def connect_back():
	state=""
	opener = urllib2.build_opener()
	index=""
	index=random.randint(1,100)
	url='http://127.0.0.1:8222/getlines/?start='+str(index)+'&end='+str(index+1)

	res = opener.open(url)
	save_html(res.read().decode("UTF-8"))
	DOMTree = xml.dom.minidom.parse("temp.html")
	root=DOMTree.documentElement
	state=root.getElementsByTagName('line')

	url='http://127.0.0.1:8222/connect/?linename='+str(state[0].getAttribute("name")).decode("UTF-8")+'&linktype=2'
	print(url)
	res = opener.open(url)
	save_html(res.read().decode("UTF-8"))
	DOMTree = xml.dom.minidom.parse("temp.html")
	root=DOMTree.documentElement
	state=root.getElementsByTagName('code')[0].firstChild.data
	if state==0:
		print("init OK")
		return 1
	else:
		print(root.getElementsByTagName('code')[0].firstChild.data)
		return root.getElementsByTagName('code')[0].firstChild.data
def connect():
	state=""
	opener = urllib2.build_opener()
	index=""
	url='http://127.0.0.1:8222/hbconnect/?province=所有&linktype=2'
	
	res = opener.open(url)
	save_html(res.read().decode("UTF-8"))
	DOMTree = xml.dom.minidom.parse("temp.html")
	root=DOMTree.documentElement
	state=root.getElementsByTagName('code')[0].firstChild.data
	if state==0:
		print("connect ok")
		return 1
	else:
		#print(root.getElementsByTagName('code')[0].firstChild.data)
		return root.getElementsByTagName('code')[0].firstChild.data

def disconnect():
	state=""
	opener = urllib2.build_opener()
	index=""
	url='http://127.0.0.1:8222/disconnect/'
	res = opener.open(url)
def save_html(data):
    file=open("temp.html", "wb")
    file.write(data)
    file.close()
def GET_IP_Connect():
	state=""
	opener = urllib2.build_opener()
	url='http://127.0.0.1:8222/getstate/'
	res = opener.open(url)

	save_html(res.read().decode("UTF-8"))
	DOMTree = xml.dom.minidom.parse("temp.html")
	root=DOMTree.documentElement
	state=root.getElementsByTagName('ip')[0].firstChild.data
	return state
def status_success():
	state=""
	opener = urllib2.build_opener()
	url='http://127.0.0.1:8222/getstate/'
	res = opener.open(url)

	save_html(res.read().decode("UTF-8"))
	DOMTree = xml.dom.minidom.parse("temp.html")
	root=DOMTree.documentElement
	state=root.getElementsByTagName('ip')[0].firstChild
	if state is not None:
		return 1
	else:
		return 0
def main_():

	if init()==1:
		disconnect()
		while 1:

			if status_success()==0:
				connect()
			else:
				break
		print(GET_IP_Connect())
if __name__ == '__main__':
	connect()