# 字符串的操作:
# 1、取值:元素位置--索引，从o开始，依次加1
# 2、取多个值:切片--[开始;结束:步长]—-=取头不取尾

# 开始头--省略=默认从o开始  结束--省略==默认末尾结束  步长--省略=默认为1
# 3、负数:从右边开始取
# -1--最后一个

str1 = "hello world!"
print(str1[9])
print(str1[0:7:5])
print(str1[-1])


# input()---内置函数:在控制台输入数据--赋值给num这个变量
# 3、元素个数：len()--- 内置函数：统计元素个数（长度）
print(len(str1))
print(str1[0:len(str1):5])

# 替换字符串里面元素：replace（）
str1 = str1.replace("world","tricy")
print(str1)

# 5、找到这个元素对应的索引：index（） 、 find（）
#print(str1.index("G"))#如果元素没有找到--会报错，代码终止运行
# print (str1.find ( "G"))#如果元素没有找到-不会报错，返回-1

print(str1.index("h"))
print(str1.index("l"))
print(str1.find("h"))
print(str1.find("l"))
print(str1)

# 统计个数：count（）
# 7、格式化输出
# 第一种：.format()
# 1、占位符：{} -- 传 变量的地方   .format()
# 2、.format()  可以默认按顺序传入变量   也可以指定位置传入变量
#
name = "yang1"
age = 18
hobby = "蹦迪"
print('''---{}---
name:{} 
ageg:{}
hobby:{}
'''.format(name,name,age,hobby))

# 8、Python运算符：
# 1、算数运算符：+ - * / %  **
# print(10 + 20 ) ---#两个数字相加
print(10+10)
print("love"+"tricy")
# 两哥个字符串拼接
print(str(123) + "adc")
# print(str(123)+ "adc" ) ---#int --> str : str() -- 强制字符串的转化，内置函数
# int()--整型 float() bool()
print("love" * 10)
print(10 / 2)#结果浮点型

#
# 2、赋值运算符：=  +=  -=  ：方向性  -- 右边的赋值给左边的
# a = 10
# a += 10  #== a = a + 10
# a -= 5   # a = a - 5
# print (a)
# 2、比较运算符： <  <=  >  >=  ==   !=   -- 运算结果是布尔值 True False
# print(2 < 3)  -- 打印结果为True
# print(2 > 3)  -- 打印结果为False
# print("登录成功"!="登录成功")  #判断字符串是否相同 === 执行结果vs预期结果
#
#
# 3、逻辑运算符： 与--and == 真真为真  或--or == 假假为假 非-- not
#
# 4、成员运算符： in    not in
# str2="Python"
# print("p" in str2) --执行结果为真


