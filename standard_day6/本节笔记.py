# __author__ = "Alex Li"
#
# 面向对象介绍
#
# 世界万物，皆可分类
# 世界万物，皆为对象
#
# 只要是对象， 就肯定属于某种品类
# 只要是对象，就肯定有属性
#
#
# 你是上帝
#
# 地球
#
# 山川，河流，大海，森林，
#
# 飞禽  飞， 吃虫子，下蛋，
# 布谷鸟    唱歌
# 乌鸦
#
# 几百种鸟
#
#
#
# 走兽，
#
# 狮子 森林之王
# 老虎  百兽之王
#
#
#
#
# 臭鱼烂虾，
#
# 人，思考，说话， 吃喝拉撒睡，

'''

'''
# 特性
# class
# object
#
# 封装
# 继承
# 多态
#
# 语法
#
# 调用函数  --》 执行 --》返回结果
#
# r1 = Role.__init__() return x342423
#
# r1 = Role(r1,"Alex","Police","15000")
# r1.name = "Alex"
# r1.role = "Poice"
# r1.money = 15000
# r1.buy_gun() # Role.buy_gun(r1)



# 属性
# 方法
# 类变量的用途? 大家共用的属性 ,节省开销
# class Person:
#     cn = "中国"
#     def __init__(self,name,age,addr,cn="china")
#         self.name = name
#         self.cn = cn
# p1 = Person(name,age ,addr)
# #
# 构造函数

# 析构函数： 在实例释放、销毁的时候自动执行的，通常用于做一些收尾工作， 如关闭一些数据库连接，关闭打开的临时文件

# 私有方法，私有属性
#
# 类变量
# 实例变量


# 封装

# 继承
# py2 经典类是按深度优先来继承的，新式类是按广度优先来继承的
# py3 经典类和新式类都是统一按广度优先来继承的
#
# 多态
# 一种接口，多种实现

# 面向对象
'''面向对象编程相对于面向过程编程和函数式编程来说，看的更长远，实现功能相对更简单。
面向对象：对象就是物体，这种编程思想就是设定一个有一定功能的物体，然后利用这个物体的功能做你想做的事情。（这个物体有attributes
，比如名字啊，年龄啊等等等等，有methods，比如吃喝拉撒睡等等等等，功能＝＝methods）
'''
'''
面向过程：你想干嘛，就直接写个功能，然后做你想做的事情。
假如你想写个程序去洗衣店洗衣服，面向对象就是设定一个人，把这个对象赋予拿衣服，搭车，交易，取衣服，回家这所有的过程的功能。当你想洗衣服的时候，创造这个对象的实例出来，然后命令他去做就好了。
面向过程：你就得写拿衣服，搭车，交易，取衣服，回家这所有的过程。实现这一个功能感觉和面向对象编程的思想差不多，但是如果你下一次还想洗衣服，就得再写一遍这个过程，假如会有很多次洗衣服，那就得写更多次，很麻烦，易出错。

'''
# 三大特性：封装、继承、多态。
''' 封装
 封装是从业务逻辑中抽象对象时，
 要赋予对象相关数据与操作，
 将一些数据和操作打包在一起的过程。
 封装是使用对象的主要魅力之一，它提供了一个简单方法来创建复杂方案
 ，解决了世界是如何工作的这一问题，
我们自然的认为周围的世界是由相互作用的对象组成，
 每个对象都有自己相关的数据，并能完成一定的功能，
 从设计的角度来看，封装还提供了一个重要的服务，
 它分开了是什么和怎么做这两个问题。对象的实现与使用是相互独立的，
封装的另外一个优势是支持代码复用，它可以将常用功能以组件方式打包起来。
'''

# 封装
# private
#   封装就是把类中的属性和方法定义为私有的，方法就是在属性名或方法名前加双下划线，而一旦这样定义了属性或方法名后，python会自动将其转换为_类名__属性名（方法名）的格式，在类的内部调用还是用双下划线加属性名或方法名，在类的外部调用就要用_类名__属性名（方法名）。
# 父类的私有属性和方法，子类无法对其进行修改。
''' 封装的优点

    1. 良好的封装能够减少耦合。

    2. 类内部的结构可以自由修改。

    3. 可以对成员变量进行更精确的控制。

    4. 隐藏信息，实现细节。
'''
'''
封装分为两个层面：

第一层面的封装：创建类和对象时，分别创建两者的名称空间。只能通过类名加“.”或者obj.的方式访问里面的名字

第二层面的封装，类中把某些属性和方法隐藏起来，或者定义为私有，只在类的内部使用，在类的外部无法访问，或者留下少量的接口(函数)供外部访问
'''
'''
但无论是哪种层面的封装，都要对外提供好访问内部隐藏内容的接口。

在python中，使用双下划线的方式实现隐藏属性(设置成私有属性)。

在python中，隐藏类的属性用什么办法呢？？'''
'''
我们家里都有电视机，从开机，浏览节目，换台到关机，
我们不需要知道电视机里面的具体细节，只需要在用的时候按下遥控器就可以完成操作，
这就是功能的封装。

在用支付宝进行付款的时候，
只需要在用的时候把二唯码给收款方或是扫一下收款方提供的二唯码就可以完成支付，
不需要知道支付宝的支付接口，以及后台的处理数据的能力，这就是方法的封装。
'''


