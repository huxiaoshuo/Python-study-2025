'''
import
import <模块名> as <别名> from . 

import from<模块名> import<对象、函数...>
'''

'''
python 标准库

内置函数

abs() 绝对值

pow(x , y) 返回x的y次幂

divmod (a,b) 返回a和b的商及余数

round (x) 四舍五入
'''

'''

a = 5
b = 2

c = divmod (a,b)
print(c)
print(type(c))
'''


'''
组合类型变量函数
all(x)  所有元素都为真返回True x为空,返回True
any(x)  有任一元素为真时返回True x为空,返回True
rebersed(r) 返回x的逆序
sorted(x) 对x排序,默认从小到大
sum(x) 求和

'''

'''
eval(s)  计算字符串s作为Python表达式的值   就是去掉双引号
exec()  计算字符串s作为Python语句的值   去掉语句的双引号
range(a,b,s)   从a到b,s为步长  不包括b


value = eval(input('你好，输入一个数字'))
print(value)
print(type(value))
'''

