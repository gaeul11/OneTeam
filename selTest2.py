import time

import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
url = 'https://statiz.sporki.com/stats/'
driver.get(url)
pr=driver.find_element('xpath','/html/body/div[2]/div[3]/section/div[8]/table/tbody/tr[4]')
print(pr.text)
time.sleep(5)