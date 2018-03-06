#authon：teddy

'''
Python其实有3个方法,即静态方法(staticmethod),
 类方法(classmethod)和
 实例方法,如下
 '''
def foo(x):
    print ("executing foo(%s)"%(x))

class A(object):
    def foo(self,x):
        print ("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print ("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x)
a=A()
'''
这里先理解下函数参数里面的self和cls.
这个self和cls是对类或者实例的绑定,
对于一般的函数来说我们可以这么调用foo(x),这个函数就是最常用的
,它的工作跟任何东西(类,实例)无关.对于实例方法,
我们知道在类里每次定义方法的时候都需要绑定这个实例,就是foo(self, x),
为什么要这么做呢?因为实例方法的调用离不开实例,
我们需要把实例自己传给函数,调用的时候是这样的a.foo(x)
(其实是foo(a, x)).类方法一样,只不过它传递的是类而不是实例,
A.class_foo(x).注意这里的self和cls可以替换别的参数,
但是python的约定是这俩,还是不要改的好.

对于静态方法其实和普通的方法一样,不需要对谁进行绑定,
唯一的区别是调用的时候需要使用a.static_foo(x)或者A.static_foo(x)来调用.

'''

编程题
1
台阶问题 / 斐波那契

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)

第二种记忆方法


def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)


第三种方法


def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return b


2
变态台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

fib = lambda n: n if n < 2 else 2 * fib(n - 1)

3
矩形覆盖

我们可以用2 * 1
的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 * 1
的小矩形无重叠地覆盖一个2 * n的大矩形，总共有多少种方法？

第2 * n个矩形的覆盖方法等于第2 * (n - 1)
加上第2 * (n - 2)
的方法。

f = lambda n: 1 if n < 2 else f(n - 1) + f(n - 2)

4
杨氏矩阵查找

在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

使用Step - wise线性搜索。

def get_value(l, r, c):
    return l[r][c]


def find(l, x):
    m = len(l) - 1
    n = len(l[0]) - 1
    r = 0
    c = n
    while c >= 0 and r <= m:
        value = get_value(l, r, c)
        if value == x:
            return True
        elif value > x:
            c = c - 1
        elif value < x:
            r = r + 1
    return False


5
去除列表中的重复元素

用集合

list(set(l))

用字典

l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = {}.fromkeys(l1).keys()
print
l2

用字典并保持顺序

l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print
l2

列表推导式

l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = []
[l2.append(i) for i in l1 if not i in l2]

sorted排序并且用列表推导式.

l = ['b', 'c', 'd', 'b', 'c', 'a', 'a'][single.append(i)
for i in sorted(l) if i not in single] print single
6
链表成对调换

1->2->3->4
转换成2->1->4->3.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head


7
创建字典的方法
1
直接创建

dict = {'name': 'earth', 'port': '80'}

2
工厂方法

items = [('name', 'earth'), ('port', '80')]
dict2 = dict(items)
dict1 = dict((['name', 'earth'], ['port', '80']))

3
fromkeys()
方法

dict1 = {}.fromkeys(('x', 'y'), -1)
dict = {'x': -1, 'y': -1}
dict2 = {}.fromkeys(('x', 'y'))
dict2 = {'x': None, 'y': None}

8
合并两个有序列表

知乎远程面试要求编程

尾递归


def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)


def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])

    循环算法


思路：

定义一个新的空列表

比较两个列表的首个元素

小的就插入到新列表里

把已经插入新列表的元素从旧列表删除

直到两个旧列表有一个为空

再把旧列表加到新列表后面


def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp

    pop弹出


a = [1, 2, 3, 7]
b = [3, 4, 5]


def merge_sortedlist(a, b):
    c = []
    while a and b:
        if a[0] >= b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c


print
merge_sortedlist(a, b)
