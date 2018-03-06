#authon teddy
# def foo():
#     print ('in the foo')
# foo()
# 函数可以在函数里面 调用
#
# def bar():
#     print ('in the bar')
# def foo():
#     print ("in the foo")
#     bar()
# foo()



import time
def bar():
    time.sleep(2)
    print ('in the bar')

def test1(func):
    start_time=time.time()
    func()   #他的作用是？  函数执行到这会调用bar
    stop_time=time.time()
    print ('the func run time is %s'%(stop_time-start_time))
test1(bar)
bar()