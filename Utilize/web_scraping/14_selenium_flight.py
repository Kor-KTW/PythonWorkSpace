from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()
browser.maximize_window() #최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

# browser.find_elements_by_link_text("27")[0].click() # [0]-> 처음나오는 달 (이번달)
# browser.find_elements_by_link_text("29")[0].click() # [0]-> 처음나오는 달 (이번달)
browser.find_elements_by_link_text("27")[0].click() # [0]-> 처음나오는 달 (이번달)
browser.find_elements_by_link_text("29")[1].click() # [1]-> 처음나오는 달 (다음달)

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

browser.find_element_by_link_text("항공권 검색").click()
try:
    elem = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
finally:
    browser.quit() 
#webdriverwait을 통해 browser를 10초간 기다리는데 오버되면 에러가 뜨고 그동안에 ec에 해당하는 xpathelement가 위치할 때까지 기다리고 바로실행 가능.
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/div[4]/ul/li[1]")
# print(elem.text)
