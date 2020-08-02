##判断一个数是否是素数
#from math import sqrt
#num = int(input('请输入一个正整数:'))
#end = int(sqrt(num))
#is_prime = True
#for x in range(2,end+1):
#    if num % x == 0:
#        is_prime = False
#        break
#if is_prime == True and num !=1:
#    print('%d是素数'%num)
#else:
#    print('%d不是素数'%num)




##生成100个“斐波拉切数列”
#a=1
#b=1
#count=0
#while( count < 100):
#    print(a)
#    count+=1
#    a=a+b
#    b,a=a,b



##输出100以内的“斐波拉切数列”
# a=1
# b=1
# while a < 101:
#     print(a)
#     a = a + b
#     b,a = a,b

#a=1
#b=1
#for i in range(1,101):
#    print(a)
#    a=a+b
#    a,b=b,a
#    if a>100:
#        break