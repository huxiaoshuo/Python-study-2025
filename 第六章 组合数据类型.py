'''
20250918
集合类型
-集合
序列类型
-列表
-元组
映射类型
-字典
'''



'''
集合类型-set
Python 语言中的集合类型与数学中的集合概念一致
集合用来存储**无序并且**不重复的数据
集合中元素的类型只能是不可变数据类型，如:整数、浮点数、字符串、元组等
相比较而言，列表、宇典、和集合类型本身都是可变数据类型
'''


'''
s = {123 ,456 ,3.14 , 'abc', 'abc'}
print(s)
体现无序以及不重复
print(type{s})
'''

'''
 集合操作符
s - t  返回一个集合包含在s中但是不在t中的元素
s & t  返回一个集合包含同时在s和t中的元素
s ^ t  返回一个集合包含集合s和t中非共同元素
s | t  返回一个集合包含s和t中所有元素

s = {1, 2, 3, 4, 5}
t = {3, 4, 5, 6, 7}
print(s - t) 差集
print(s & t) 交集
print(s ^ t) 补集
print(s | t) 并集


'''

'''
函数

s .add(x)
如果数据项x不在集合s中
将x添加到 s


s.remove(x)
如果 x在集合 s中
移除该元素
不在则产生 KeyError 异常


s.clear()
移除s 中所有的元素


len(s)
返回集合 s的元素个数


x in s
如果x是s的元素
返回True
否则返回Fa1se


x not in s
如果x不是s的元素
返回 True
否则返回 False

s = {1, 2, 3, 4, 5}
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
print(s)
print(5 in s)
print(5 not in s)
t = set()
print(t)
print(type(t))
'''
