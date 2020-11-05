
import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
goodproduct = []
for i in range(1,6):

    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())
    for item in items:
        #광고제품 제외 
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            #print("광고 상품 제외합니다.")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        rate = item.find("em", attrs={"class":"rating"})

        if "Apple" in name:
            #print("애플 상품 제외합니다.")
            continue

        if rate:
            rate= rate.get_text()
        else:
            rate = "평점 없음"
            #print("평점 없는 상품을 제외합니다.")
            continue
            
        rate_count = item.find("span", attrs={"class":"rating-total-count"})
        if rate_count:
            rate_count = rate_count.get_text()[1:-1] #ex:(26)
        else:
            rate_count = "평점 수 없음"
            #print("평점 수 없는 상품을 제외합니다.")
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_count) > 100:
            print(name, price, rate, rate_count)
            print(f"제품 명 : {name}")
            print(f"가격: {price}")
            print(f"평점 : {rate}")
            print(f"리뷰 수 : {rate_count}")
            print(f"링크 : https://www.coupang.com/{link}")
            print("-"*200)

            info = str(name+" "+price+" "+rate+" "+rate_count)
            # print(info)
            goodproduct.append(info)

        # elif float(rate) >=4.0:
        #     #print("리뷰 수가 부족한 상품을 제외합니다. (리뷰 수 : {})".format(rate_count))

        # elif int(rate_count)>50:
        #     #print("평점이 부족한 상품을 제외합니다. (평점 : {})".format(rate))
        # else:
        #     #print("평점과 리뷰 수가 부족한 상품을 제외합니다.(리뷰 수 : {}, 평점 : {})".format(rate_count, rate))
print(" - - 조건을 만족하는 상품 리스트 - - ")
for data in goodproduct:
    print(data)  