# 测试组合关系 has-a
class MobilePhone:
    def __init__(self, screen, cpu, battery):
        self.screen = screen
        self.cpu = cpu
        self.battery = battery


class CPU:
    def calculate(self):
        print(self, "计算中……")

    def work_for_screen(self):
        print(self, 'CPU 解码……')


class Screen:
    def __init__(self, cpu, battery):
        self.cpu = cpu
        self.battery = battery

    def show(self):
        CPU.work_for_screen(self.cpu)
        Battery.work_for_screen(self.battery)
        print(self, "显示一个好看的画面")


class Battery:
    def work_for_screen(self):

        print(self, 'Battery 供能……')


c = CPU()
b = Battery()
s = Screen(c, b)
m = MobilePhone(s, c, b)

m.screen.show()

m.screen.cpu.calculate()  # 通过screen中的cpu调用calculate
m.cpu.calculate()   # 通过mobile phone中的cpu调用calculate
