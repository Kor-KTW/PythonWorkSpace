import requests
from bs4 import BeautifulSoup
import re


url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:
    #광고제품 제외 
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("광고 상품 제외합니다.")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rate = item.find("em", attrs={"class":"rating"})
    if "Apple" in name:
        print("애플 상품 제외합니다.")
        continue
    if rate:
        rate= rate.get_text()
    else:
        rate = "평점 없음"
        print("평점 없는 상품 제외합니다.")
        continue
    rate_count = item.find("span", attrs={"class":"rating-total-count"})
    if rate_count:
        rate_count = rate_count.get_text() #ex:(26)
        rate_count = rate_count[1:-1]
        print("리뷰 수", rate_count)
    else:
        rate = "평점 수 없음"
        print("평점 수 없는 상품 제외합니다.")
        continue
    if float(rate) >= 4.5 and int(rate_count) > 100:
        print(name, price, rate, rate_count)

print(name, price, rate, rate_count)