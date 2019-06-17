# 嵌套函数（内部函数）


def print_name(is_chinese, name, family_name):
    c = 10

    def inner_print(a, b):
        print("{0} {1}".format(a, b))
        nonlocal c
        print(c)
    if is_chinese:
        inner_print(family_name, name)
    else:
        inner_print(name, family_name)


print_name(True, "xx", "高")
print_name(False, "George", "Bush")

# 测试LEGB
# str = 'global'


def outer():

    # str = 'outer'

    def inner():

        # str = 'inner'
        print(str)

    inner()


outer()
