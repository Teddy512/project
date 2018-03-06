#authon :teddy
import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print ('the func run time is %s'%(start_time-stop_time))
    return warpper

@timmer    #装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。在Python中一般callable对象都是函数，
def test1():
    time.sleep(3)
    print ('in the test1')

test1()


# from functools import wraps
#
# def logging(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         """print log before a function."""
#         print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
# @logging
# def say(something):
#     """say something"""
#     print "say {}!".format(something)
#
# print say.__name__  # say
# print say.__doc__ # say something
# class Car(object):
#     def __init__(self, model):
#         self.model = model
#
#     @logging  # 装饰实例方法，OK
#     def run(self):
#         print "{} is running!".format(self.model)
#
#     @logging  # 装饰静态方法，Failed
#     @staticmethod
#     def check_model_for(obj):
#         if isinstance(obj, Car):
#             print "The model of your car is {}".format(obj.model)
#         else:
#             print "{} is not a car!".format(obj)
#
# """
# Traceback (most recent call last):
# ...
#   File "example_4.py", line 10, in logging
#     @wraps(func)
#   File "C:\Python27\lib\functools.py", line 33, in update_wrapper
#     setattr(wrapper, attr, getattr(wrapped, attr))
# AttributeError: 'staticmethod' object has no attribute '__module__'
# """
