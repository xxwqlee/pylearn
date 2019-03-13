# Design Pattern 工厂模式，单例模式
class ComputerFactory:

    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self):
        if self.__init_flag:
            print('init ComputerFactory')
            self.__init_flag = False

    def create_computer(self, brand):
        if brand == '联想':
            print(self.__init_flag)
            return Lenovo()
        elif brand == '华硕':
            print(self.__init_flag)
            return ASUS()
        elif brand == '神舟':
            print(self.__init_flag)
            return Hasee()
        else:
            print('无法生产该品牌')
            print(self.__init_flag)


class Computer:

    def __init__(self):
        self.str_c = 'is calculating'

    def calculate(self):
        print(self, self.str_c)


class Lenovo(Computer):
    pass


class ASUS(Computer):
    pass


class Hasee(Computer):
    pass


fac = ComputerFactory()
c1 = fac.create_computer('联想')
c2 = fac.create_computer('神舟')
c3 = fac.create_computer('惠普')
c1.calculate()
