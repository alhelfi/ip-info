from ast import Try
from email import header
import requests
import webbrowser
#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

print(f'''\033[33m
 ██▓ ██▓███      ██▓ ███▄    █   █████▒▒█████  
▓██▒▓██░  ██▒   ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▒██▒▓██░ ██▓▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
░██░▒██▄█▓▒ ▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
░██░▒██▒ ░  ░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
░▓  ▒▓▒░ ░  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
 ▒ ░░▒ ░         ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
 ▒ ░░░           ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
 ░               ░           ░            ░ ░ 
My website : https://alhelfi.softr.app  |  My instagram : hh__y
''')

ip=input(f'\033[31mType ip \033[36m:\033[39m ')
def ipinfo():
	
	url=f'https://demo.ip-api.com/json/{ip}?fields=66842623&lang=en'
	headers={
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'demo.ip-api.com',
	'Origin': 'https://ip-api.com',
	'Referer': 'https://ip-api.com/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
	 }
	
	req=requests.post(url,headers=headers)
	print(f'\033[31m[+]  status :  \033[32m'+req.json()['status'])
	print(f'\033[31m[+]  continent :  \033[32m'+req.json()['continent'])
	print(f'\033[31m[+]  continentCode : \033[32m'+req.json()['continentCode'])
	print(f'\033[31m[+]  country : \033[32m'+req.json()['country'])
	print(f'\033[31m[+]  countryCode : \033[32m'+req.json()['countryCode'])
	print(f'\033[31m[+]  region :  \033[32m'+req.json()['region'])
	print(f'\033[31m[+]  regionName : \033[32m'+req.json()['regionName'])
	print(f'\033[31m[+]  city : \033[32m'+req.json()['city'])
	print(f'\033[31m[+]  district : \033[32m'+req.json()['district'])
	print(f'\033[31m[+]  zip : \033[32m'+req.json()['zip'])
	print(f'\033[31m[+]  timezone : \033[32m'+req.json()['timezone'])
	print(f'\033[31m[+]  currency : \033[32m'+req.json()['currency'])
	print(f'\033[31m[+]  isp : \033[32m'+req.json()['isp'])
	print(f'\033[31m[+]  as : \033[32m'+req.json()['as'])
	print(f'\033[31m[+]  asname : \033[32m'+req.json()['asname'])
	print(f'\033[31m[+]  query : \033[32m'+req.json()['query'])
	print(f'\033[31m[+]  lat : \033[32m'+str(req.json()['lat']))
	print(f'\033[31m[+]  lon : \033[32m'+str(req.json()['lon']))
	print(f'\033[31m[+]  offset : \033[32m'+str(req.json()['offset']))
	print(f'\033[31m[+]  mobile : \033[32m'+str(req.json()['mobile']))
	print(f'\033[31m[+]  proxy : \033[32m'+str(req.json()['proxy']))
	print(f'\033[31m[+]  hosting : \033[32m'+str(req.json()['hosting']))

	url1=f'https://ipwhois.pro/{ip}?key=Sxd2AkU2ZL0YtkSR&security=1&lang=en'
	headers1={
	    'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'ipwhois.pro',
	'Origin': 'https://ipwhois.io',
	'Referer': 'https://ipwhois.io/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'cross-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36ed-with'
	
	}
	req1=requests.get(url1,headers=headers1)
	
	print(f'\033[31m[+]  calling_code : \033[32m'+str(req1.json()['calling_code']))
	print(f'\033[31m[+]  img country :   \033[32m'+str(req1.json()['flag']['img']))
	print(f'\033[31m[+]  vpn :  \033[32m'+str(req1.json()['security']['vpn']))
	print(f'\033[31m[+]  tor :  \033[32m'+str(req1.json()['security']['tor']))
	print(f'\033[31m[+]  anonymous :  \033[32m'+str(req1.json()['security']['anonymous']))

	req3=requests.get(f'https://ipapi.co/{ip}/json/')
	print(f'\033[31m[+]  version :  \033[32m'+str(req3.json()['version']))
	print(f'\033[31m[+]  asn :  \033[32m'+str(req3.json()['asn']))
	print(f'\033[31m[+]  Location : \033[32m'+str(req.json()['lat'])+','+str(req.json()['lon']))

ipinfo()
print('''
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀ ⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁ ''')
myweb = input("This tool was developed by Mohammad Ali, do you want to visit my personal website? (Y/N)")
if myweb == "y":
	webbrowser.open("https://alhelfi.softr.app")
elif myweb == "n":
	print("thank you for using :( ")
else:
	print("i said Y or N =_=")
	exit()