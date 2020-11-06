
import re
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
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
"10.1103/PhysRevD.100.112003"
]


usableurls = []

PLBcheck = re.compile("physletb")
#저널명 확인 위함.
options = webdriver.ChromeOptions()
options.headless = False
#background job 할 때 넣는 기능 -> True로 설정하면 백그라운드에서 작업가능. 다만, CORS 정책때문에 블락 당했다고하지만 데이터는 다 가져옴. 
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")
#user-agent option을 통해 해당 사이트에 코드로 접속하는것이 아닌, 사람이 접속하는 것으로 느끼게 함. https://www.whatismybrowser.com/detect/what-is-my-user-agent 여기 들어가서 주소부분 복사 붙여넣기하면됨.
browser = webdriver.Chrome(options=options)
browser.maximize_window()
f = open("PLB", "w", encoding="utf8")
for url in urls:
    usableurl = "https://doi.org/"+url
    
    
    




    if PLBcheck.search(usableurl):
        browser.get(usableurl)
        
        elem = WebDriverWait(browser, 100).until(ec.presence_of_element_located((By.XPATH,"//*[@id='pdfLink']/span/span[1]")))
        #내가 원하는 자료가 나타날때까지 최대 100초간 대기.
        informa = browser.find_element_by_xpath("//*[@id='publication']/div[2]/div").text
        #xpath로 타겟잡고 텍스트로 출력
        informa = list(informa.split(", "))
        volume = informa[0]
        date = informa[1]
        motherpage = informa[2]
        f.write(f"{volume}  {date}  {motherpage}\n")
        print(volume, date, motherpage)
        print("Browser get : ", usableurl," -->>  Complete")
    
    else:
        pass