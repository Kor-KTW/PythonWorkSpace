import requests
from bs4 import BeautifulSoup
url = "https://play.google.com/store/movies/top"
headers = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     #f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)