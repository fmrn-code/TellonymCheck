#Need's to list.txt file in same folder
from colorama import Fore
import requests
import random
from threading import Thread
import ctypes
file = open('list.txt','r').read().splitlines()
ag = open('userAgentList.txt','r').read().splitlines()
print(Fore.LIGHTBLUE_EX+'''
  _______   __        ________  ________________ __    
 /_  __/ | / /       / ____/ / / / ____/ ____/ //_/    
  / / /  |/ /       / /   / /_/ / __/ / /   / ,<       
 / / / /|  /  _    / /___/ __  / /___/ /___/ /| |      
/_/ /_/ |_/  (_)   \____/_/ /_/_____/\____/_/ |_|      
''')
omar = requests.session()
def tell():
    Good = 0
    Bad = 0
    Error = 0
    try:
        for user in file:
            url = f'https://api.tellonym.me/accounts/check?username={user}&limit=25'
            h = {'user-agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)', }
            ok = omar.get(url, headers=h)
            if ('"usernameError"') in ok.text:
                print(Fore.RED + f'Taken >> {user}')
                Bad +=1
            elif ('"username":true') in ok.text:
                print(Fore.GREEN+f'Available >> {user}')
                Good +=1
            elif ('"PARAMETER_INVALID"') in ok.text:
                print(Fore.RED+f'Taken >> {user}')
                Bad +=1
    except:
        Error +=1


tell()
stop = input('Programmed \n By @omarmazin_ ...')
