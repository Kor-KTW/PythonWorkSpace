import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

urls = ["10.1016/j.physletb.2020.135710",
"10.1016/j.physletb.2020.135609",
"10.1016/j.physletb.2020.135502",
"10.1016/j.physletb.2020.135425",
"10.1016/j.physletb.2020.135578",
"10.1016/j.physletb.2020.135345",
"10.1016/j.physletb.2020.135203",
"10.1016/j.physletb.2020.135448",
"10.1016/j.physletb.2020.135409",
"10.1016/j.physletb.2020.135263",
"10.1016/j.physletb.2020.135285",
"10.1016/j.physletb.2019.135087",
"10.1016/j.physletb.2019.134992",
"10.1016/j.physletb.2019.135183",
"10.1016/j.physletb.2019.134876",
"10.1016/j.physletb.2020.135328",
"10.1016/j.physletb.2019.134952",
"10.1007/JHEP08(2020)139",
"10.1103/PhysRevD.102.072001",
"10.1103/PhysRevLett.125.152001",
"10.1007/JHEP08(2020)051",
"10.1007/JHEP07(2020)115",
"10.1007/JHEP07(2020)116",
"10.1103/PhysRevLett.125.061801",
"10.1007/JHEP07(2020)125",
"10.1140/epjc/s10052-020-8166-5",
"10.1007/JHEP06(2020)076",
"10.1140/epjc/s10052-020-8168-3",
"10.1007/JHEP07(2020)126",
"10.1103/PhysRevD.102.032007",
"10.1007/JHEP05(2020)052",
"10.1088/2632-2153/ab9023",
"10.1007/JHEP06(2020)146",
"10.1007/JHEP05(2020)032",
"10.1103/PhysRevLett.124.162002",
"10.1103/PhysRevLett.124.131802",
"10.1007/JHEP06(2020)018",
"10.1007/JHEP03(2020)131",
"10.1007/JHEP03(2020)034",
"10.1007/JHEP02(2020)191",
"10.1007/JHEP03(2020)103",
"10.1103/PhysRevD.101.052010",
"10.1007/JHEP03(2020)051",
"10.1007/JHEP05(2020)033",
"10.1103/PhysRevLett.124.202001",
"10.1007/JHEP03(2020)055",
"10.1103/PhysRevLett.125.102001",
"10.1007/JHEP02(2020)015",
"10.1007/JHEP04(2020)188",
"10.1007/JHEP03(2020)065",
"10.1007/JHEP03(2020)014",
"10.1140/epjc/s10052-020-7834-9",
"10.1103/PhysRevC.101.064906",
"10.1103/PhysRevLett.124.041803",
"10.1140/epjc/s10052-019-7541-6",
"10.1103/PhysRevD.100.112003"]


usableurls = []
#urltpys = PLB=physletb, JHEP=JHEP, PRC=PhysRevC, PRD=PhysRevD, PRL=PhysRevLett, epjc, iop --> iop는 url에 저널정보가 없음.
PLB = []
JHEP = []
PRC = []
PRD = []
PRL=[]
EPJC = []
IOP = []

PLBcheck = re.compile("physletb")
JHEPcheck = re.compile("JHEP")
PRCcheck = re.compile("PhysRevC")
PRDcheck = re.compile("PhysRevD")
PRLcheck = re.compile("PhysRevLett")
EPJCcheck = re.compile("epjc")

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")
browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
for url in urls:
    usableurl = "https://doi.org/"+url
    res = requests.get(usableurl)
    res.raise_for_status()
    print("REQ", usableurl,"complete")
    # usableurls.append(usableurl)
    soup = BeautifulSoup(res.text, 'lxml')



    if PLBcheck.search(usableurl):
        PLB.append(usableurl)
        date = soup.find_all("div", attrs={"id":"publication"})
        print(date)



    elif JHEPcheck.search(usableurl):
        JHEP.append(usableurl)

    elif PRCcheck.search(usableurl):
        PRC.append(usableurl)        

    elif PRDcheck.search(usableurl):
        PRD.append(usableurl)

    elif PRLcheck.search(usableurl):
        PRL.append(usableurl)

    elif EPJCcheck.search(usableurl):
        EPJC.append(usableurl)

    else:
        IOP.append(usableurl)
# print("--------------------------")
# print(str(PLB))
# print("--------------------------")
# print(str(JHEP))
# print("--------------------------")
# print(str(PRC))
# print("--------------------------")
# print(str(PRD))
# print("--------------------------")
# print(str(PRL))
# print("--------------------------")
# print(str(EPJC))
# print("--------------------------")
# print(str(IOP))

    
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")