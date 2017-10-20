from flask import Flask, url_for, redirect, request, json, session,Response
from flask import render_template
from app.controler.deviceinfo import deviceinfo


import re
app = Flask(__name__)


@app.route('/getinfo')
#getLP?creativeID=838
def getdeviceinfo():
	r=""
	sn=""
	username=""
	ip_=request.remote_addr
	UA_=request.headers.get('User-Agent')
	args=request.args.items()
	for x in xrange(0,len(args)):
		if args[x][0].lower()=="sn".lower():
			print(args[x][1])
			sn=args[x][1]
		if args[x][0].lower()=="username".lower():
			print(args[x][1])
			username=args[x][1]
	if username=="" or username is None:
		r='{"status":"500"}'
	else:
		r=deviceinfo.get_device_info(username)
	deviceinfo.get_device_info_log(sn,username,ip_,UA_[0:199],r[11:14])
	return str(r)

@app.route('/getplan')
#getLP?creativeID=838
def getplan_():
	r=""
	sn=""
	channel_type=""
	game_id=""
	ip_=request.remote_addr
	UA_=request.headers.get('User-Agent')
	args=request.args.items()
	for x in xrange(0,len(args)):
		if args[x][0].lower()=="sn".lower():
			sn=args[x][1]
		if args[x][0].lower()=="game_id".lower():
			game_id=args[x][1]
		if args[x][0].lower()=="channel_type".lower():
			channel_type=args[x][1]
	if  channel_type=="" or channel_type is None  or len(channel_type)>50 or game_id=="" or game_id is None :
		r='{"status":"500"}'
	else:
		r=deviceinfo.get_plan(game_id,channel_type,sn,ip_)
	return str(r)





@app.route('/update_status')

def update_status_():
	r=""
	status=""
	des=""
	account_id=""
	ip_=request.remote_addr
	# UA_=request.headers.get('User-Agent')
	args=request.args.items()
	for x in xrange(0,len(args)):
		if args[x][0].lower()=="status".lower():
			print(args[x][1])
			status=re.sub("[^\w]+","",args[x][1])
		if args[x][0].lower()=="des".lower():
			print(args[x][1])
			des=re.sub("[^\w]+","",args[x][1])
		if args[x][0].lower()=="account_id".lower():
			print(args[x][1])
			account_id=re.sub("[^\w]+","",args[x][1])
	if (status!="4" and status!="2") or account_id=="" or account_id is None:
		print 1
		r='{"status":"500"}'
	else:
		r=deviceinfo.update_status(status[0:10],des[0:40],account_id[0:15],ip_)
	
	return str(r)


if __name__ == '__main__':

	app.debug = True
	app.run(host='0.0.0.0', port=5000,threaded=True)