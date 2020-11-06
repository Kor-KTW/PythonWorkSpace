import requests
from bs4 import BeautifulSoup
import re 
def print_news(index, title, link):
    print("{}. {}".format(index, title))
    print("  (링크 : {})".format(link))    

def create_soup(url):
    headers = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    cast = soup.find("p", attrs="cast_txt").get_text()
    print(cast)

    curr_temp = soup.find("span", attrs="todaytemp").get_text() + "℃"
    min_temp = soup.find("span", attrs="min").get_text().replace("˚","℃")
    max_temp = soup.find("span", attrs="max").get_text().replace("˚","℃")

    m_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    a_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    dust = soup.find("dl", attrs={"class":"indicator"}).find_all("dd")
    mise = dust[0].get_text()
    cho_mise = dust[1].get_text()
    print(cast)
    print("현재 {} ( 8최저 {} / 최고 {} )".format(curr_temp,min_temp,max_temp))
    print("오전 {} / 오후 {}".format(m_rain_rate, a_rain_rate))
    print()
    print("미세먼지 {}".format(mise))
    print("초미세먼지 {}".format(cho_mise))
    print()

def scrape_headline():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        # print("{}. {}".format(index+1, title))
        # print("  (링크 : {})".format(link))
        print_news(index+1, title, link)

def scrape_IT():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)
    news_list = soup.find_all("div", attrs={"class":"cluster_text"}, limit=3)
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        # print("{}. {}".format(index+1, title))
        # print("  (링크 : {})".format(link))
        print_news(index+1, title, link)

def scrape_eng():
    print()
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print()
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline()
    scrape_IT()
    scrape_eng()