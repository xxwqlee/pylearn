# ？？？？？？？？？？？？？？？
class A:

    def a_say(self):
        print('A:', self)


class B(A):

    def b_say(self):
        A().a_say()
        A.a_say(self)
        super().a_say()   # super()方法调用父类的定义
        print('B:', self)


A().a_say()
B().b_say()
B().a_say()

