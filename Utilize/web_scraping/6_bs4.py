import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()
 
soup = BeautifulSoup(res.text, "lxml") # 우리가 가져온 html을 lxml을 통해서 beautifulsoup으로 만든다.

# 페이지에 대한 이해가 높은 경우

# print(soup.title)
# print(soup.title.get_text())

# print(soup.a) # soup 객체에서 첫번째로 발견되는 a element 출력.
# print(soup.a.attrs) # a element의 속성정보 출력.
# print(soup.a["href"]) # a element의 href 속성 '값' 출력
 
# 페이지에 대한 이해가 없는 경우 아래와 같이 원하는 객체의 class, element 이름 등의 특징을 이용하여 찾을 수 있음.


# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class가 Nbtn_upload인 a element 찾기
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class가 Nbtn_upload인 첫번째로 나오는 어떤 element 찾기

# print(soup.find("li", attrs={"class":"rank01"})) # tag명이 li, class명이 rank01
# rank1 = soup.find("li", attrs={"class":"rank01"})
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())
# print(rank1.a.get_text()) # 그 중  tag가 a인 녀석
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank3 = rank2.find_previous_sibling("li")
# print(rank2.a.get_text())
# print(rank1.find_next_siblings("li"))
webtoon = soup.find("a", text="연애혁명-323. 마음의 저울")
print(webtoon)
#<a onclick="nclk_v2(event,'rnk*p.cont','570503','2')" href="/webtoon/detail.nhn?titleId=570503&amp;no=327" title="연애혁명-323. 마음의 저울">연애혁명-323. 마음의 저울</a>