__author__ = "Alex Li"
import random
checkcode=''
#循环六次【0，6）

# randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
for i in range(6):
    current=random.randrange(0,5)   #[0,5)
    print("current:",current)
    print ('i:',i)
    #这里是 如果当前数字和循环数字相同则输出字母65,90 is A-Z
    if current == i:
        tmp=chr(random.randint(65,90))
        print("tmp:", tmp)
    #否则输出0，9之间的数字
    else:
        tmp=random.randint(0,9)
        print("tmp:", tmp)
    #最后将循环的数字字母带出来
    checkcode+=str(tmp)
#输出结果
print(checkcode)

'''
以下展示了使用 randrange() 方法的实例：

#!/usr/bin/python
import random

# 输出 100 <= number < 1000 间的偶数
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)

# 输出 100 <= number < 1000 间的其他数
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)

以上实例运行后输出结果为：

randrange(100, 1000, 2) :  976
randrange(100, 1000, 3) :  520
'''