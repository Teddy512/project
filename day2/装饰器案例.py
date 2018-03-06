#authon ：teddy
# import time
# def timer(func):
#     def deco(*args,**kwargs):
#         start_time=time.time()
#         func(*args,**kwargs)
#         stop_time=time.time()
#         print ("the func run time is %s"%(stop_time-start_time))
#     return deco
#
# def test1():
#     time.sleep(4)
#     print('in the test1')
# # 使用了”@”语法糖后，我们就不需要额外代码来给”test2”重新赋值了，
# # 其实”@timer”的本质就是”test2 = timer(func):”，
# # 当认清了这一点后，后面看带参数的装饰器就简单了
# @timer
# def test2(name,age):
#     print ('test2',name,age)
# test1()
# test2("alex",22)
#
# # in the test1
# # test2 alex 22
# # the func run time is 0.0



# 案例2
# #authon teddy
#
# import time
# def deco(func):#2
#     starttime=time.time()#3
#     func()     #4 func=myfumc
#     endtime=time.time()   #9
#     msecs=(endtime-starttime)*1000   #10
#     print ("elapased time:%f ms",msecs)  #11
#
#
# def myfunc():  #5
#     print ("star myfunc")  #6
#     time.sleep(2)        #7
#     print ("end myfunc") #8
#
# deco(myfunc)  #1
# myfunc()



# 案例3：
# import time
#
# def deco(func):
#     def wrapper():
#         starttime=time.time()
#         func()
#         endtime=time.time()
#         msecs=(endtime-starttime)*1000
#         print ("elapased time:%f ms",msecs)
#     return wrapper
#
# def myfunc():
#     print ("star myfunc")
#     time.sleep(0.6)
#     print ("end myfunc")
#
#
# print ("myfunc is:",myfunc.__name__)
# myfunc=deco(myfunc)
# print ("myfunc is:",myfunc.__name__)
#
# myfunc()

# 结果：
# myfunc is: myfunc
# myfunc is: wrapper
# star myfunc
# end myfunc
# elapased time:%f ms 609.3780994415283

# 装饰器语法
# 案例4：
#
# import time
#
# def deco(func):
#     def wrapper():
#         starttime=time.time()
#         func()
#         endtime=time.time()
#         msecs=(endtime-starttime)*1000
#         print ("elapased time:%f ms",msecs)
#     return wrapper
#  #的本质就是”myfunc = deco(myfunc)”
# @deco
# def myfunc():
#     print ("star myfunc")
#     time.sleep(0.6)
#     print ("end myfunc")
#
#
# print ("myfunc is:",myfunc.__name__)
#
# myfunc()


# 案例5也就是说这时，”addFunc(3, 8) = deco(addFunc(3, 8))”。
#authon teddy

# import time
#
# def deco(func):
#     def wrapper(a,b):
#         starttime=time.time()
#         func(a,b)
#         endtime=time.time()
#         msecs=(endtime-starttime)*1000
#         print ("elapased time:%f ms",msecs)
#     return wrapper
#
# @deco
# def addFunc(a,b):
#     print ("star addFunc")
#     time.sleep(0.6)
#     print ("result is %d"%(a+b))
#     print ("end  addFunc")
#
#
# addFunc(6,8)


# # 案例6  you  bug
# #authon teddy
#
# import time
# def deco(arg=True):
#   if arg:
#      def _deco(func):
# 	    def wrapper(*args,**kwargs):
#              starttime=time.time()
#              func(*args,**kwargs)
#              endtime=time.time()
#              msecs=(endtime-starttime)*1000
#              print ("elapased time:%f ms",msecs)
# 	    return wrapper
#   else:
#      def _deco(func):
#         return func
#   return _deco
#
#
#
# @deco(False)
# def myFunc():
#     print ("satrt myFunc")
#     time.sleep(0.9)
#     print ("end myfunc")
#
# @deco(True)   #的本质就是”myfunc = deco(myfunc)”
# def addFunc(a,b):
#     print ("star addFunc")
#     time.sleep(0.6)
#     print ("result is %d"%(a+b))
#     print ("end  addFunc")
#
#
#
# print ("myFunc id",myFunc.__name__)
# myFunc()
# print
# print ("addFunc is",addFunc(6,8))
# addFunc(6,8)


#authon teddy
# 装饰器是可以叠加使用的，那么这是就涉及到装饰器调用顺序了。
# 对于Python中的”@”语法糖，
# 装饰器的调用顺序与使用 @ 语法糖声明的顺序相反。
# import time
#
# def deco_1(func):
#     print ("enter the deco_1")
#     def wrapper(a,b):
#         print ("enter the deco_1  wrapper")
#         func(a,b)
#     return wrapper
#
# def deco_2(func):
#     print ("enter the deco_2")
#     def wrapper(a,b):
#         print ("enter the deco_2  wrapper")
#         func(a,b)
#     return wrapper
#
#
# @deco_1
# @deco_2
# def addFunc(a,b):
#     print ("star addFunc")
#     time.sleep(0.6)
#     print ("result is %d"%(a+b))
#     print ("end  addFunc")
#
#
# addFunc(6,8)


# enter the deco_2
# enter the deco_1
# enter the deco_1  wrapper
# enter the deco_2  wrapper
# star addFunc
# result is 14
# end  addFunc


# Python内置装饰器
#
# 在Python中有三个内置的装饰器，都是跟class相关的：staticmethod、classmethod 和property。
#
#     staticmethod 是类静态方法，其跟成员方法的区别是没有 self 参数，并且可以在类不进行实例化的情况下调用
#     classmethod 与成员方法的区别在于所接收的第一个参数不是 self （类实例的指针），而是cls（当前类的具体类型）
#     property 是属性的意思，表示可以通过通过类实例直接访问的信息
