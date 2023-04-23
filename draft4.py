from dotenv import load_dotenv
import os
import pickle
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
#driver = webdriver.Chrome(chrome_options=chrome_options,service_log_path='NUL')
driver = webdriver.Chrome()
url = os.getenv('URL')
url2 = os.getenv('URL2')
url3 = os.getenv('url3')
username = os.getenv('username')
password = os.getenv('password')
driver.get(url3)
cookie_expired = False
cookies = pickle.load(open("cookies.pkl","rb"))


# Check if the cookies are expired
for cookie in cookies:
    if 'expiry' in cookie:
        expiry = datetime.fromtimestamp(cookie['expiry'])
        if expiry < datetime.now():
            print(f"Cookie {cookie['name']} is expired!")
            cookie_expired = True

#login if expired
if(cookie_expired):
    driver.find_element(By.XPATH,'//*[@id="sso-name"]').click()
    driver.find_element(By.XPATH,'//*[@id="netid"]').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH,'//*[@id="submit"]').click()
    driver.implicitly_wait(10)
    cookies = driver.get_cookies()
    pickle.dump(cookies, open("cookies.pkl","wb"))
    print("New Cookies are Dumped")

#login using cookies
for cookie in cookies:
    cookie['domian'] = '.joinhandshake.com'
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(e)

print('Login Successful')
driver.get(url3)

#driver.implicitly_wait(10)
#inside Handshake
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/main/div[3]/div/div[1]/div/form/div[2]/div/div/div[2]/div[1]/div[1]/h1/a').click()
#time.sleep(10)
driver.implicitly_wait(30)
job = driver.find_elements(By.CLASS_NAME,'style__content___3pUVU')
for value in job:
    print(value.text)


while(True):
    pass
