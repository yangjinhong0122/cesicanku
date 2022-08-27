

# 1.1、元素可以是任意的数据类型：int   float   bool   str   list  ...
# list1 =[20,3.14,True,"七木"，"荷花鱼"，[1,2,3,4]]    #空列表
#
# 1.2、收值:素引取值--类比字符串
# 取多个值:切片     print(list1[3:5])
# 扩展:列丧的嵌套收值		print(list[5][1])

list1 =[20,3.14,True,"七木","荷花鱼",[1,2,3,4]]
print(list1)
print(list1[3])
print(list1[3:5])
print(list1[5][1])

# 、列表的元素是可以被改变的!   --增加，修改，剔除
# #增加
# list1.append("焕蓝")	#默认追加元素到列表的末尾	-P1
# list1.insert(5,"kingo")	#指定位置迸行元素插入	--P2
# list1.extend(["十又" ,""kingo", "陌上寸草","大丑"]〉#两个列表合并--P3
# print(list1 )

list1.append("焕蓝")
list1.insert(5,"kingo")
list1.extend(["十又","kingo","陌上寸草","大丑"])
print(list1)

# #删除
# list1.pop(0)	#默认鹏除最后一个元素，也可以拊定位置（索引）进行鹏除
# list1.remove (3.14)		#指定元素本身进行驱除
# #list1.clear()	#清除所有元素
# print (list1)
#
# #修改--取值-重新赋值
# list1[4]= "Amiee"
# print(list1)

list1.pop()
print(list1)
list1.pop(0)
print (list1)
list1.remove (3.14)
print(list1)
# list1.clear()
print(list1)
list1[4]= "Amiee"
print(list1)

# 1.4、列表的元素是可以重复的   --统计个数count()
# list1.append ("方方士")
# print (list1)
# print (list1.count ("方方士"))
#
# 1.5、len() ---统计元素个数
# print(len(list1))

list1.append ("方方士")
print (list1)
print (list1.count ("方方士"))
print(len(list1))


# 2、元祖：tuple,（）
#
# 2.1、元素可以是任意的是数据类璧: int  float	bool	str	list	tuple.. .
# tuple1 = ('方方士'，'七木'，'荷花值'，'kingo'，'Amice'，'焕蓝'，'十又'，'bingo'，'陌上寸草'，'大丑')
#
# 2.2、取值:索引取值--类比字符串
# 收多个值:切片
# 扩展:列表的嵌套取值
#
# 2.3、元组的元素是不可以被改变的!     tuple1[-1] ="小丑"---不可以
#
# 2.4、元组的元素是可以重复的---统计个数--count	print(tuple1.count('大丑'))
#
# 2.5、len () ----统计元素个数
#
# 2.6、list和tuple的互相转换
# list1 = list(tuple1)#把元组转化为列表
# list1[-1] ="小丑"
# print(list1)
# tuple2 = tuple(list1)
# print(tuple2)

tuple1 = ('方方士','七木','荷花值','kingo','Amice','焕蓝','十又','bingo','陌上寸草','大丑')
print(tuple1)
list1 = list(tuple1)#把元组转化为列表
list1[-1] ="小丑"
print(list1)
# tuple2 = tuple(list1)
# print(tuple2)


# 3.3、字典是没有顺序的!!--不能用索引取值- 取值:通过key取value
dict1 = { "name":"tan","height":"173","weight":"160"}  #空字典
print (dict1[ "height"])	#key--value 1
print (dict1.get ( "weight"))	#key-- value2
dict1["weight"]= "150"		#key存在，修改对应key 的value
print(dict1)
#
# #增加
dict1 ["age"] =18   	#key不存在，新增加键值对
print (dict1)
dict1.update({"city":"北京","hobby":"学习python","gender":"male"})#字典的合并
# #删除
dict1.pop ( "weight")	#指定key删除对应的键值对
print(dict1)
# #del dict1		#变最存储	删除--对象不存在了
# # print (dict1)




# 4、集合: set{}，元素单个   --了解
# 4.1、无序
# 4.2、元素不可以重复—使用场景:去重
list2 = [ 11,22,11,33,11,11]#去重
set1 = set(list2)		#set() --list2转化为集合
print(set1)
list3 = list(set1)		#list() --set1转化为列表
print (list3)


# 判断: if 语法
# if条件:---成立（bool值True）---冒号:缩进（4个空格=tab键）
# 子代码（执行语言）
# elif条件:---成立
# 执行语句（子代码〉
# ... (elif可以没有，可以有多个)
# else(后面没有条件):--可以没有
# 执行语句

money = int(input("请输入你的余额:"))    # input(）控制台输入--数据类型--字符串
if money >= 500:		#False
    print("买别墅!")
elif money >= 200:
    print("买一栋楼!")
elif money >= 50:
    print("买车!")
else:
    print("滚去工作赚饯!")



