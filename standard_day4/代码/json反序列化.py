__author__ = "Alex Li"
import pickle

def sayhi(name):
    print("hello2,",name)


f = open("test.text","rb")

data = pickle.loads(f.read())


print(data["func"]("Alex"))

# r：只读（默认）
# >>>f = open('youfile', 'w')
# w：只写（不存在则创建，存在则先清空）
#
# x：创建新文件并打开设置可写权限
#
# a：打开文件并设置可写权限，向文件最后追加内容
#
# b：以二进制读取文件，以字节对象读写数据，用于操作不包含文本的文件
#
# t：文本模式（默认）
#
# +：为更新而打开一个硬盘文件（可读写）
#
# r+：可读可写
# 读写文件时要考虑很多意外的情况，如，没有找到要打开的文件就会抛异常(r模式):
# >> > open('f.txt', 'r')
# Traceback(most
# recent
# call
# last):
# File
# "<stdin>", line
# 1, in < module >
# IOError: [Errno 2]
# No
# such
# file or directory: 'f.txt'
#
# 所以在读文件时要对异常进行处理：
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise


