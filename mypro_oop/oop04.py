class Person:

    __str__ = "chi he la sa shui"

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print('stu`age is', self.__age)

    def say_name(self):
        print('stu`s name is', self.name)


class Student(Person):

    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def say_name(self):
        print('学生的名字是', self.name)


# 子类继承父类的方法和属性
stu1 = Student('pj', 22, 59)
stu1.say_age()
print(stu1.__str__)
print(stu1.name, stu1.score)
# 子类访问父类的私有属性
print(stu1._Person__age)
# 测试子类方法的重写
stu1.say_name()
# 查看类的继承层次结构
print(Student.mro())
# 查看对象的所有属性
print(dir(stu1))
