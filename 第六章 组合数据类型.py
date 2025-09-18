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
集合类型-set {}
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


创建空集合只能用t = set()和 t= set({})
'''


'''
序列类型

序列类型用来存储有序并且可以重复的数据，分别为以下两种类型类型
列表(list)
元组(tuple)

'''


'''
列表-list []
ls = ['s', 's', 'r', 666, 666]
print(ls)
print(type(ls))
'''


'''
列表类型-列表索引
索引用来表示列表中元素的所在位置
基于位置，可以快速找到其对应的列表元素
如果一个列表中有n个字符
那么案引的取值范国是0~n-1
<列表或列表变量>[索引]

ls = ['s', 's', 'r', 666, 666]
print(ls[0])
print(ls[0:3])


'''


'''
ls = [1, 2, 3, '123', [1, 2, 3]]
print(ls[4])
print(ls[4][2])

'''


'''
函数

x in s
如果 x是s的元素,返回 True,否则返回 False
x not in s
如果 x不是s的元素,返回 True,否则返回 False
len(s)
返回列表 s的元素个数
min(s)
返回列表 s 中的最小元素
max(s)
返回列表 s 中的最大元素

s = [123, 234, 345]
t = ['s','ss']

print(123 in s)
print(123 not in s)
print(max(s))
print(min(s))
print(len(s))
print(max(t))
print(min(t))
print(len(t))


都可以创建空列表
ls = list
ls = []
ls = list([])
'''

'''
函数或方法
ls.append(x)
在列表 1s 末尾处理添加一个新元素x

ls.insert(i,x)
在列表 1s 第 i 位增加元素x

ls .clear()
清空列表 1s 中所有元素

1s.pop(i)
将列表 1s 中第i 个元素删除

1s.remove(x)

将列表中出现的第一个元素 x删除
1s.reverse()
将列表 1s 中的元素反转

ls.index(x)
列表 1s 中第一次出现元素x的位置

ls.count(x)
列表 1s 中出现 x的总次数返回一个新列表


1s.copy()
复制1s中所有元素


ls = [1, 2, 3, 3, 2, 1]
ls.append(1)
print(ls)
ls.insert(2,2)
print(ls)
ls.pop(3)
print(ls)
ls.remove(2)
print(ls)
ls.reverse()
print(ls)
ls1=ls.count(1)
print(ls1)
ls1 = ls.index(1)
ls2 = ls.index(2)
ls3 = ls.index(3)
print(ls1,ls2,ls3)
ls4 = ls.copy()
print(ls4)
ls4[1]=2.5
print(ls4)
print(ls)
ls.clear()
print(ls)


'''



'''
元组类型-tuple
元组一旦定义就不能修改。
元组类型使用()来表示，例:t=(123,3.14,123,"abe")

t = (123, 3.14 ,123 ,'abc')
print(t)
t1 = ()
print(t1)
print(type(t1))
'''
'''
元组可用函数
len(t)
min(t)
max(t)
ls.index(x)
ls.count(x)


'''



'''
ls = {1 ,2 ,3 ,4 ,5 ,6 ,7}
for i in ls
    print(i)

ls = [1 ,2 ,3 ,4 ,5 ,6 ,7]
ls.reverse()
for i in ls:
    print(i)

'''




'''
字典类型-字典的定义
字典类型数据主要以“键值对”的形式存储，类似汉语字典的目录形式。
具体定义格式如下
[<键1>:<值1>,<键2>:<值2>，…,<键n>:<值n>}

d = {'2000':'first', '2001':'sceond', '2002':'third'}
print(d['2000'])
d['2000'] = 'uno'
print(d['2000'])
d['2003'] = 'forth'
print(d['2003'])
'''


'''
索引函数
len()
max()
min()
查的是key ，与后面对应值无关

d = {'2aaa':'first', 'a001':'sceond', 'a002':'third'}

print(len(d))
print(min(d))
print(max(d))
'''


'''
函数或方法


d. keys
返回所有的键信息

d.values()
返回所有的值信息

d.items()
返回所有的键值对

d.get(key,default)
键存在则返回相应值，
否则返回默认值defau1t

d.pop(key, default)
键存在则删除相应键值对，
并返回相应值，
否则返回默认值defau1t

d.popitem()
随机从字典中取出一个键值对，
以元组(key,value)形式返回，
同时将该键值对从字典中删除。

d.clear()
清空字典 d 中所有键值对





d = {'000':'first', '001':'sceond', '002':'third'}


d = {'000':'first', '001':'sceond', '002':'third'}
print(d.keys())
print(d.values())
print(d.items())


for i in d:
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i[0],i[1])
#此处i为元组
for K,V in d.items():
    print(K,V)


print(d.get('003','NONE'))
print(d.get('000','NONE'))

print(d.pop('000','none'))
print(d.pop('000','already pop'))
print(d)
d['000']='first'
print(d)

d1 = d.popitem()
print(d1)
print(d)

'''
