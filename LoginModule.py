# coding:utf-8
import time

# Get the present time stamp 
time1 = time.time()
f1 = open('time.txt')
time2 = float(f1.readline())
# Compare two time stamps,if the interval isn't over 10s,check the blacklist. 
if time1-time2<10:
	f2 = open('blacklist.txt')
	if 'quit' in f2.read():
		exit()
# 3 chances to access,if success,show welcome message,
# else quit and write in the blacklist,and also record the time stamp.
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
