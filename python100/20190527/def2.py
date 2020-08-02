# def gcd(x, y):
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor


#def lcm(x, y):
#    return x * y // Mygcd(x, y)
#
#
#def Mygcd(x, y):
#    (x, y) = (y, x) if x > y else (x, y)
#    a=1
#    for factor in range(1, x+1):
#        if x % factor == 0 and y % factor == 0:
#            a=factor
#    return a
#
#if __name__ == '__main__':
#    a = int(input('Please input the zhengzhengshu:'))
#    b = int(input('Please input the zhengzhengshu:'))
#    x = Mygcd(a,b)
#    print(x)
#    y = lcm(a,b)
#    print(y)
    


def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    #print(c)  # NameError: name 'c' is not defined

if __name__ == '__main__':
    a = 100
    foo()
    #print(b)  # NameError: name 'b' is not defined