from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()


# import selenium		#工具里的所有的内容都导入
#
# from selenium import webdriver		#从selenium 工.具里导入webdriver库
#
# import time		#导入time这个模块--- Python自带的
#
# #选择chrome这个浏览器，初始化driver==可以浏览器进行沟通建立会话= session
# driver = webdriver.Chrome()
#
# #1、打开一个网址
# driver.get ( "http://120.78.128.25:8765")
#
# #2、浏览器窗口最大化
# driver.maximize_window ()
#
# #3、打开新页面
# #time.sleep(2)#等待，默认秒
# driver.get ("http://erp.lemfix.com" )
#
# #4、向前退后――刷新
# #time.sleep (2)
# driver.back ()			#退回上一个页面
# #time .sleep (2)
# driver.forward()		#前进道下一个页面
# #time .sleep(2)
# driver.refresh ()		#刷新页面
#
# #5、退出
# driver.quit()	#关闭驱动	sessionx闭
# #driver.close()		#关闭当前的窗口，不会退出会话


driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
driver.get ("http://erp.lemfix.com" )
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)


driver.find_element(by=By.ID,value='username').send_keys("15766723430")
driver.find_element(by=By.ID,value='password').send_keys("123456")
driver.find_element(by=By.ID,value="btnSubmit").click()
# test3=driver.find_element(by=By.XPATH,value='//div[@class="login-logo"]//b').text
# print(test3)
# if test3 == "柠檬ERP":
#     print("这个页面的标题是:{}".format(test3))
# else:
#     print("这条用例不通过")
#
# test4=driver.find_element(by=By.XPATH,value='//b[text()="柠檬ERP"]').text
# print(test4)
time.sleep(3)
# driver.find_element(by=By.XPATH,value='//span[text()="零售出库"]').click()
driver.find_element(by=By.XPATH,value='//span[text()="基本资料"]').click()
driver.implicitly_wait(10)
driver.find_element(by=By.XPATH,value='//span[text()="会员信息"]').click()
# 隐式等待
driver.implicitly_wait(10)


# 获取元素
p_id = driver.find_element(by=By.XPATH,value='//div[text()="会员信息"] /..').get_attribute("id")
print(p_id)
f_id=p_id+"-frame"
print(f_id )
# 通过ID进行iframe切换
driver.switch_to.frame(f_id)
driver.find_element(by=By.ID,value="searchSupplier").send_keys("15766723430")

# 找文本
driver.find_element(by=By.XPATH,value='//span[text()="查询"]').click()
time.sleep(3)
aa=driver.find_element(by=By.XPATH,value='//tr[@id="datagrid-row-r1-2-0"]//td[@field="telephone"]/div').text
print(aa)



# #找到了有username这个id的元素--点击
# driver.find_element_by_id("username" ).click()
#
# #找到了有username这个id的元素--点，输入内容
# driver.find_element_by_id ("username" ).send_keys ("15766723430")
# #找到了有password这个id的元素--点，输入内容
# driver.find_element_by_id ("password" ).send_key=("123456")
# ctrl+f的意思是元素搜索框，确认元素


