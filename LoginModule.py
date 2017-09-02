# coding:utf-8
import time

time1 = time.time()
f1 = open('time.txt')
time2 = f1.readline()
if time1-time2<10:
	f2 = open('blacklist.txt')
	if 'quit' in f2.read():
		exit()
for i in range(3): 
	username = raw_input("Username: ")
	password = raw_input("Password: ")
	if username=='admin' and password=='admin':
		print 'Welcome'
		exit()
	else:
		print 'Invalid username or password!'
else:
	print "Oops!Too many retries,you've been locked!Sorry!"
	f3 = open('blacklist.txt','w')
	f3.write('quit')
	f3.close()
	f4 = open('time.txt','w')
	f4.write(str(time.time()))
	f4.close()
