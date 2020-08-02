#for i in range(1, 10):
#    for j in range(1, i + 1):
#        print('%d*%d=%d' % (i, j, i * j), end='\t')
#    print()



#from math import sqrt
#
#num = int(input('请输入一个正整数: '))
#end = int(sqrt(num))
#is_prime = True
#for x in range(2, end + 1):
#    if num % x == 0:
#        is_prime = False
#        break
#if is_prime and num != 1:
#    print('%d是素数' % num)
#else:
#    print('%d不是素数' % num)
#


def foo():
    print('hello, world!')
def foo():
    print('goodbye, world!')
# 下面的代码会输出什么呢？ 
foo()