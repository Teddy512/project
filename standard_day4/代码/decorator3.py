__author__ = "Alex Li"

def foo():
    print('in the foo')
    def bar():
        print('in the bar')

    bar()  #再执行函数bar（）
foo()   #先执行函数foo（）

# in the foo
# in the bar