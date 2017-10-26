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
		#return result
		mysql_r.close()
		return result

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

	@staticmethod
	def get_plan(game_id,channel_type,token,ip):
 		mysql_r = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])
 		account_id="none"
 		username="none"
		result=""
		sql='select username,password,channel_name,server_id,action_type,648_,328_,228_,198_,98_,30_,6_,account_id,game_id from zilong_robot.`account_info` where status=0 and channel_name="'+str(channel_type)+'" and game_id="'+str(game_id)+'" order by DATE_FORMAT( plan_time,"%Y-%c-%d %h:%i:%s") limit 1'
		print(sql)
		cursor=mysql_r.cursor()
		cursor.execute(sql)
		rs=cursor.fetchall()		
		if len(rs)>0:
			for r in rs:
				result='[{"account_id":"'+str(r[12])+'","game_id":"'+str(r[13])+'","username":"'+str(r[0])+'","password":"'+str(r[1])+'","channel_name":"'+str(r[2])+'","server_id":"'+str(r[3])+'","action_type":"'+str(r[4])+'","648_":"'+str(r[5])+'","328_":"'+str(r[6])+'","228_":"'+str(r[7])
				result+='","198_":"'+str(r[8])+'","98_":"'+str(r[9])+'","30_":"'+str(r[10])+'","6_":"'+str(r[11])+'"}]'
				result='{"status":"200","body":'+result+'}'
				account_id=str(r[12])
				username=str(r[0])
			sql='insert into zilong_robot.account_run_log values("'+str(account_id)+'","'+str(username)+'",now(),"","1","action_start","'+str(token)+'","'+str(ip)+'","");'
			sql+='update zilong_robot.account_info set status=1 where account_id="'+str(account_id)+'";'
			print(sql)
			cursor.execute(sql)
			mysql_r.commit()

		else:
			result='{"status":"400","body":"there is no plan now"}'
		cursor.close()
		#return result
		mysql_r.close()
		return result		
	@staticmethod
	def update_status(status,des,accountid,ip_):
 		mysql_r = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])
 		try: 
	 		account_id="none"
	 		username="none"
			result=""
			sql='update account_run_log set end_time=now(),status="'+str(status)+'",des="'+str(des)+'",end_IP="'+str(ip_)+'" where account_id="'+str(accountid)+'";'
			sql+='update account_info set status="'+str(status)+'" where account_id="'+str(accountid)+'"' 
			print(sql)
			cursor=mysql_r.cursor()
			cursor.execute(sql)
			mysql_r.commit()
			result=	'{"status":"200"}'
		except:
			result='{"status":"400","body":"sql is error"}'
		cursor.close()
		#return result
		mysql_r.close()
		return result