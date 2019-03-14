"""
异常的自定义和抛出：
class ****Exception(Exception):
    pass
定义一个学生类，私有属性gender，提供对应的设置值及访问值的方法

"""
# 异常类定义


class GenderException(Exception):
    def __init__(self):
        super().__init__()
        self.err_msg = "性别只能设置为男、女、male、female、man、woman"


class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = self.gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender == 'man' \
                or gender == 'woman'\
                or gender == 'male' \
                or gender == 'female'\
                or gender == '男' \
                or gender == '女':
            self.__gender = gender
        else:
            # 抛出（性别）异常
            raise GenderException

    def show_info(self):
        print('我叫{0}，性别{1}'.format(self.name, self.__gender))


stu1 = Student('yy', 'male')
stu1.show_info()
try:
    stu1.gender = 'unknown'
except Exception as e:
    print(type(e))
    print(e.args)
    print(e.err_msg)
finally:
    stu1.show_info()
print(stu1.gender)
print(type(stu1.gender))
