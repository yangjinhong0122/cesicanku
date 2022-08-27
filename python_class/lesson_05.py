a=[1,2,'6','summer']
# i = input("请输入：")
if '6' in a:
    print("在列表里")
else:
    print("不是")


dict1 = {"class id":46,"num":30}
print(dict1)
num1 = dict1.get("num")
if num1 > 5:
    print("班上人数是:{}".format(num1))
else:
    print("班上不足5人")

list1 = [1,1,1,1,1,1]
list2 = [2,2,2,2,2,2]
list3 = [3,3,3,3,3,3]
list4 = [4,4,4,4,4,4]
list5 = [5,5,5,5,5,5]
list6 = []
for i in range(6):
    dict1 = dict(name=list1[i],age=list2[i],sex=list3[i],hobby=list4[i],job=list5[i])
    list6.append(dict1)
print(list6)

def add_jia(num2):
    # num2 = int(input("num2输入:"))
    # print(num2)
    sum1 = 0
    for i in range(num2):
        sum1 += i
    print(sum1)
add_jia(3)

def function_len(object):
    if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):
        leng =len(object)
        if leng >=5:
            print("ture")
        else:
            print("false")
    else:
        print("数据类型bufuhe")
function_len([1,2,3,4,5,6])