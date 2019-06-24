"""
    装饰器：@语法糖、任意数量参数、自定义参数、类装饰器、装饰器的嵌套
    实例：用户身份认证、日志记录、输入合理性检查
"""


# 简单装饰器
def my_decorator1(func):
    def wrapper():
        print('wrapper of decorator1')
        func()
    return wrapper


@my_decorator1
def greet():
    print('hello world!')


# 带有参数的装饰器
def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator2')
        func(*args, **kwargs)
    return wrapper


@my_decorator2
def show_date(*args, **kwargs):
    print(args, '\t', kwargs)


# 带有自定义参数的装饰器（例如num表示内部函数被执行的次数）
def repeat(num):
    def my_decorator3(func):
        def wrapper(*args, **kwargs):
            print('wrapper of decorator3')
            func(*args, **kwargs)
        return wrapper
    return my_decorator3


@repeat(4)
def show_message(message):
    print(message)


# 类装饰器
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'num of calls is：{self.num_calls}')
        return self.func(*args, **kwargs)


@Count
def example():
    print('this is a example')


# 装饰器的嵌套
@my_decorator1
@my_decorator2
def dec_nest():
    print('nest of decorator')


if __name__ == '__main__':
    greet()
    show_date(2019, 6, 24, year='2019', month='06', date='24')
    show_message('201906241112')
    example()
    example()
    dec_nest()
