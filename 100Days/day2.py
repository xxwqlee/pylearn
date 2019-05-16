"""
    控制结构练习：
    1.选择结构：三角形面积周长
    2.循环结构：判断素数、最大公约数和最小公倍数
"""
import math


class Triangle:

    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            print('不能构成三角形')

    def perimeter(self):
        p = (self.a+self.b+self.c)/2
        return p

    def area(self):
        p = self.perimeter()
        # p = (self.a + self.b + self.c) / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area

    def draw_tri(self):
        row = int(self.perimeter())
        for i in range(row):
            for _ in range(i + 1):
                print('*', end='')
            print()

        for i in range(row):
            for j in range(row):
                if j < row - i - 1:
                    print(' ', end='')
                else:
                    print('*', end='')
            print()

        for i in range(row):
            for _ in range(row - i - 1):
                print(' ', end='')
            for _ in range(2 * i + 1):
                print('*', end='')
            print()


class NumJudge:

    def __init__(self):
        pass

    @staticmethod
    def prime_judge(a):
        end = int(math.sqrt(a))
        is_prime = True
        for x in range(1, end + 1):
            if a % x == 0:
                is_prime = False
                break

        if is_prime and a != 1:
            print('{0}是素数'.format(a))
        else:
            print('{0}不是素数'.format(a))

    @staticmethod
    def mm_judge(a, b):
        x = int(a)
        y = int(b)
        if x > y:
            x, y = y, x
        for factor in range(x, 0, -1):
            if x % factor == 0 and y % factor == 0:
                print('%d和%d的最大公约数是%d' % (x, y, factor))
                print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
                break


tri1 = Triangle(3, 5, 7)
print(tri1.perimeter(), tri1.area())
tri2 = Triangle(3, 4, 10)
tri1.draw_tri()

NumJudge.prime_judge(11)
NumJudge.prime_judge(12)
NumJudge.mm_judge(3, 5)


