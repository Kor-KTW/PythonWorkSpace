
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=557672&weekday=thu"

for 
res = requests.get(url)
res.raise_for_status()
 
soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
cartoonsrates = soup.find_all("div", attrs={"class":"rating_type"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]

# print(title)
# print("https://comic.naver.com"+link)

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)
total = 0

for cartoonsrate in cartoonsrates:
    rate = cartoonsrate.find("strong").get_text()
    print(rate)
    total += float(rate)
print("전체 점수 : ", total)
print("평균 점수 : ", total / len(cartoonsrates))

# https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/
print(type(cartoons))