import os

# 指定要处理的目录
directory = './audio/wav'

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    # 获取文件的完整路径
    wav_file_path = os.path.join(directory, filename)
    # 替换路径中的 'wav' 为 'mfcc' 并替换文件扩展名为 '.mfcc'
    mfcc_file_path = wav_file_path.replace('wav', 'mfcc').replace('.wav', '.mfcc')
    # 打印结果
    print(wav_file_path, mfcc_file_path)