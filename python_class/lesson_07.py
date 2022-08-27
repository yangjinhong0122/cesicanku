from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_page(username,password,driver):
    driver.find_element(by=By.ID,value='username').send_keys(username)
    driver.find_element(by=By.ID,value='password').send_keys(password)
    driver.find_element(by=By.ID,value="btnSubmit").click()


def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element(by=By.XPATH,value='//span[text()="基本资料"]').click()
    time.sleep(3)
    driver.find_element(by=By.XPATH,value='//span[text()="会员信息"]').click()
    # 获取元素
    p_id = driver.find_element(by=By.XPATH,value='//div[text()="会员信息"] /..').get_attribute("id")
    f_id=p_id+"-frame"
    # 通过ID进行iframe切换
    driver.switch_to.frame(f_id)
    driver.find_element(by=By.ID,value="searchSupplier").send_keys(s_key)
    # 找文本
    driver.find_element(by=By.XPATH,value='//span[text()="查询"]').click()
    time.sleep(3)
    aa=driver.find_element(by=By.XPATH,value='//tr[@id="datagrid-row-r1-2-0"]//td[@field="telephone"]/div').text
    print(aa)