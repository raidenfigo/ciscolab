# -*- coding: UTF-8 -*-
import sys
import re
#如果是windows版本也可以正常使用 但要改路径

def Cal_ip_used_ratio(filename, netmaskNo=24):
	
	with open(filename, 'r') as file: #读取原始数据文件
		#n=24	#掩码位数
		ipshuliang = (2**(32-netmaskNo)-2)   #计算ip数量

		ipdata = file.readlines()  #读取文件内容
		usedip= 0	#统计使用的ip
		
		for i in ipdata:
		    if re.match(r'^Internet' , i):		#正则表达式匹配关键字
		        usedip += 1
		result = usedip/ipshuliang*100    #计算ip利用率
	return result 
	#except ZeroDivisionError as e:
	#    print('error message is ', e)
	#finally:
	#	file.close()


if len(sys.argv) ==1:
	print('没有正确输入文件名和掩码位数,查看帮助请输入python3.4 test.py -help')
	sys.exit()
elif len(sys.argv) == 2 :


	if sys.argv[1].startswith('-'):
	   option = sys.argv[1][1:]
	   # fetch sys.argv[1] but without the first two characters
	   if option == 'version':
	      print ('ip利用率统计Version 0.1')
	      sys.exit()
	   elif option == 'help':
	      print ('''
	-version : 显示版本号
	-help    : 显示帮助
	e.g. 
	python3.4 test.py /Users/feiwan2/Desktop/pythontest/ipdata.txt 24''')
	      sys.exit()
	   else:
	       print ('参数错误。')
	       sys.exit()
	else:
		#print(sys.argv[:])
		result = Cal_ip_used_ratio(sys.argv[1])
		print('这个网段ip 利用率为%.2f' %result,'%',sep='')

elif len(sys.argv) == 3 :
	try:
		result = Cal_ip_used_ratio(sys.argv[1], int(sys.argv[2]))
		print('这个网段ip 利用率为%.2f' %result,'%',sep='')
	except ValueError :
		print('pls input No. for netmaskNo')

else:
	print("toomany input")	
