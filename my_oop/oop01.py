class Student:

    school = 'scu'  # 类属性
    count = 0  # 类属性

    def __init__(self, name, score):
        self.name = name  # 实例属性
        self._score = score  # _开头表示受保护的属性，提示访问应该慎重
        Student.count += 1

    def say_score(self):  # 实例方法
        print('{0}:school is {1} '.format(self.name, Student.school))
        print('{0}的分数是：{1}'.format(self.name, self._score))

    @classmethod
    def print_school(cls):  # 类方法
        print(cls.school)

    @staticmethod
    def print_add(a, b):  # 静态方法
        print('{0} + {1} = {2}'.format(a, b, (a+b)))


stu1 = Student('l', 99)
stu1.say_score()

stu2 = Student('p', 6)
stu2.say_score()
print(stu1.__sizeof__())
print(stu2.__dir__())
print(stu1.__module__)
print(stu1.__dict__)
print('创建了{0}个Student对象'.format(Student.count))
# 类方法的使用
Student.print_school()
# 静态方法的使用
Student.print_add(stu1._score, stu2._score)
# 对象可以访问类属性，类不能访问对象的实例属性
stu1.print_school()
print(stu1.count)

