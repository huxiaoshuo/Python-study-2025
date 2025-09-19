

'''

pip 工具安装
自定义安装
文件安装(扩展名.whl)


·pip<命令><选项>
安装:install 库名
卸载:uninstall 库名
下载:download 库名
查看当前第三方库列表:1ist
查看某个第三方信息:show
'''


'''
jieba.lcut(s) 精确模式，返回一个列表类型
jieba.lcut(s,cut all=True) 全模式，返回一个列表类型
jieba.lcut for search(s) 搜索引擎模式，返回一个列表类型
jieba.add word(w) 向分词词典中增加新词 w



inmport jieba
ls = ['你吼！这里是文字测试，测试为国家计算机考试二级！']
ls2 = jieba.lcut(ls)


requests  简单处理HTTP请求
scrapy web获取框架

数据分析：
nupmy 科学计算库
scipy 在numpy基础上添加库函数
pandas 数据处理 数据分析

文本处理：
pdfminer 读取 pdf数据
openpyxl 处理 Excel 表格
python-docx 处理 word 文档
beautifulsoup4 解析和处理 HRML、XML


数据可视化方向
matplotlib 二维图绘制
TVTK 三维可视化
mayavi  更方便的三维可视化

用户图形界面方向
库名
PyQt 5 用户图形界面开发
wxPython 用户图形界面开发
PyGTK 用户图形界面开发

机器学习方向
scikit-learn 机器学习
TensorFlow 人工智能
Theano 深度学习

Web 开发方向
Django web 框架
Pyramid web 框架
Flask web 框架

游戏开发
Pygame 多媒体制作
Handa3D 3D 引擎
cocos2d 2D 引擎



PIL 图像处理
SymPy 数学计算
NLTK 自然语言处理
WeRoBot 微信机器人框架
MyQR 二维码








'''

import jieba 

ls2 = jieba.lcut('测试为国家计算机考试二级')
print(ls2)