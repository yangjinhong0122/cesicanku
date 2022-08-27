# for循环:遍历数据对象里的所有元素:str	list	tuple 	dict
# for  变量名 in  数据对象:
# 子代码（循环体）
# 循环多少次由什么决定的？---元素个数
# 中断：break    continue
#
#
# count = 0   #计数器
# list1 = ['方方士','七木','荷花鱼','kingo','Amiee','焕蓝','十又','bingo','陌上寸草','大丑']
# for name in list1:
# # #不打印“荷花鱼”
# # if name == "荷花鱼":    #False(结果为false不执行里面语句)
# # break		--#跳出整个循环
# # continue	--#跳出本次循环
#     print(name)
#     count += 1	#每次循环+1
# print(count)	#打印循环次数
# print(len(list1))	#打印列表长度

# 2、range()  --内置函数：生成一个整数序列：1,2,3,4,5,6
# 跟 for 循环一起使用：start（开始）（默认值为0），stop（结束），step（步长）--取头不取尾
# for i in range(1:5:1)
# prtint(i)	--打印1,2,3,4



# 3、函数:封装成函数，调用。===提高代码的复用率，提高执行的效率
# 语法:
# def函数名():
# 子代码（函数体）--实现功能
# 注意：函数只定义了  没有调用  不会执行：如何调用？  --写函数名
#
# 函数里不固定的数据--定义成函数的参数--括号里
# 1、形参--函数定义的时候定义的
# 2、实参:调用函数传入参数
#
# 参教定义的类型:
# 1、必备参数:定义了就必须要传入的参数--不传会报错
# 2、默认参数（缺省参数）:可以定义的时候赋值一个默认值--调用的时候可以不传入；可以传-替换掉默认值。
# 注意：默认参数必须跟在必备参数后面！！
# 3、不定长参数：等前面的必备参数和默认参数都接受完了，剩下的参数都给不定长参数接受
# *args接受不确定数量，个数的参数 -- 可以不传，可以传入（1个、多个）
# 元组接收  传参方式：按照位置来传
# **kwargs:字典接收	传参方式：关键字传参
#
# 传多的方式类型:
# 1、位置传参:按照位置参数传入
# 2、关键字传参:指定参数名来进行传参，不关心顺序  --可靠
# 3、混合传参：注意：关键字传参必须跟在位置传参后面！
#
# #定义--两数名==函数的参数--形参-变量替代
# def good_job(salary,bonus,subsidy,*args):
#     sum1 = salary + bonus + subsidy   #sum1实现功能
#     print ("salary的值:{ }".format (salary))
#     print ("bonus的值:{ }".format (bonus))
#     print ("subsidy的值: { }".format (subsidy))
#     print ("args的值:{ }".format(args))
#     print ("kwargs的值: { } ".format (kwargs))
#     for i in args:
#         sum1 += i
#     # for j in kwargs:
#     #     print (kwargs.get(j))#通过key --取到value
#     #     sum1 += kwargs[j]
#     print("这个工作的工资总和是:{}".format (sum1 ))
# #
# # #用函数名进行函数的调用--函数才会被执行.--实参
# good_job(8000,2000,800,100,200,300)

# def good_job(salary,bonus,subsidy,*args,**kwargs):
#     sum1 = salary + bonus + subsidy
#     print("salary的值:{}".format(salary))
#     for i in args:
#         sum1 += i
#     for j in kwargs:
#         print(kwargs.get(j))
#         sum1 += kwargs[j]
#
#     print("这个工作的工资总和是:{}".format(sum1))
#     return sum1
# good_job(8000,2000,800,100,200,300,aa=50,bb=100,cc=200,dd=300)
#


# 4、有进有出:进--―参数，出--返回值
# 返回值:函数可以给到外面的人用的数据，做后续操作--调用函数的时候可以获取到这个返回值--return
# 1、定义
# 2、调用--变量接收返回值
# 3、如果没有返回值-- None，可以有 return ：可以多个--用元组保存
# 4、注意：返回值写在函数的最后 -- 标志着函数结束

#定义--函数名=函数的参数--形参-变量替代
def good_job(salary,bonus, subsidy=500, *args,**kwargs):
    sum1 = salary + bonus + subsidy#sum1实现功能
    for i in args:
        sum1 += i
    for j in kwargs:
        sum1 += kwargs[j]
    return sum1 #定义了一个返回值==两个返回值用逗号隔开
result =good_job(8000,2000,800) #用函数名进行函数的调用--函数才会被执行--实参

if result > 10000:
    print("这个是一个不借的工作!")
else:
    print("我还可以找到更好的工作!")
print(result)

#
#
# 内置函数:
# print()
# input (） -- 字符串
# type()
# instance ()
# len ()
# replace count,find indextappend insert popremove update ... --数据类型的内置方法
# str()，float() int() list() tuple() dict () bool() set()
# range() -- 整数序列
