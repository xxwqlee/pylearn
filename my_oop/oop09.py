"""
try:
    代码
except (异常1,异常2，异常3） as 变量:
    遇到对应异常执行代码，并保存异常到变量
"""
try:
    a = input('输入被除数')
    b = input('输入除数')
    ia = int(a)
    ib = int(b)
    print('商为', ia / ib)
except ValueError:
    print('输入数据类型有误')
except ZeroDivisionError:
    print('除数不能为零')
# except Exception:
#     print('其他异常')
