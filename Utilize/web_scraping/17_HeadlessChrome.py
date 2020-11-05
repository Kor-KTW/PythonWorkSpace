# 크롬을 띄우지 않고 크롬을 사용할 수 있는, 백그라운드에서 동작하는 크롬.

from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)
interval = 2 

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height

browser.get_screenshot_as_file("google_movie.png")
soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

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
