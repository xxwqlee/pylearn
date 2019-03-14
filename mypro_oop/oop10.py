"""
try:
    可能出现异常的代码
except 异常 as 变量:
    捕获到对应异常时执行
else:
    没有异常，执行的代码
finally:
    必须执行的代码
案例：将一些字符串数据写入文件

"""
try:
    file = open('data1.txt', 'w', encoding='utf-8')
    file.write('Hello')
    file.write('World')
    # write 只能用于字符串数据写入
    # file.write([1, 2, 3])
    print('写入完毕')
except Exception as e:
    print(e.args)
else:
    print('没有异常')
finally:
    # 关闭文件
    file.close()
    print('关闭文件')
