import os   
import datetime

today = datetime.datetime.today()
path = 'C:/Users/Fatin/Desktop/十二月信息反馈 - 副本/folder' #需要修改的文件所在的路径
original_name = os.listdir(path)        #读取文件夹中文件初始的名字

for i in original_name: 
    x = i.index('22') #x获取到第一个对应字符串的下标
    os.rename(os.path.join(path,i),os.path.join(path,"%d月" % today.month + i[x - 2:x + 3] + "信息反馈报告.xlsx" ))  #修改文件名