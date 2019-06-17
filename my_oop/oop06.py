"""
    多态,运算符重载
    抽象：通过abc模块的ABCMeta元类和装饰器来达到抽象类的效果
"""
from abc import ABCMeta, abstractmethod


class Animal(object, metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def shout(self):
        pass

    def __add__(self, other):
        if isinstance(other, Animal):
            return f'{self.name}--{other.name}'
        else:
            return 'error:不是同类对象'


class Dog(Animal):

    def shout(self):
        print('WongWongWong!')


class Cat(Animal):

    def shout(self):
        print('MiaoMiaoMiao!')


def animal_shout(a):
    if isinstance(a, Animal):
        a.shout()


# unknown_animal = Animal('???') 无法创建该抽象类
# TypeError: Can't instantiate abstract class Animal with abstract method
if __name__ == "__main__":
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
