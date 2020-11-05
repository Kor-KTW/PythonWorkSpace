# 이와 같이 user agent 값을 설정하지 않으면 user agent 정보가 날아갈 수 있음.
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
detected_value = browser.find_element_by_id("detected_value")

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 
# (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
print(detected_value.text)
browser.quit()

# 더 공부하려면 selenium with python을 검색하면 더 자세히 공부할 수 있음.
