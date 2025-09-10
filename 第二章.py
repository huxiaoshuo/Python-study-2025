
'''
a=100
print(a)
'''

#这样子可以注释
'''
这样就是多行注释
'''

#2.2数据类型
#0b   二进制
#0o   八进制
#0x   十六进制

'''
print(0x123)
print(0o123)
print(0b111)   
0x后面跟的是对应的进制
输出的是十进制
'''


#浮点数
'''
f1 = 1.23
f2 = 1.01e4
print("f1=",f1)
print('f2=',f2)
'''

#虚数
'''
f1 = 1 + 2j
f2 = 3 + 4j
f3 = f1 + f2
print(f3)
print(f3.real)
print(f3.imag)
'''


#字符串
#双引号单引号括起来的都是字符串
'''
想要换行的话



'''
#example='''这种单引号装引号都可以
#只要回车就能换行
#'''
#print(example)


#布尔类型
#True False
'''
f1 = bool (1)
f2 = bool (0)
print(f1,f2)

'''
#注意，True False 首字母要大写
#true false会被识别成变量

#type()函数
'''
整形 class 'int'
浮点数 class 'float'
复数 class 'complex'
字符串 class 'str'
布尔类型 class 'bool'

f1 = int (1)
f2 = float (1)
f3 = complex (1 + 1j)
f4 = 'f4'
f5 = bool (1)


f6 = type(f1)
f7 = type(f2)
f8 = type(f3)
f9 = type(f4)
f10 = type(f5)

print(f6,f7,f8,f9,f10)
'''

#float int str 三者之间可以通过转换，就用对应名称就可以，直接舍弃小数，没有四舍五入

#算数运算符

'''
+加
-减
*乘
/除
//整除
%取余（模运算）
**x的y次幂
+加本身
-自己的负值
考试中出现询问算术运算符的数量时
9 为正确答案
'''

'''
a = 11
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(+a)
print(-a)

''' 



'''
字符串的运算符
str1 = "字符串1"
str2 = '字符串2'
print(str1 + str2)
很可惜python不能自动转换数据类型
所以str1 + 123 这种情况
会报错...

x = 10
print(str1 * x)
'''

#赋值运算符、增强赋值运算符
'''
a = 100
b = 50
print(a,b)
a, b = b, a
print(a,b)



print("a的值为",a)
发现空格了吗，所以我们需要
print("a的值为"+str(a))
'''

'''
x=15

print(x)
x += 1
print(x)
x -= 1
print(x)
x *= 2
print(x)
x /= 2
print(x)
x //= 2
print(x)
x %= 2
print(x)
x **= 2
print(x)
记住直接print(x += 1)会报错

'''

#关系运算符
'''
<小于
>大于
<=小于等于
>=大于等于
==等于
!=不等于

x=1
y=2

z = (x < y)
print(z)
z = (x > y)
print(z)
z = (x <= y)
print(z)
z = (x >= y)
print(z)
z = (x == y)
print(z)
z = (x != y)
print(z)
'''


#逻辑运算符
'''
not  非   取反bool
and  与   只要有false 就false
or   或   只要有true  就true

x = 1
y = 2
print(x == y)
print(x != y)
print(not x == y)
print(x == y and x == y)
print(x == y and x != y)
print(x != y and x != y)
print(x == y or x == y)
print(x == y or x != y)
print(x != y or x != y)


'''



#()可以用作优先级设置




#input()


'''
a = input("请您输入")
input默认输入的是str
print(type(a))
想要整形或者浮点数的话
a = int(input("请您输入"))
print(type(a))




'''


