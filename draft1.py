
import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(chrome_options=chrome_options,service_log_path='NUL')
# 'https://utdallas.joinhandshake.com/stu/postings?page=1&per_page=25&sort_direction=desc&sort_column=created_at&job.student_screen.disable_majors=true&job.student_screen.disable_school_years=true&job.student_screen.disable_graduation_date=true&job.student_screen.disable_work_auth=true&job.student_screen.disable_gpa=true&job.job_types%5B%5D=6&qualified_only=false'
driver = webdriver.Chrome()
url = 'https://utdallas.joinhandshake.com/login'
driver.get(url)

driver.find_element(By.XPATH,'//*[@id="sso-name"]').click()
#login
driver.find_element(By.XPATH,'//*[@id="netid"]').send_keys('username')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('password')
driver.find_element(By.XPATH,'//*[@id="submit"]').click()
driver.implicitly_wait(10)
cookies = driver.get_cookies()
pickle.dump(cookies, open("cookies.pkl","wb"))

#inside Handshake
driver.find_element(By.XPATH,'//*[@id="permanent-topbar"]/div/div/div[1]/div/div/nav/div/div[1]/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="postings-filters"]/div/div/div/div[2]/button[4]/div/span').click()
driver.find_element(By.XPATH,'//*[@id="advanced-filters-body"]/fieldset/div/span/button[2]/div').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'/html/body/reach-portal/div[3]/div/div/div/div[3]/div/div/button').click()
driver.find_element(By.XPATH,'//*[@id="skip-to-content"]/div[3]/div/div[1]/div/form/div[2]/div/div/div[1]/div[1]/div/div[2]/div/button/span').click()
driver.find_element(By.XPATH,'/html/body/main/div[3]/div/div[1]/div/form/div[2]/div/div/div[1]/div[1]/div/div[2]/div/ul/li[3]/a').click()
driver.implicitly_wait(10)
time.sleep(2)



#after applied filters
'''
driver.find_element(By.XPATH,'').click()
driver.find_element(By.XPATH,'//*[@id="submit"]').click()
driver.find_element(By.XPATH,'//*[@id="submit"]').click()
driver.find_element(By.XPATH,'//*[@id="submit"]').click()
'''
while(True):
    pass
