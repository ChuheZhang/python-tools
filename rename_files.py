import os
import datetime

# 获取当前日期和路径
today = datetime.datetime.today()
path = ''  # 文件路径

if not os.path.exists(path):
    print(f"路径 {path} 不存在")
    exit()

# 读取文件夹中的文件名
original_name = os.listdir(path)

for i in original_name:
    start_index = 0  # 从文件名开头开始寻找 '22'
    while True:
        # 找到 '22' 的位置
        x = i.find('22', start_index)
        if x == -1:  # 如果找不到 '22'，退出循环
            print(f"文件 {i} 中没有符合条件的 '22'，跳过")
            break
        # 检查 '22' 后的字符是否是 '级'
        if x + 2 < len(i) and i[x + 2] == '级':
            # 如果是 '级'，继续寻找下一个 '22'
            start_index = x + 2
            continue
        
        # 找到合适的 '22'，生成新文件名
        new_name = f"{today.month}月{i[x - 2:x + 3]}信息反馈报告.xlsx"
        # 重命名文件
        os.rename(os.path.join(path, i), os.path.join(path, new_name))
        print(f"文件 {i} 已重命名为 {new_name}")
        break  # 退出 while 循环，处理下一个文件
