#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import xlrd
from Config import Config
import pymysql
import datetime
import os
import shutil


def card_import():
	try:
		data = xlrd.open_workbook('card.xlsx')
	except:
		print('excel is not exists')
		return 0
	table = data.sheets()[0]
	sql="delete from card_info where card_status=99;insert into card_info values "
	money_count=[]
	for x in xrange(0,table.nrows):
		#print(table.cell(x,1).value)
		#print(table.cell(x,0).value)
		#print(table.cell(x,2).value)
		try:
			sql+="(null,'"+str(table.cell(x,1).value)+"','"+str(table.cell(x,2).value)+"','"+str(int(table.cell(x,0).value))+"',99,now()),"
			money_count.append(int(table.cell(x,0).value))
		except:
			print(table.cell(x,0).value,table.cell(x,1).value,table.cell(x,2).value,'is not import')

	print("sum money is: ",sum(money_count))
	print("10 card is: ",money_count.count(10))
	print("100 card is: ",money_count.count(100))
	print("1000 card is: ",money_count.count(1000))
	status = raw_input("card is ok?:")

	if status=='ok':
		mysql = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])
		cursor=mysql.cursor()
		cursor.execute(sql[:-1])

		mysql.commit()
		sql='SELECT SUM(card_class) FROM card_info WHERE card_status=99; '
		cursor.execute(sql)
		rs=cursor.fetchall()
		if len(rs)==1:
			for r in rs:
				print(int(r[0]))
				if int(r[0])==int(sum(money_count)):
					print('all card money is ok')
				else :
					print( 'card  money insert into mysql is not equals')
		cursor.close()
		mysql.close()
	else:
		print('no mysql insert')


def plan_import(name):
	name_=0
	pass_=0
	money_=0
	count=0
	try:
		data = xlrd.open_workbook('plan.xlsx')
	except:
		print('excel is not exists')
		return 0
	table = data.sheet_by_name(name)
	for x in xrange(0,table.ncols):
		if table.cell(0,x).value=='账号名':
			name_=x
		if table.cell(0,x).value=='密码':
			pass_=x
		if table.cell(0,x).value=='待充值':
			money_=x

	if name_==0 or pass_==0 or money_==0:
		print('excel is error')
		return 0
	game_name = raw_input("game_name is ok?:")
	sql='delete from account_info where status=99;INSERT INTO account_info VALUES '
	for x in xrange(0,table.nrows):
		try:
			if int(table.cell(x,0).value)==0:
				sql+="('"+str(game_name)+"',null,now(),'"+str(int(table.cell(x,name_).value))+"','"+str(table.cell(x,pass_).value)+"','"+str(name)+"','"+str(int(table.cell(x,money_).value))+"',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,99),"
				count+=1
		except:
			pass
	print("account count",name,count)
	status = raw_input("account is ok?:")	
	if status=='ok':
		mysql = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])
		cursor=mysql.cursor()
		cursor.execute(sql[:-1])
		mysql.commit()
		sql="""
INSERT INTO `card_recharge_plan`

SELECT NULL,account_id,'oppo',99,10_,100_,CASE WHEN 1000_="" THEN 0 ELSE 1000_ END AS 1000_,NOW() FROM (
SELECT account_id,
CASE WHEN MID(c,LENGTH(c)-1,1)<8 AND MID(c,LENGTH(c),1)!=0 THEN MID(c,LENGTH(c)-1,1)+1  WHEN MID(c,LENGTH(c)-1,1)<8 AND MID(c,LENGTH(c),1)=0 THEN MID(c,LENGTH(c)-1,1)  WHEN MID(c,LENGTH(c)-1,1)>=8 THEN 0 END  AS 10_,
CASE WHEN LENGTH(c)>2 AND MID(c,LENGTH(c)-1,1)<8 THEN MID(c,LENGTH(c)-2,1) WHEN  LENGTH(c)>=2 AND MID(c,LENGTH(c)-1,1)>=8 AND  MID(c,LENGTH(c)-2,1)<9 THEN  MID(c,LENGTH(c)-2,1)+1 ELSE 0 END AS 100_,
CASE WHEN LENGTH(c)>3 AND MID(c,LENGTH(c)-2,1)<9 THEN MID(c,1,LENGTH(c)-3) WHEN  LENGTH(c)>=3 AND MID(c,LENGTH(c)-2,1)>=9 AND  MID(c,LENGTH(c)-1,1)>=8 THEN MID(c,1,LENGTH(c)-3)+1  WHEN  LENGTH(c)>=3 AND MID(c,LENGTH(c)-2,1)>=9 AND  MID(c,LENGTH(c)-1,1)<8 THEN MID(c,1,LENGTH(c)-3)  ELSE 0 END  AS 1000_,
NOW() FROM (
SELECT account_id,server_id AS c
FROM `account_info` WHERE STATUS=99 GROUP BY account_id) a
) a


		"""
		cursor.execute(sql)# 生成执行计划
		mysql.commit()
		sql="""
INSERT INTO `deviceinfo`

SELECT b.username,REPLACE(macaddress,":",""),REPLACE(macaddress,":",""),a.imei,a.imei,CONCAT("+86",b.username),a.microvirt_vm_brand,a.microvirt_vm_manufacturer,a.microvirt_vm_model,a.operator_network,720,1280,a.simserial,NULL FROM (

SELECT @rownum:=@rownum+1 AS rownum, b.* FROM (SELECT @rownum:=0) a,(SELECT * FROM `device_back` WHERE microvirt_vm_brand='oppo' ORDER BY RAND() LIMIT """+str(count)+""") b ) a 
,

(SELECT @rownum2:=@rownum2+1 AS rownum, b.* FROM (SELECT @rownum2:=0) a,( SELECT  a.* FROM `account_info` a, `card_recharge_plan` b WHERE a.`account_id`=b.`account_id` AND b.status=99 AND b.`channel_name`='oppo') b ) b
WHERE a.rownum=b.rownum

		"""
		cursor.execute(sql)# 随机生成设备信息
		mysql.commit()
		sql="SELECT COUNT(*) FROM card_recharge_plan WHERE STATUS=99 AND channel_name='"+str(name)+"'"
		cursor.execute(sql)
		rs=cursor.fetchall()
		if len(rs)==1:
			for r in rs:
				print(int(r[0]))
				if int(r[0])==count:
					print ('all account insert  mysql is ok')
				else :
					print('account insert mysql is not euqals')
		cursor.close()
		mysql.close()
	else:
		print('no mysql insert')

