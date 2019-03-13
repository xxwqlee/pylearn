class SalaryAccount:
    """工资计算类"""

    __age = 25  # 私有属性
    age = 18

    @staticmethod
    def __work():   # 私有方法
        print('好好上班！')

    def __call__(self, month_sal):
        year_sal = month_sal * 12
        day_sal = month_sal / 22.5
        hour_sal = day_sal / 8

        return dict(
            month_salary=month_sal,
            year_salary=year_sal,
            day_salary=day_sal,
            hour_salary=hour_sal)


PjSalary = SalaryAccount()
# 可调用对象：通过对象名实际调用__call__方法
print(PjSalary(7000))

# 测试私有属性
print(PjSalary.age)
# print(PjSalary.__age)
print(PjSalary._SalaryAccount__age)
# 测试私有方法
PjSalary._SalaryAccount__work()
