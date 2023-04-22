import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
uurl = 'https://utdallas.joinhandshake.com/stu/postings?page=1&per_page=25&sort_direction=desc&sort_column=created_at&job.student_screen.disable_majors=true&job.student_screen.disable_school_years=true&job.student_screen.disable_graduation_date=true&job.student_screen.disable_work_auth=true&job.student_screen.disable_gpa=true&job.job_types%5B%5D=6&qualified_only=false'
url = 'https://utdallas.joinhandshake.com/login'
driver.get(url)

cookies = pickle.load(open("cookies.pkl","rb"))

for cookie in cookies:
    cookie['domian'] = '.joinhandshake.com'
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(e)

driver.get(uurl)

while(True):
    pass