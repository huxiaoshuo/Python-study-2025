'''
day2 20250911

条件为bool类型,为True时才执行语句块。
'''


'''
单分支

if <条件>:
    <语句块>

python的换行十分重要

score = float(input('请输入一个成绩'))
if score >= 80:
    print('成绩优秀！')
if score >= 60 and score < 80:
    print('成绩良好！')
'''


'''
双分支

if <条件>:
    <语句块>
else:
    <语句块>


balance = 10000
money = float(input('请输入取款金额'))
if money <= balance :
    if money % 100 == 0:
        print("请稍等")
    if money % 100 != 0:
        print('本取款机只可以取出100元纸币!') 
else:
    print('余额不足')

'''

'''
多分枝
if <条件>:
    <语句块>
elif <条件>:
    <语句块>
...
else:
    <语句块>

    
只有上一个if判断失败后,才会往后继续判断
所以 >80  
     <80 and >60
和
> 80
> 60

是一样的

score = float(input('请输入一个成绩'))
if score >= 80:
    print('成绩优秀！')
elif score >= 70:
    print('成绩良好！')
elif score >= 60:
    print('成绩及格！')
else:
    print('不及格')
'''

'''
无限循环
while <条件>:
    <语句块>

i = 10
while i>0 :
    print('好'*i)
    i -= 1

这里i-=1的位置很重要


i = 100
sum = 0
while i>0:
    sum = sum+i
    i -= 1
print(sum)
'''



'''
continue 和 break
continue 用来结束当前本次循环
continue 后面的内容不会执行然后继续执行下一次循环。

break 用于终止所在的循环



i = 0
while i <= 100:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)

count = 0
i = 0
while i <= 100:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)
    count += 1
    if count == 5:
        break



'''



'''
异常处理
try - except

try:
    <语句块1>
except:
    <语句块2>

try:
    score = float (input ('请输入一段数字'))
    print(score)
except:
    print('输入的是非数字')


try:
    a = 5
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("除以零了！！")
except:
    print("出错了")
'''
