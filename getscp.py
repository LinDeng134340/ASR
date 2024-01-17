import os

# 指定要处理的目录
directory = './audio/wav'

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    # 获取文件的完整路径
    file_path = os.path.join(directory, filename)
    # 打印文件路径
    print(file_path)