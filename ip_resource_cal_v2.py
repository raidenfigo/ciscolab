#!/usr/bin/python3.4
# -*- coding=utf-8 -*-
#本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
#教主QQ:605658506
#亁颐堂官网www.qytang.com
#乾颐盾是由亁颐堂现任明教教主开发的综合性安全课程
#包括传统网络安全（防火墙，IPS...）与Python语言和黑客渗透课程！
import sys
# sys.path.append('/usr/local/lib/python3.4/dist-packages/PyQYT/ExtentionPackages')
# sys.path.append('/usr/lib/python3.4/site-packages/PyQYT/ExtentionPackages')
# sys.path.append('../../ExtentionPackages')

from telnetlib import Telnet
#import re,可以使用正则表达式匹配回显，然后做判断，决定下一步的操作
import time

def QYT_TelnetClient(ip, password, enable, *cmds):
	tn = Telnet(ip, 23)
	rackreply = tn.expect([],timeout=1)[2].decode().strip()#读取回显
	print(rackreply)#打印回显
	# tn.write(username.encode())#任何字串都需要转成二进制字串
	# tn.write(b'\n')#注意一定要打回车
	# time.sleep(1)#在命令之间留出一定的时间间隔！否则路由器可能反应不过来
	# rackreply = tn.expect([],timeout=1)[2].decode().strip()
	# print(rackreply)
	tn.write(password.encode())	
	tn.write(b'\n')
	# time.sleep(1)
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	print(rackreply)
	tn.write(b'enable\n')
	# time.sleep(1)
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	print(rackreply)
	tn.write(enable.encode())
	tn.write(b'\n')
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	print(rackreply)
	# time.sleep(1)
	for cmd in cmds:#读取命令，并且逐个执行！
		tn.write(cmd.encode() + b'\n'+b' '*15)
		result= tn.expect([],timeout=1)[2].decode()
		# print(rackreply)
		# time.sleep(1)
	tn.write(b'exit\n')
	rackreply = tn.expect([],timeout=1)[2].decode().strip()
	print(rackreply)
	tn.close()
	return result



if __name__ == "__main__":
	a=QYT_TelnetClient('10.74.88.1',  'cisco', 'cisco123!', 'show arp | include 10.74.118' )
	print(a)
	usedip=a.count('Internet')
	result = usedip/255*100
	print('这个vlan的ip利用率为%.2f' %result,'%',sep='')