#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import device_info_client
import vivo_viewclient_sigle
import json
import sys
import os
import subprocess
from Config import Config
import pymysql

import time
import money_import_oppo
import oppo_viewclient_sigle
def get_card_recharge_plan(channel):
	mysql = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])
	update_sql=""
	res=""
	r=""
	# sql='LOCK tables card_recharge_plan write;LOCK tables card_info write;'
	# cursor=mysql.cursor()
	# cursor.execute(sql)
	sql='SELECT a.10_,a.100_,a.1000_,a.card_plan_id,a.account_id,b.username,b.password,a.channel_name FROM  `card_recharge_plan` a ,account_info b WHERE a.account_id=b.account_id AND a.status=0 and a.channel_name="'+str(channel)+'" limit 1 for update'
	print(sql)
	cursor=mysql.cursor()
	cursor.execute(sql)
	rs=cursor.fetchall()		
	if len(rs)==1:
		for r in rs:
			res="""
SELECT * FROM (
SELECT card_id,card_name,card_pwd,card_class FROM `card_info` WHERE card_status=0 AND card_class='10' LIMIT """+str(r[0])+""" ) a 
UNION ALL
SELECT * FROM (
SELECT card_id,card_name,card_pwd,card_class FROM `card_info` WHERE card_status=0 AND card_class='100' LIMIT """+str(r[1])+""" ) b
UNION ALL
SELECT * FROM  (

SELECT card_id,card_name,card_pwd,card_class FROM `card_info` WHERE card_status=0 AND card_class='1000' LIMIT """+str(r[2])+""") c
for update

			"""
			update_sql+="UPDATE `card_recharge_plan` SET STATUS=1,update_time=now() WHERE card_plan_id='"+str(r[3])+"';"

			cursor=mysql.cursor()
			cursor.execute(res)
			rs=cursor.fetchall()
			
			res='{"account_id":"'+str(r[4])+'","username":"'+str(r[5])+'","password":"'+str(r[6])+'","channel_name":"'+str(r[7])+'","card_plan_id":"'+str(r[3])+'",'
			res_card='"rechargeDict":['
			if len(rs)>0:
				update_sql+="UPDATE `card_info` SET card_status=1 ,update_time=NOW() WHERE card_id IN ("
				for x in rs:
					res_card+='{"card_id":"'+str(x[0])+'","card_name":"'+str(x[1])+'","card_pwd":"'+str(x[2])+'","card_class":"'+str(x[3])+'"},'
					update_sql+=str(x[0])+","

				res=res+res_card[:-1]+"]}"
				update_sql=update_sql[:-1]+");"
				
				cursor=mysql.cursor()
				cursor.execute(update_sql)
				mysql.commit()

				r=res
			else:
				r=-2
	else:
		r=-1
		
	# sql='unlock tables;'
	# cursor=mysql.cursor()
	# cursor.execute(sql)
	cursor.close()
	mysql.close()
	return r
def card_reacharge_success(account_id,money,balance,card,pwd):
	mysql = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])
	sql="INSERT INTO `account_balance_log` VALUES('"+str(account_id)+"','"+str(balance)+"',now(),2,'"+str(money)+"','"+str(card)+"');"
	sql+="update card_info set card_status=2,update_time=now() where card_name='"+str(card)+"' and card_pwd='"+str(pwd)+"';"
	cursor=mysql.cursor()
	cursor.execute(sql)
	mysql.commit()
	cursor.close()
	mysql.close()


def plan_success(plan_id,res):
	card_id=""
	res=res.split(",")
	for r in res:
		r=r.split("_")
		card_id+=r[2]+","

	mysql = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])
	sql='UPDATE `card_recharge_plan` SET STATUS=(CASE WHEN (SELECT COUNT(card_status)+1 FROM `card_info` WHERE card_id IN('+str(card_id[:-1])+') AND card_status!=2 ) THEN 2 ELSE 4 END ) WHERE card_plan_id="'+str(plan_id)+'" '
	cursor=mysql.cursor()
	cursor.execute(sql)
	mysql.commit()	
	cursor.close()
	mysql.close()

