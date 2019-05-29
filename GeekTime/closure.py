"""
    闭包：closure
    嵌套函数以及输入类型检查：factorial()
"""


def nth_power(exponent):  # 闭包函数
    def exponent_of(base):
        return base ** exponent
    return exponent_of  # 返回值是一个函数


def nth_power_rewrite(base, exponent):
    return base ** exponent


def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0')

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input - 1)
    return inner_factorial(input)


if __name__ == "__main__":
    square = nth_power(2)
    cube = nth_power(3)
    print(f'type of square{type(square)}\t'
          f'{square(5)}\t{nth_power_rewrite(5, 2)}')
    print(f'type of cube{type(cube)}\t'
          f'{cube(5)}\t{nth_power_rewrite(5, 3)}')
    for i in range(3, -3, -1):
        print(factorial(i))
