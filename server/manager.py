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



if __name__ == '__main__':

	app.debug = True
	app.run(host='0.0.0.0', port=5000,threaded=True)