def main(brand,memuname,ser,comname):

	path=os.getcwd()
	while 1:
		plan=get_card_recharge_plan(brand)
		print(plan)
		if plan==-1 or plan==-2:
			print(plan,'there is no plan')

			return 10086 # 为了提示执行完毕，不让多线程死锁
		# try:

		# 	IP.main_()
		# except:
		# 	print("no change IP")
		# 	pass

		plan=json.loads(plan)
		account_id=plan["account_id"]
		user=plan["username"]

		pwd=plan["password"]
		rechargeDict=plan["rechargeDict"]
		card_plan_id=plan["card_plan_id"]
		print(user)
		print(pwd)
		print(rechargeDict)
		# follow=0
		# while follow==0:
		# 	try:
		# 		device_info_client.main(user,memuname,ser)
		# 	except:
		# 		print("change device error")
				

			
		# 	tag=vivo_viewclient_sigle.main(user,pwd,ser,comname)#登录vivo
		# 	if tag=="ok":
		# 		print('login ok')
		# 		follow=1
		# 	else:
		# 		print('login error')
		# 		#time.sleep(10)
		# 		return 0

		res=""
		for x in xrange(0,len(rechargeDict)):
			res+=rechargeDict[x]['card_name']+"_"+rechargeDict[x]['card_pwd']+"_"+rechargeDict[x]['card_id']+","

		print(str(res[:-1]),user)
		
		cmd='monkeyrunner '+path+'\\money_import.py '+str(res[:-1])+" "+str(user)+" "+str(ser)
		print(cmd)
		p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		while  p.poll() is None:
			line=p.stdout.readline()
			line=line.strip()
			if line:
				print(line)
				if "card_reacharge_success|" in str(line):
					money=line.split("|")[1]
					balance=line.split("|")[2]
					card=line.split("|")[3]
					pwd=line.split("|")[4]
					card_reacharge_success(account_id,money,balance,card,pwd)
		if p.returncode==0:
			print('sub success')
			plan_success(card_plan_id,res[:-1])
		else:
			print('sub error')
	
def main_v2(brand,memuname,ser,comname):

	path=os.getcwd()
	while 1:
		plan=get_card_recharge_plan(brand)
		print(plan)
		if plan==-1 or plan==-2:
			print(plan,'there is no plan')

			return 10086 # 为了提示执行完毕，不让多线程死锁
		# try:

		# 	IP.main_()
		# except:
		# 	print("no change IP")
		# 	pass

		plan=json.loads(plan)
		account_id=plan["account_id"]
		user=plan["username"]
		result=[]
		pwd=plan["password"]
		rechargeDict=plan["rechargeDict"]
		card_plan_id=plan["card_plan_id"]
		print(user)
		print(pwd)
		print(rechargeDict)
		
		follow=0
		while follow==0:

			# try:
			device_info_client.main(user,memuname,ser)
			# except:
			# 	print("change device error")
			# 	continue

			if brand=='oppo':
				
				tag=oppo_viewclient_sigle.main(user,pwd,ser,comname)#登录vivo
				if tag=="ok":
					print('login ok')
					follow=1
				else:
					print('login error')
					#time.sleep(10)
					continue
			else:
				continue
				print('brand is not oppo')
		
		res=""
		for x in xrange(0,len(rechargeDict)):
			#try:
				result=money_import_oppo.money_import(rechargeDict[x]['card_class'],rechargeDict[x]['card_name'],rechargeDict[x]['card_pwd'],ser,'com.zlongame.fs.nearme.gamecenter/com.nearme.game.sdk.component.proxy.ProxyActivity')
				if result!='faild_4' and result!='faild_other' and result!='faild_7' and result!='faild_8':
					card_reacharge_success(account_id,result[0],result[1],rechargeDict[x]['card_name'],rechargeDict[x]['card_pwd'])
				elif result=='faild_other': 
					print('money inport is error'+str(rechargeDict[x]['card_name']))
					card_reacharge_success(account_id,result[0],result[1],str(rechargeDict[x]['card_name'])+"_error",str(rechargeDict[x]['card_pwd'])+"_error")
				elif result=='faild_4': 
					print('money inport is error。。already recharge'+str(rechargeDict[x]['card_name']))
					card_reacharge_success(account_id,result[0],result[1],str(rechargeDict[x]['card_name'])+"_error—recharge",str(rechargeDict[x]['card_pwd'])+"_error—recharge")
				elif result=='faild_7': 
					#print('money inport is error。。already recharge'+str(rechargeDict[x]['card_name']))
					card_reacharge_success(account_id,result[0],result[1],str(rechargeDict[x]['card_name'])+"_error_pageshow_faild",str(rechargeDict[x]['card_pwd'])+"_error_pageshow_faild")
				elif result=='faild_8': 
					#print('money inport is error。。already recharge'+str(rechargeDict[x]['card_name']))
					card_reacharge_success(account_id,result[0],result[1],str(rechargeDict[x]['card_name'])+"_error_no_jcard",str(rechargeDict[x]['card_pwd'])+"_error_no_jcard")

			#except:
				#print('error,money import code is error')
		res=""
		for x in xrange(0,len(rechargeDict)):
			res+=rechargeDict[x]['card_name']+"_"+rechargeDict[x]['card_pwd']+"_"+rechargeDict[x]['card_id']+","		
		plan_success(card_plan_id,res[:-1])




if __name__ == '__main__':
	print(main_v2('oppo','MEmu_1','127.0.0.1:21513','com.zlongame.fs.nearme.gamecenter/com.amazing.flex.GameActivity'))
