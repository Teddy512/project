#authon teddy
二、单继承与多继承

在其他语言中只支持单继承即class
类名(父类名)，而python支持多继承，用逗号将多个父类隔开即class
类名(父类名1, 父类名2,。。。。)



三、继承与抽象

抽象就是把一类事物的共有特性提取出来，
继承则是把父类的属性拿过来并且还拥有自己的属性。抽象是包含的范围越来越大，共性越来越少，
继承则是包含的返回越来越小，共性越来越多。我们定义父类的过程就是抽象，定义子类的过程就是继承。



四、父类方法重写

我们把子类有而父类没有的方法叫做子类的派生方法，而父类有子类也有的方法叫做对父类方法的重写，因为按照类方法的搜索顺序一个方法如果在子类中有就不会再从父类中找了，结果就是父类中的方法无法调用了，如果既想执行父类中的方法同时在子类中又能定义新功能，就需要先把父类中的这个方法单独继承过来，在python中只能使用父类名.方法名(
    self, 父类的其他参数)
的方式，在python3中可以使用super函数来实现，比如super().父类方法名(
    除self外的其他参数)，其实在super函数中还需要传入子类名和子类对象（在类中用self）, 但是我们使用时不需要特意去传，除非在类外单独调用父类的方法。注意在继承父类方法时父类的参数除了需要在父类的方法中传递还需要在子类重写的方法中传递


class Animal:
    def __init__(self,name,life_value,aggr):
        self.name=name
        self.life_value=life_value
        self.aggr=aggr
    def eat(self):
        self.life_value+=10

class Person(Animal):
    def __init__(self,money,name,life_value,aggr):
        super().__init__(name,life_value,aggr)
        self.money=money
    def attack(self,obj):
        obj.life_value-=self.aggr



五、接口类

   接口类是用于规范子类的方法名定义用的，继承接口类的子类可以不存在任何逻辑上的关系但是都需要实现某些共同的方法，为了让这些子类的方法名能够统一以便之后调用这些方法时不需要关注具体的对象就用接口类规范了这些方法的名字，子类一旦继承了接口类就必须实现接口类中定义的方法，否则在子类实例化的时候就会报错，而接口类本身则不需要实现去实现这些方法。
 from abc import ABCMeta,abstractmethod
 class Payment(metaclass=ABCMeta):
     @abstractmethod
     def pay(self,money):
         pass
 
 class Wechatpay(Payment):
    def pay(self,money):  #子类中必须定义接口类中有的方法，否则实例化会报错
        pass
 
 w1=Wechatpay()

六、抽象类

抽象类的作用和接口类一样，只是继承它的子类一般存在一些逻辑上的关系，且抽象类中的方法可以去实现，子类在重写时用super函数调用抽象类的方法即可，同时在用抽象类时使用单继承，使用接口类时使用多继承

七、多态

多态就是不同的对象可以调用相同的方法然后得到不同的结果，有点类似接口类的感觉，在python中处处体现着多态，比如不管你是列表还是字符串还是数字都可以使用 + 和 *。



八、封装

封装就是把类中的属性和方法定义为私有的，方法就是在属性名或方法名前加双下划线，而一旦这样定义了属性或方法名后，python会自动将其转换为_类名__属性名（方法名）的格式，在类的内部调用还是用双下划线加属性名或方法名，在类的外部调用就要用_类名__属性名（方法名）。父类的私有属性和方法，子类无法对其进行修改。



九、类的装饰器
1. 何为装饰器？

　　官方定义：装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

 　　Python中总共包括三个内置装饰器：

　　　　① staticmethod

　　　　② classmethod

　　　　③ property

property属性装饰器：将类内的方法的调用方式和属性一样，
这个装饰器还有和其配套的setter、deleter。

class Demo:
    @property
    def p(self):
        print('property func')
    @p.setter
    def p(self,num):
        print('property_setter')
    @p.deleter
    def p(self):
        print('在删除')
d=Demo()
d.p  
d.p=10
del d.p
--------------------------------------------------------------------------------------
property func
property_setter
在删除




setter对值的设置
# -*- encoding:UTF-8 -*-

class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value >= 0 and value <= 100:
            self.__score = value  # 还记得__score吗？前面加一个双下划线，表示private私有属性
        else:
            raise ValueError('score must between 0 ~ 100!')

    def age(self):
        self.__age = 26
        return self.__age


s = Student()
s.score = 90
print(s.score)
print(s.age())





staticmethod静态方法装饰器：将类内的方法变成普通的函数，或者把类外的函数放到类内当作方法调用

比如说狗，猫，猪。它们都是动物，我们就可以归为一类。
而猫，狗就是动物类中的一个对象。


class A:
    @staticmethod
    def sum():  # 这个方法跟普通函数没有区别
        print('staticmethod')


A.sum()  # 用类名调用
--------------------------------------------------------------------------------------
staticmethod



classmethod类方法装饰器：该方法用于操作类属性，无法操作对象属性




class A:
    role = 'male'

    @classmethod
    def sum(cls):  # 用于操作类属性
        print(cls.role)


A.sum()  # 用类名调用
--------------------------------------------------------------------------------------
male



十、isinstance和type的区别以及issubclass

isinstance和type都可以用于判断对象和指定类间的关系，
但是isinstance的判断没有type准确，它无法正确判断子类的对象和其父类的关系




class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))
print(type(b) is B)
print(type(b) is A)
--------------------------------------------------------------------------------------
True
True
True
False



issubclass用于判断给定的两个类，前者是否是后者的子类

十一、反射

hasattr(对象或类名，‘属性或方法名’)  判断指定的对象或类中是否存在指定的属性或方法，有返回True

getattr(对象或类名, '属性或方法名')
获取对象或类的指定属性值或方法的内存地址

setattr(对象或类名,‘新属性名’, 新属性值) 给对象或类添加新的属性或方法

delattr(对象或类名,‘新属性名’) 删除之前添加的属性

十二、类的内置方法

__doc__ ：输出类的描述信息

__module__ ：表示当前操作的对象在那个模块

__class__ ：  表示当前操作的对象的类是什么

__dict__ ：查看类或对象中的所有成员
类调用打印类的所有属性，不包括实例属性。实例调用打印所有实例属性

__str__
格式化输出 % s输出该方法的值

__repr__
格式化输出 % r输出该方法的值，并且 % s在没有__str__方法时也是输出该方法的值
__del__
del 执行该方法
__getitem__
用对象加[]
方式取值




class A:
    def __init__(self):
        self.names = ['egon', 'alex', 'eva']  # 可以是其他序列

    def __getitem__(self, item):
        print(self.names[item])


a = A()
a[1]
----------------------------------------------------------
alex



__setitem__
添加值
__delitem__
删除值
__new__
用于创建没有属性的对象，调用object的__new__即可不需要自己实现。可以利用该方法实现单例模式
__call__
对象加括号执行该方法
__len__
len()
执行该方法
__eq__ == 运算输出该方法的值

__hash__
hash执行该方