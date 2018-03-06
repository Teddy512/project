#authon :teddy
def fib(max):
    n,a,b=0,1,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return '---done---'

f=fib(10)
#generator#### f是一个生成器函数
# yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
# Python 解释器会将其视为一个 generator，
# 调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，
# 每次循环都会执行 fab 函数内部的代码，
# 执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，
# 代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
# 于是函数继续执行，直到再次遇到 yield。
# print (f)#<generator object fib at 0x00000280E3B2B0A0>

# g=fib(6)
# while True:
#     try:
#         x=next(g)
#         print ('g:',x)
#     except StopAsyncIteration as e:
#         print ('Generator return value:',e.value)
#         break
# f.__next__()这是打印出f里面的下一位数
print("---------dddd")

print ("555555")
print(f.__next__())
print("======")
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())


print("====start loop======")
