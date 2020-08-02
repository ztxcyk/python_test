#import os
#
#x=[d for d in os.listdir('.')] 
#print(x)


#def fib(max):
#    n, a, b = 0, 0, 1
#    while n < max:
#        yield b
#        a, b = b, a + b
#        n = n + 1
#    return 'done'
#
#if __name__ == "__main__":
#    num = int(input('Please input the number:'))
#    #x = fib(num)
#    for n in fib(num):
#        print(n)


#def fun(num):
#    for x in range(1, num+1):
#        result = x * x
#        if result % 2 !=0:
#            yield result
#
#if __name__ == '__main__':
#    num = int(input('Please input the num:'))
#    for x in fun(num):
#        print(x)


def fun(num):
    n=0
    x=1
    while n < num:
        result=x**2
        if result%2==1:
            yield result
            n+=1
        x+=1



if __name__ == '__main__':
    num = int(input('Please input the num:'))
    for x in fun(num):
        print(x)