def check():
	mysql = pymysql.connect(host=Config.mysql_conf['host'],port=Config.mysql_conf['port'],user=Config.mysql_conf['user'],password=Config.mysql_conf['password'],database=Config.mysql_conf['dbName'],charset=Config.mysql_conf['charset'])
	cursor=mysql.cursor()
	sql=""

	sql="SELECT SUM(10_)*10+SUM(100_)*100+SUM(1000_)*1000 AS B , SUM(10_) as '10' ,SUM(100_) as '100',SUM(1000_) as '1000' FROM `card_recharge_plan` WHERE STATUS=99;"
	cursor.execute(sql)
	rs=cursor.fetchall()
	if len(rs)==1:
		for r in rs:

			print('plan all money:',str(r[0]),'10 count',str(r[1]),'100 count ',str(r[2]),'1000 count',str(r[3]))
			
	sql='SELECT SUM(card_class) FROM card_info WHERE card_status=99;'
	cursor.execute(sql)
	rs=cursor.fetchall()
	if len(rs)==1:
		for r in rs:
			print('card all money:',str(r[0]))

	status = raw_input("is it ok,start?:")
	if status=='ok':
		sql='UPDATE `card_info` SET card_status=0 WHERE card_status=99;UPDATE `card_recharge_plan` SET STATUS=0 WHERE STATUS=99;UPDATE `account_info` SET STATUS=0 WHERE STATUS=99;'
		cursor.execute(sql)
		mysql.commit()
		cursor.close()
		mysql.close()		
	else :
		cursor.close()
		mysql.close()
def backfile():
	newpath=os.getcwd()+"\\_"+str(str(datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')))
	os.mkdir(newpath)
	try:
		shutil.move(os.getcwd()+"\\plan.xlsx",newpath+"\\plan.xlsx")
	except:
		print('plan not copy')
	try:
		shutil.move(os.getcwd()+"\\card.xlsx",newpath+"\\card.xlsx")
	except:
		print('card not copy')





if __name__ == '__main__':
	card_import()
	plan_import('oppo')
	backfile()
	check()