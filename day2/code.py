#authon:teddy

# 对文件的操作读了一行以后就不能再读，除非光标移到第一行，活在这关闭重新打开

f=open("yestday",encoding="utf-8")#文件句柄
# a=append  追加
data=f.read()
print(data)