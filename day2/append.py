names=["zhangsan","lisi","wabnger","pois"]
# 列表的功能 ：
# 增加，插入
names.append("zhangsan")
names.insert(0,"zhangsan")
# 删除
del names[0]
names.remove("zhangsan")
names.pop(0)
dd=names.copy() #浅拷贝
dd=names.copy.deepcopy(names)#深拷贝
# 修改
names[1]="lisi"
# 找人位置
pp=names.index("lisi")  #索引位置
pp=names.count("lisi")  #计数有多少个lisi
cc=names.reverse()  #反转列表
print (names[names.index("lisi")])  #打印名字


print (names[0:-1:2])  #从0到末尾，步长2
print(names[::2])#从0到末尾，步长2
print(names[:])#从0到末尾浅拷贝


# 元组tuple的功能：是只读的列表只能  count，和index功能（'1','2','3'）
# names=["zhangsan","lisi","wabnger","pois"]