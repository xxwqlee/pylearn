# 多态,运算符重载
class Animal:

    def __init__(self, name):
        self.name = name

    def shout(self):
        print('shout')

    def __add__(self, other):
        if isinstance(other, Animal):
            return '{0}--{1}'.format(self.name, other.name)
        else:
            return 'error:不是同类对象'


class Dog(Animal):

    def shout(self):
        print('wongwongwong!')


class Cat(Animal):

    def shout(self):
        print('miaomiaomiao!')


def animal_shout(a):
    if isinstance(a, Animal):
        a.shout()


td = Dog('TuDou')
pj = Cat('PJ')
# 多态polymorphism
animal_shout(td)
animal_shout(pj)
# 运算符重载
print(td + pj)

# 测试特殊属性
print(dir(td))
print(pj.__dict__)
print(pj.__class__)
print(Dog.__bases__)
print(Dog.mro())
print(Cat.__mro__)
print(Animal.__subclasses__())
