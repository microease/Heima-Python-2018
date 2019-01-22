#coding=utf-8
import time

def application(env,startResponse):
	status = " 200 OK"
	headers = [("Content-Type","text/plain")]
	startResponse(status,headers)
	return time.ctime()