#authon :teddy
import time
def consumer(name):
    print ("%s 准备吃包子！"%name)
    while True:
        baozi=yield
        print ("包子[%s]来了，被[%s]吃了"%(baozi,name))

c=consumer("teddy")
c.__next__()
b1="韭菜"
c.send(b1)
# c.__next__()







# send方法中的应用



def producer(name):
    c=consumer('A')
    c2=consumer('B')
    c.__next__()#执行下一步
    c2.__next__()
    print ("包子")
    for i  in range(10):
        time.sleep(3)
        print ("做了一个包子，分两边")
        c.send(i)
        c2.send(i)
producer("teddy")
