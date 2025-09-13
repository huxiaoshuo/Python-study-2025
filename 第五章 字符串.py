'''
字符串 操作符

+ x与y连接
* 复制y次x
in 如果y是x的字迹,返回True


s1 = 'hello'
s2 = 'world'
s3 = 3
print(s1 + s2)
print(s1 * s3 + s2 * s3)
print('orl' in s1)
print('orl' in s2)

'''

'''
字符串索引


字符串索引
索引用来表示字符串中字符的所在位置基于位置
可以快速找到其对应的字符如果一个字符串中有 n个字符
那么索引的取值范围是 0~n-1
<字符串或字符串变量>[索引]

s1 = "how are you"
print(s1[0])
print(s1[3])

*****从零开始数*****

'''


'''
字符串切片

使用切片可以获取字符串指定索引区间的字符
<字符串或字符串变量>[开始索引:结束索引:步长]

不包含结束索引

s1 = "how are you"

print(s1[3:6])
# 从字符串s1中第三个到第六个,不包含第六个

print(s1[1:])
#从字符串s1中第一个开始,直到最后一个字符


print(s1[3:10:2])
#从字符串s1中第三个到第十个,不包含第十个,每隔一个(步长为2)取一个。
print(s1[3:100:2])
#没有的默认为空，不会输出

print(s1[:])
#输出s1

print(s1[::-1])
#逆序排列s1 并输出


print(s1[-1])
#输出倒数第一个
print(s1[-2])
#输出倒数第二个
print(s1[:-2])
#输出直到倒数第二个（倒数第二个也输出）
'''


'''
for循环(遍历循环)

可迭代对象,如字符串,列表,元组,字典等可以用来遍历循环的数据


for <循环变量> in <可迭代对象>
    <循环体>

s = 'How are you'
for i in s:
    print(i)

i逐次基于s中的每一个字符

for i in range(10)
i逐次给予0-9十个数
'''

'''
s = 'Hello World'
for i in s:
    if i == 'W':
        break
    print(i)
到W就停下来,不输出W




s = 'Hello World'
for i in s:
    if i == 'W':
        continue
    print(i)
跳过W


'''




'''
字符串函数

len(x) 
返回字符串x的长度,
也可返回其他组合数据类型的元素个数


str(x)
返回任意类型x所对应的字符串形式


chr(x)
返回 Unicode 编码x对应的单个字符


ord(x)
返回单字符x表示的 Unicode 编码


hex(x)
返回整数x对应十六进制数的小写形式字符串
就是直接转成十六进制

oct(x)
返回整数x对应八进制数的小写形式字符串
就是直接转成八进制

s = 'Hello World'
a = 97
print(len(s))
print(str(a))
print(chr(a))
print(ord('a'))
print(hex(20))
print(oct(20))
'''


'''
字符串常用处理方法

方法
str.lower() 
返回字符串 str的副本
全部宇符小写


str.upper()
返回字符串 str的副本
全部字符大写


str.split(sep=None)
返回一个列表
由str根据sep被分割的部分构成
省略sep默认以空格分隔
会输出一个列表

str.count(sub)
返回 sub 子串出现的次数


str.replace(old, new)
返回字符串 str的副本
所有 old 子串被替换为 new


str.center(width, fillchar)
字符串居中函数
flchar参数可选


str.strip()
从字符串str中去掉在其左侧和右侧chars中列出的字符


str.join(iter)
将 iter 变量的每一个元素后增加一个str 字符串




s1 = 'AAA How are YOU'

print(s1)
print(s1.lower())
print(s1.upper())
print(s1.split(' '))
print(s1.count('A'))
print(s1.replace('A' , 'B'))
print(s1.center(20,'-'))
#字符串长度变为20，空出来的用后面那个填充，如果填一个小于s1长度的，会直接输出原s1
print(s1.strip('AAA'))
#去除左右的指定参数
print('.'.join('python'))
#每一个元素后面都加一个.



'''

'''
补充
capitalize()
将字符串的首字母大写

index(sub,begin,end)
返回sub在当前字符串中第一次出现的位置
如果没找到
报错

find(sub,begin,end)
返回find在当前字符串中第一次出现的位置
如果没找到
返回-1
'''


'''
format()
初始化输出

<模板字符串>.format(<参数列表>)
模块字符串是一个由字符串和槽组成的字符串
用来控制字符串和变量的显示效果
槽用{}表示
与format()中的参数列表对应



rint("{} today is a good day".format('xiaoming say'))
xiaoming say today is a good day
#format里面的代替了{}

print("{0} today is a good day,but toaday is {1}".format('xiaoming say','bad day'))
print("{1} today is a good day,but toaday is {0}".format('xiaoming say','bad day'))
默认一一对应
0开始递增


print("{} today is a good day,but toaday is {}".format('xiaoming say'))
两个槽一个值会报错，
但是
print("{0} today is a good day,but toaday is {0}".format('xiaoming say'))
就没事
'''


'''
format()方法的格式控


{<参数序号>:<格式控制标记>}

:<填充><对齐><宽度><,><精度><类型>



<填充> n
用于填充的单个字符

<对齐> <^>
<左对齐   >右对齐   ^居中对齐

<宽度> n
槽的设定输出宽度
数字的千位分隔符适用于整数和浮点数

<精度>.n
浮点数小数部分的精度或字符串的最大输出长度

<类型>
整数类型b c d o x X浮点数类型e E f %
b整数二进制
c整数对应Unicode字符
d整数十进制形式
o整数八进制形式
x整数小写十六进制形式
X整数大写十六进制形式

e浮点数对应的小写字母e指数形式
E浮点数对应的大写字母e指数形式
f浮点数
%浮点数百分比格式








可以空，但是有数的话就要按顺序



print('{:=>25}'.format('你好'))
print('{0:{1}^25}'.format('成绩',1))



print("{:=^25,}".format(123456789))

print("{:=^25,.5}".format(13.1415926))
print("{:=^25,.5f}".format(13.1415926))
print("{:=^25,.5f}".format(131415926))
'''

