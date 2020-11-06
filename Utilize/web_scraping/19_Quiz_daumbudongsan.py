import requests
from bs4 import BeautifulSoup
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows):
    trade_type = row.find("td",attrs={"class":"col1"}).get_text()
    area = row.find("td",attrs={"class":"col2"}).get_text()
    price = row.find("td",attrs={"class":"col3"}).get_text()
    dong = row.find("td",attrs={"class":"col4"}).get_text()
    floor = row.find("td",attrs={"class":"col5"}).get_text()

    print(" ========== 매물 {}========== ".format(index+1))
    print("거래 : ", trade_type)
    print("면적 : ", area, "(공급/전용)")
    print("가격 : ", price, "(만원)") 
    print("동 : ", dong)
    print("층 : ", floor)
    print(" =========================== ")

        


