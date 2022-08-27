from selenium.webdriver.common.by import By
from python_class import lesson_07
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = test_data.url["url"]
user = test_data.login_data["username"]
pwd = test_data.login_data["password"]
s_key = test_data.s_key["s_key"]

lesson_07.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)