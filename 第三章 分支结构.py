'''
day2 20250911
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



