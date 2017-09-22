# This Python file uses the following encoding: utf-8
import sys
from Config import Config
import datetime
import random
import pymysql
class deviceinfo:


	@staticmethod
	def get_device_info(username):
 		mysql_r = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])

		result=""
		sql='select username,macaddress,hmac,imei,imsi,linenum,microvirt_vm_brand,microvirt_vm_manufacturer,microvirt_vm_model,operator_network,resolution_height,resolution_width,simserial,mac_back from zilong_robot.deviceinfo where username='+str(username)+' limit 1;'
		cursor=mysql_r.cursor()
		cursor.execute(sql)
		rs=cursor.fetchall()		
		if len(rs)>0:
			for r in rs:
				result='[{"username":"'+str(r[0])+'","macaddress":"'+str(r[1])+'","hmac":"'+str(r[2])+'","imei":"'+str(r[3])+'","imsi":"'+str(r[4])+'","linenum":"'+str(r[5])+'","microvirt_vm_brand":"'+str(r[6])+'","microvirt_vm_manufacturer":"'+str(r[7])
				result+='","microvirt_vm_model":"'+str(r[8])+'","operator_network":"'+str(r[9])+'","resolution_height":"'+str(r[10])+'","resolution_width":"'+str(r[11])+'","simserial":"'+str(r[12])+'","mac_back":"'+str(r[13])+'"}]'
				result='{"status":"200","body":'+result+'}'
		else:
			result='{"status":"400","body":"username does not exist"}'
		cursor.close()
		return result
		mysql_r.close()


	@staticmethod
	def get_device_info_log(sn,username,ip,ua,r):
 		mysql_r = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])

		result=""
		sql='insert into zilong_robot.device_update_log values(null,"'+str(sn)+'","'+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+'","'+str(username)+'","'+str(ip)+'","'+str(ua)+'","'+str(r)+'");'
		print(sql)
		cursor=mysql_r.cursor()
		cursor.execute(sql)
		mysql_r.commit()
		cursor.close()
		mysql_r.close()
