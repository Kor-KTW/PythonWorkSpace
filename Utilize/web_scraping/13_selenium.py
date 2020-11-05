# selenium : 웹페이지 테스트 자동화를 할 수 있는  유용한 frame work
# pip install selenium
from selenium import webdriver
import time
browser = webdriver.Chrome("./chromedriver.exe") # 경로지정
browser.get("http://naver.com")
#  browser.get("http://naver.com") 
#  elem = browser.find_element_by_class_name("link_login") 
#  browser.back()
#  browser.foward() 
#  browser.forward() 
#  browser.refresh()
# elem = browser.find_element_by_id("query") 
# from selenium.webdriver.common.keys import Keys -> 키보드 접근.
# elem.send_keys("나도코딩") -> import Keys 없이도 사용가능.
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_tag_name("a")
# elem = browser.find_elements_by_tag_name("a")
# for e in elem:
#   e.get_attribute("href")
#  browser.get("http://daum.net") 
# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# browser.back()
# elem.send_keys("나도코딩")
# elem = browser.find_element_by_xpath("//*[@id="daumSearch"]/fieldset/div/div/button[2]")
# elem.click()
# browser.close() -> 탭 닫기
# browser.quit() -> 전체 닫기


#네이버 로그인 하기
elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")
browser.find_element_by_id("log.login").click()

# 같은 element에 대한 값을 초기화 해야함. 안그러면 중복되서 나옴.
browser.find_element_by_id("id").clear()

time.sleep(3)
browser.find_element_by_id("id").send_keys("my_id")

#html 정보 출력.
print(browser.page_source)

#브라우저 종료
browser.quit()