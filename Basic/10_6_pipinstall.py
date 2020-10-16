from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#인스톨 pip install beautifulsoup4
#업그레이드 pip install --upgrade beautifulsoup4
#언인스톨 pip uninstall beautifulsoup4