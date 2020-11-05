
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

#지정한 위치로 스크롤 내리기 (java) (1080으로 스크롤 내리기)
# browser.execute_script("window.scrollTo(0, 1080)") # 1080은 pc의 해당도의 세로 높이.
# browser.execute_script("window.scrollTo(0, 2080)")

#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2 

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height

# print("스크롤 완료")


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
# print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    
    if original_price:
        original_price = original_price.get_text()

    else:
        # print(title, " < 할인되지 않은 영화 제외 >")
        continue
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    link = "https://play.google.com"+link

    print(f"제목 : {title}")
    print(f"할인전 가격 : {original_price}")
    print(f"할인 후 가격 : {price}")
    print(f"링크 : {link}")
    print("-"*200)

browser.quit()
