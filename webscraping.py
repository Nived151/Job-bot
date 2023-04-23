import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(chrome_options=chrome_options,service_log_path='NUL')

driver = webdriver.Chrome()
url = 'https://utdallas.joinhandshake.com/login'
driver.get(url)

title = driver.find_element(By.CLASS_NAME ,'marketing-title')
print(title.text)

while(True):
    pass