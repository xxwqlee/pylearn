"""
    闭包：closure
"""


def nth_power(exponent):  # 闭包函数
    def exponent_of(base):
        return base ** exponent
    return exponent_of  # 返回值是一个函数


def nth_power_rewrite(base, exponent):
    return base ** exponent
    #  TODO: rewrite power function


if __name__ == "__main__":
    square = nth_power(2)
    cube = nth_power(3)
    print(f'type of square{type(square)}\t{square(5)}\t{nth_power_rewrite(5, 2)}')
    print(f'type of cube{type(cube)}\t{cube(5)}\t{nth_power_rewrite(5, 3)}')
