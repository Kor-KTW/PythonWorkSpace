import requests
from bs4 import BeautifulSoup
import re

urls = ["10.1016/j.physletb.2020.135710"]

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


for url in urls:
    usableurl = "https://doi.org/"+url
    res = requests.get(usableurl)
    res.raise_for_status()
    #print("REQ", usableurl,"complete")
    print(res.text)
    # usableurls.append(usableurl)
    soup = BeautifulSoup(res.text, 'html.parser')

    


    if PLBcheck.search(usableurl):
        PLB.append(usableurl)
        date = soup.find_all("div", attrs={"id":"publication"})
        #print(date)



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