# 测试@property的使用
class Employee:

    @property
    def print_demo(self):
        print('salary is 9999')
        return 10001

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):   # 相当于salary属性的getter方法
        return self.__salary

    @salary.setter
    def salary(self, salary):   # 相当于salary属性的setter方法
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('录入错误！1000-50000')


emp1 = Employee('pj', 7000)
print(emp1.print_demo)
print(emp1.salary)
emp1.salary = 20000
print(emp1.salary)
emp1.salary = -1000
