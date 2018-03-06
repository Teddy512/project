# __author__ = "Alex Li"
# import copy
#
# person=['name',['saving',100]]
# '''
# p1=copy.copy(person)
# p2=person[:]
# p3=list(person)
# '''
# p1=person[:]
# p2=person[:]
#
# p1[0]='alex'
# p2[0]='fengjie'
#
# p1[1][1]=50
#
# print(p1)
# print(p2)

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120),
]

# 利用enumerate()会更加直接和优美：
# 如果对一个列表，既要遍历索引又要遍历元素时，首先可以这样写：
list1 = ["这", "是", "一个", "测试"]

for index, item in enumerate(product_list):
    print(index, item)
    break

    # 如果要统计文件的行数，可以这样写：

    count = len(open(filepath, 'r').readlines())



# 这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。
#
# 可以利用enumerate()：

count = 0
for index, line in enumerate(open(filepath, 'r')):
     count += 1