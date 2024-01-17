import os

# 指定要处理的目录
directory = 'audio/wav'

# 定义一个函数，将数字转换为英文单词
def number_to_words(num):
    digit_to_word = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    return ' '.join(digit_to_word[digit] for digit in num if digit.isdigit())

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    # 去掉文件扩展名
    name_without_ext = os.path.splitext(filename)[0]
    # 将文件名前四个字符转换为英文单词
    words = number_to_words(name_without_ext[:4])
    # 添加文件名的后两个字母，字母之间添加一个空格
    words += ' ' + name_without_ext[-2] + ' ' + name_without_ext[-1]
    # 打印原始的文件名和转换后的单词，所有字符都转换为大写
    print(f"{name_without_ext} {words}".upper())
    