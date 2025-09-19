'''

文件的类型



文本文件
-般由单一特定编码的字符组成
如Unicode编码
内容容易统一展示和阅读
由于文本文件存在编码
可以看作是存储在磁盘上的长字符串
如一个txt 格式的文本文件
二进制文件



直接由0和1组成
没有统一的字符编码
文件内部数据的组织格式与文件用途有关
如png格式的图片文件、mkv格式的视频文件




区别:是否有统一的字符编码

'''


'''
文件的操作-打开文件
变量名>= open(<文件路径及文件名>,<打开模式>)


打开模式
'r'
只读模式，
如果文件不存在，
返回异常 FileNotFoundError，
默认值

"w'
覆盖写模式，文件不存在则创建，存在则完全覆盖原文件

'x'
创建写模式，
文件不存在则创建，
存在则返回异常FileExistsError

'a'
追加写模式，
文件不存在则创建，
存在则在原文件最后追加内容

'b'
二进制文件模式

't'
文本文件模式，默认值

'+'
与 r/w/x/a 一同使用，在原功能基础上增加同时读写功能



文件的操作-常用组合
以文本方式只读打开一个文件，读入后不能对文件进行修改:r
以文本方式可读写地打开一个文件，可以读入并修改文件:r+
以文本方式打开一个空文件，准备写入一批内容，并保存为新文件:w
以文本方式打开一个空文件或已有文件，追加形式写入一批内容，更新原文件:a+
以二进制方式只读打开一个文件，读入后不能对文件进行修改:rb


'''



'''
文件的操作-读
方法
f.read(size)
从文件中读入整个文件内容。
参数可选，
如果给出，
读入前size长度的字符串或字节流

f.readline(size)
从文件中读入一行内容。
参数可选，
如果给出，
读入该行前size长度的字符串或字节流

f .readlines (hint)
从文件中读入所有行，
以每行为元素形成一个列表。
参数可选，
如果给出读入hint行

f.seek(offset)
改变当前文件操作指针的位置，
offset的值:0为文件开头;
1为从当前位置开始;
2为文件结尾

相对路径
相对于当前编写的代码的位置
a/b
绝对路径
path = 'E:/Python study 2025/teach.txt'



\n 换行
\t tab
\\ \



path = 'E:/Python study 2025/teach.txt'
f = open(path,'rt',encoding='utf-8')
s = f.read()
f.close()
print(s)

path = 'E:/Python study 2025/teach.txt'
f = open(path,'rt',encoding='utf-8')
s = f.read(3)
f.close()
print(s)

path = 'E:/Python study 2025/teach.txt'
f = open(path,'rt',encoding='utf-8')
s = f.readline(2)
print(s)
s = f.readline()
f.close()
print(s)


path = 'E:/Python study 2025/teach.txt'
f = open(path,'rt',encoding='utf-8')
s = f.readlines(1)
print(s)
f.close()
print(type(s))



path = 'E:/Python study 2025/teach.txt'
f = open(path,'rt',encoding='utf-8')
s = f.read()
print(s)
f.seek(0)
s = f.readlines()
print(s)
f.close()
'''


'''
写

f.write(s)向文件写入一个字符串或者字节流


f.witrlines(lines) 将一个元素为字符串的列表整体写入文件


path = 'E:/Python study 2025/new.txt'
f = open(path,'w')
f.write('明天就要考试了\n')
f.write('希望可以过\n')
f.write('20250919')
f.close()


f = open(path,'a')
f.write('明天就要考试了\n')
f.write('希望可以过\n')
f.write('20250919')
f.close()
'''

'''
一维数据



二维数据




'''
'''
path = 'E:/Python study 2025/excel.csv'
f = open( path , 'w' )
a = ['1','2','3']
s = ','.join(a)
print(s)
f.write(s)
f.close()

f = open( path , 'r' )
info = f.read()
f.close()
ls = info.split(',')
print(ls)

'''
a = [
['1','2','3','4'],
['5','6','7','8']
]
print(a)
path = 'E:/Python study 2025/excel.csv'
f = open(path ,'w')
for row in a:
    s = ','.join(row)
    print(s)
    print(type(s))
    f.write(s+ '\n')
