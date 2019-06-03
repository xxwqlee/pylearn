"""
    继承调用关系
"""


class A:

    def a_say(self):
        print('执行A:', self)


class B(A):

    def b_say(self):
        A.a_say(self)  # 效果与下面的语句相同
        super().a_say()  # super()方法调用父类的定义,
        # 默认传入当前对象的引用self
        A().a_say()  # 类对象的直接使用，先创建一个类对象A
        print('执行B:', self)


a = A()
b = B()
a.a_say()
b.a_say()
print("*" * 50)
b.b_say()  # 仍然引用子类实例化的对象
print("*" * 50)
B().b_say()