# 在编程语言里，对外提供接口，表示这个接口的函数，通常称为接口函数






# 封装包括两点，把内容封装到某个地方；调用封装的内容
class c1:
    def __init__(self,name,obj):
        self.name = name
        self.obj = obj
class c2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name)
        return 123
class c3:
    def __init__(self, a1):
        self.money = 123
        self.aaa = a1
c2_obj = c2('aa', 11)
# c2_obj是c2类型
# - name = "aa"
# - age = 11
c1_obj = c1("alex", c2_obj)
# c1_obj 是c1 类型
# - name = "alex"
# - obj = c2_obj
c3_obj = c3(c1_obj)
# 使用c3_obj执行show方法
ret = c3_obj.aaa.obj.show()
print(ret)
print(c3_obj.money)

# aa
# 123
# 123
# 我定义了3个类，每个类都有自己的构造方法__init__,我对每一个类都进行实例化一个对象；每个对象创建的时候会自动调用自己的__init__方法封装不同的内容；
#
# self是一个形式参数，他就相当于实例，比如当c1_obj=c1('alex',c2_obj),self就等于c1_obj
#
# 当我们输出money这个字段的时候，c3_obj可以调用show这个方法输出money（间接调用self）或者直接输出c3_obj.money(直接调用）
#
# 对象本身也可以当做参数传给其他的类

# 没有封装时候的写法
class Teacher:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def teach(self):
        print("%s is teaching"%self.name)

class Student:
    def __init__(self,name,age,group):
        self.name=name
        self.age=age
        self.group=group

    def study(self):
        print("%s is studying"%self.name)


'''
用所定义的类创建一个老师s1和一个学生s1。

t1=Teacher("alex",28,"python")
s1=Student("jack",22,"group2")

分别调用老师和学生的姓名，年龄等特征：

print(t1.name,t1.age,t1.course)
print(s1.name,s1.age,s1.group)

返回如下的信息：

alex 28 python
jack 22 group2

调用老师的教书技能和学生的学习技能：

t1.teach()
s1.study()

返回信息如下：

alex is teaching
jack is studying
'''


# 封装起来例子   java 中的封装就是set和get方法封装
'在python中，使用双下划线的方式实现隐藏属性(设置成私有属性)'
class Teacher:
    def __init__(self,name,age,course):
        self.__name=name
        self.__age=age
        self.__course=course

    def teach(self):
        print("%s is teaching"%self.__name)

class Student:
    def __init__(self,name,age,group):
        self.__name=name
        self.__age=age
        self.__group=group

    def study(self):
        print("%s is studying"%self.__name)


'''
创建老师和学生的实例：

t1=Teacher("alex",28,"python")
s1=Student("jack",22,"group2")

再用前面一样的方法调用老师和学生的特征：

print(t1.name,t1.age,t1.course)
print(s1.name,s1.age,s1.group)

此时这样调用就会报错，输出信息如下所示：

Traceback (most recent call last):
  File "E:/py_code/oob.py", line 114, in <module>
    print(t1.name,t1.age,t1.course)
AttributeError: 'Teacher' object has no attribute 'name

再调用老师的教书技能和学生的学习技能：

t1.teach()
s1.study()

返回信息如下：

alex is teaching
jack is studying

可以看到隐藏属性后，再像以前那样访问对象内部的属性，就会返回属性错误，那现在要怎么才能访问其内部属性呢？
现在来查看t1和s1的名称空间



print(t1.__dict__)
{'_Teacher__name': 'alex', '_Teacher__age': 28, '_Teacher__course': 'python'}
print(s1.__dict__)
{'_Student__name': 'jack', '_Student__age': 22, '_Student__group': 'group2'}

可以看到t1和s1的名称空间完全改变了，现在访问t1名称空间里的key，可以看到什么呢？？

print(t1._Teacher__name)
print(t1._Teacher__age)
print(t1._Teacher__course)

返回如下：

alex
28
python

这次没有报错了，看来隐藏属性之后可以通过"_类名__属性"的方式来访问其内部的属性值，
来得到和隐藏属性之前，直接查看其内部属性一样的值。

python对于这样的隐藏，有一些特点：
1.类中定义的_X吸能在内部使用，如self._X,引用的就是变形之后的结果。
2.这种变形其实正是对外部的改变，在外部是无法通过_X这个名字访问到的。

事实上，python对于这一层面的封装，需要在类中定义一个函数。
这样在类的内部访问被隐藏的属性，在外部就可以使用了，而且这种形式的隐藏并没有
真正意义上的限制从外部直接访问属性，知道了类名和属性名一样可以调用类的隐藏属性。

python并不会真的阻止开发人员访问类的私有属性，模块也是遵循这种约定。
很多模块都有以单下划线开头的方法，此时使用

from module import *

时，这些方法是不会被导入的，此时必须要通过

from module import _private_module
'''