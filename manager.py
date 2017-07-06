#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import os
import IP
import update_device_info
import csv
import sys
def getpro_vivo():
	prop=[]
	pwd=os.getcwd()+'\\plan.csv'
	if not os.path.exists(pwd):
		print("plan.csv not found")
		sys.exit()
	filename=open(pwd)
	reader=csv.reader(filename)
	reader.next()
	for row in reader:
		# _6_=int(row[7])-int(row[14])
		# _30_=int(row[8])-int(row[15])
		# _98_=int(row[9])-int(row[16])
		# _198_=int(row[10])-int(row[17])
		# _328_=int(row[11])-int(row[18])
		# _588_=int(row[12])-int(row[19])
		# _648_=int(row[13])-int(row[20])
		_6_=int(row[7])
		_30_=int(row[8])
		_98_=int(row[9])
		_198_=int(row[10])
		_328_=int(row[11])
		_588_=int(row[12])
		_648_=int(row[13])
		prop.append([row[1],row[2],row[3],row[4],row[5],row[6],_6_,_30_,_98_,_198_,_328_,_588_,_648_])

	#prop=[]#[imei,imsi,linenum,simserial,pwd,serverid,6,30,98,198,328,588,648]
	return prop

if __name__ == '__main__':
	update_device_info.open_device()#连接 adb connect


	#######
	prop=[]
	prop=getpro_vivo()

	for x in xrange(0,len(prop)):
		print('monkeyrunner '+os.getcwd()+'\\vivo.py '+str(prop[x][0])+' '+str(prop[x][1])+' '+str(prop[x][2])+' '+str(prop[x][3])+' '+str(prop[x][4])+' '+str(prop[x][5])+' '+str(prop[x][6])+' '+str(prop[x][7])+' '+str(prop[x][8])+' '+str(prop[x][9])+' '+str(prop[x][10])+' '+str(prop[x][11])+' '+str(prop[x][12])+' ')
		#解析开回来的每个prop，然后拼成多个参数给到monkey
		#monkey 执行，存结果日志


		while 1:
			try:
				IP.main_()
				update_device_info.setproperty(prop)
				break
			except:
				print("error ip")
		info=os.popen('monkeyrunner '+os.getcwd()+'\\vivo.py '+str(prop[x][0])+' '+str(prop[x][1])+' '+str(prop[x][2])+' '+str(prop[x][3])+' '+str(prop[x][4])+' '+str(prop[x][5])+' '+str(prop[x][6])+' '+str(prop[x][7])+' '+str(prop[x][8])+' '+str(prop[x][9])+' '+str(prop[x][10])+' '+str(prop[x][11])+' '+str(prop[x][12])+' ')
		print(info.read())


