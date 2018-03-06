#Authon :teddy
'''import sys
# 路径  打印环境变量
print (sys.path)
print(sys.argv)  #打印绝对路径'''
# ['C:\\Users\\Teddy\\PycharmProjects\\demo\\day2',
#  'C:\\Users\\Teddy\\PycharmProjects\\demo',
#  'C:\\Users\\Teddy\\PycharmProjects\\demo\\venv\\Scripts\\python35.zip',
#  'C:\\Users\\Teddy\\PycharmProjects\\demo\\venv\\DLLs',
#  'C:\\Users\\Teddy\\PycharmProjects\\demo\\venv\\lib',
#  'C:\\Users\\Teddy\\PycharmProjects\\demo\\venv\\Scripts',
#  'C:\\Users\\Teddy\\AppData\\Local\\Programs\\Python\\Python35\\Lib',
#  'C:\\Users\\Teddy\\AppData\\Local\\Programs\\Python\\Python35\\DLLs',
#  'C:\\Users\\Teddy\\PycharmProjects\\demo\\venv',
#  'C:\\Users\\Teddy\\PycharmProjects\\demo\\venv\\lib\\site-packages',
#  'C:\\Users\\Teddy\\AppData\\Roaming\\JetBrains\\PyCharm 2017.3\\helpers\\pycharm_matplotlib_backend']


import os

# cmd_res=os.system("dir") #zhixing命令，不保存结果

cmd_read=os.popen("dir").read

print (cmd_read)

# 编译性语言：效率高  java、python是一个先编译，
# 后解释的一种语言程序执行速度快，同等条件下对系统要求较低，
# 因此像开发操作系统、大型应用程序、数据库系统等时都采用它，
# 像C/C++、Pascal/Object Pascal（Delphi）等都是编译语言

# 解释性语言：没有编译过程（python  ruby）解释一句，执行一句。
# JavaScript、VBScript、Perl、Python、Ruby、MATLAB 等等


# pyc编译结果，然后执行