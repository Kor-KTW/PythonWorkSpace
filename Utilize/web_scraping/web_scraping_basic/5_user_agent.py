#request로 데이터를 받아올 때, user의 agent에 따라서 차단하는 경우가 있는데, 헤더를 이용하여 agent를 변경시켜주면 제대로된 데이터를 가져올 수 있음
import requests
url = "http://nadocoding.tistory.com"
headers = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("Utilize/web_scraping/web_scraping_basic/study.html", "w", encoding="utf8") as f:
    f.write(res.text)
