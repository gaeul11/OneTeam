from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriver 자동 관리
service = Service(executable_path=ChromeDriverManager().install())

# 옵션 설정 예 (headless 모드)
options = webdriver.ChromeOptions()
options.headless = True  # GUI 없이 실행

# 드라이버 초기화
driver = webdriver.Chrome(service=service, options=options)

# 웹 페이지 열기
driver.get('https://devyihyun.tistory.com/30')

# 요소 찾기 및 데이터 추출
try:
    route = '//*[@id="mArticle"]/div[2]/h3'
    element = driver.find_element('xpath', route)  # 요소 찾기

    print(element.text)  # 텍스트 추출
finally:
    driver.quit()  # 드라이버 종료