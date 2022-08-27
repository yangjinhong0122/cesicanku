# from selenium import webdriver

# xpath:
# 1、绝对路径：/html/body/div/div/div[1]/a/b   --根节点，顺序性，继承关系  --失效
# == 面试不说，工作不用
# 2、相对路径：只靠自己的特征定位   // 开头 -- 加上我关心节点的标签名
# ==标签名+属性 =//标签名[@属性名=属性值]
# //input[@id="username"]  --xpath表达方式
# 3、获取页面文本：text
#
# 2、层级定位:
# //标签名[@属性值]//标签名[@属性名=届性值]
# -//div[@class="login-logo"]//b
#
# 3、文本属性定位://b[text()=“柠檬ERP"]
#
# 4、包含属性值://标签名[contains(@属性名/text(),属性值]
# ---//input[contains(@class,"username")]

