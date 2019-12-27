# 面向对象编程
## self
#### 相当与C++的this指针，一个对象可以生成无数个类，当一个对象的方法被调用的时候，对象会将自身作为第一个参数传给self参数，这个时候python就能知道是哪个对象在调用方法了，也就是：self就是谁调用它，self就是谁，即指向你正在使用的对象。
```py
class Ball:
    def setName(self,name):
            self.name = name
    def kick(self):
            print('我叫%s,该死的，谁踢我。。。'%self.name)

a = Ball()
a.setName('球A')
b = Ball()
b.setName('球B')
c = Ball()
c.setName('土豆')

a.kick()
c.kick()
```
> 类里没有name这个属性，也可以直接赋值。

> 类里面的变量（属性）是公有变量（属性），即使没有定义，也可以直接赋值，而对象可以有私有变量（属性）。

> 新建一个对象a，也可以直接赋值a.age = 5。

> 在类的方法内使用类的属性变量，需要：self.变量名

> 因为py使用普通变量不需定义，在方法内不加self. 的话会被当成普通变量

> 这种普通变量不是类共有的，是方法私有的，不可以类外访问，其他方法也不能用
## __init__(self,parameter1,parameter2,...)方法
#### init方法在对象被创造的时候就会被自动调用
```py
class Ball():
    def __init__(self,name)
            self.name = name
    def kick(self):
            print('我叫%s，该死的，谁踢我。。。'%self.name)

b = Ball('土豆')
b.kick()
```
## 共有和私有
#### 私有变量只能被调用，不能被外部修改
#### python的私有是伪私有，它的类没有权限控制，变量可以被外部调用。
```py
class Person:
    __name = '小甲鱼'
    def getName(self):
            return self.__name

p = Person()
p.__name
p._Person__name
```
