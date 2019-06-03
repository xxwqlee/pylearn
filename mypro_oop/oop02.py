class SalaryAccount:
    """工资计算类"""

    __age = 25  # 私有属性
    work_age = 3

    def __work(self):   # 私有方法
        print(f'上班{self.work_age}年！')

    def __call__(self, month_sal):
        year_sal = month_sal * 12
        day_sal = month_sal / 22.5
        hour_sal = day_sal / 8
        self.__work()  # 类中可以访问私有属性和方法

        return dict(
            month_salary=month_sal,
            year_salary=year_sal,
            day_salary=day_sal,
            hour_salary=hour_sal)


PjSalary = SalaryAccount()

print(PjSalary(7000))  # 可调用对象：通过对象名实际调用__call__方法

print(PjSalary.work_age)
# print(PjSalary.__age)  私有属性无法直接访问
print(PjSalary._SalaryAccount__age)  # 访问私有属性
PjSalary._SalaryAccount__work()  # 测试私有方法
