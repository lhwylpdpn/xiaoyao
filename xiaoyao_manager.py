#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import device_info_client
import vivo_viewclient_sigle



print 3

while 1:

	res=device_info_client.get_plan('vivo','1479458217005')
	print(res)
	try:
		device_info_client.main(res[0]["er"])
	except:
		device_info_client.write_log(res[0]['account_id'],4,'start_error or userinfo_error')
	vivo_viewclient_sigle.main(res[0]["username"],res[0]['password'])

	break;
