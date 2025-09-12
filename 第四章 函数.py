'''
第四章函数
经常重复运用的部分,可以用函数代替
对内隐藏细节,对外暴露接口
'''



'''
函数的声明（定义）
def <函数名>(《参数列表》)
    <函数体>
    return<返回值>
'''
'''

def plus(y):
    sum = 0
    i = 1
    while i <= y:
        sum += i
        i += 1
    print(sum)

plus(50)
'''

'''
默认返回值为你给你给他的类型
def add(a,b):
    return a + b


c = add(1 ,2)
print(c)
print(type(add(1 ,2)))

d = add('你好' , '世界')
print(d)
print(type(add('你好' , '世界')))
'''

'''
多个返回值
def change(a,b):
    a,b = b,a
    return a,b
c,d = change(1,2)
print(c,d)
print(type(achange(c,d)))

'''

'''
形式参数:简称“形参”，函数定义(声明)时使用的参数。
实际参数:简称“实参”，函数被调用时实际传入的参数。
'''


'''
def change(a,b):
    a,b = b,a
    return a,b
c,d = change(1,2)

a , b为形参
1 , 2 , c ,d 为实参 

'''


'''
值传递不会影响原来的数值
def fun(a):
    a = 5
    print(a)

m = 10
fun(m)
print(m)

'''


'''
不同场景如何使用参数与返回值
无参数、无返网值
有参数、无返回值
无参数、有返回值
有参数、有返回值


输出1-100之间的和
#无参数、无返回值
def fun1():
sum=0
i= 1
while i<=100:
    sum += i
    i+=1
    print(sum)


并计算1-100之间的和,并返回
#无参数，有返回值
def fun2():
    sum=0
    i= 1
    while i<=100:
        m += i
        i += 1
    return sum


#实现传入一个成绩,判断该成绩是否及格,并输出“及格”或“不及格
#有参数，无返回值
def fun3(s):
    if s >= 60:
        print("及格”)" 
    else:
        print("不及格”)

实现传入一个成绩，判断该成绩是否及格，如果及格返回True，否则返回False
#有参数，有返回值
def fun4(s):
    if s >= 60:
        return True
    else:
        return False      
'''

'''
def<函数名>(<非可选参数列表>,<可先参数>=<默认值>):
    <函数体>
    return <返回值列表>
可选参数一定在非可选参数后面
    

def add(a , b=5):
    print(a+b)

add (10)
add (10 , 20)


'''

'''
函数变量作用域（在哪里管用）

局部变量
在函数内部定义的变量，
仅在函数内部有效，
当函数退出时变量将不再存在。


全局变量
在函数之外定义的变量，
在程序执行过程有效，
全局变量在函数内部使用时，
需要提前使用保留字 qlobal声明
语法如下:
global<全局变量>


#a和b是局部变量,因为是在函数内声明的
def fun():
    a = 10
    b = 15
    print(a, b)
print(a, b)
会报错


#函数外声明的n为全局变量,随时可以使用
n = 10
def fun():
    a = 10
    b = 15
    print(a, b)
    print(n)
print(a, b)



#函数内部与全局变量重复的会重新设置一个局部变量，不会影响全局变量的值
n = 2
def fun(a,b):
    n = a + b
    print(n)
fun (5, 6)
print(n)



若是想要影响全局变量,可以使用global语句


n = 2
print(n)
def fun(a,b):
    global n
    n = a + b
    print(n)
fun (5, 6)
print(n)
'''

'''
print 输出不换行


print(<待输出的内容>,end="<增加的输出结尾>")


a = 100
print(a,end='')
print(a,end='%')


可以看出 print函数中end部分是可选参数，默认为换行符，可以手动置空
'''
