#x=int(input('Please input the number fanwei shi 100 到 999:'))
#if x > 99 and x < 999:
#    a = x // 100
#    b = x // 10 % 10
#    c = x % 10
#    f = a*a*a+b*b*b+c*c*c-x
#    if 0 == f :
#        print('这是水仙花数')
#    else:
#        print('不是水仙花数')
#else:
#    print('输入错误')

#print('x=%.2f'%(5/3))
#print('x=%d'%(5//3))



from math import sqrt
from math import pow
num = int(input('please input the number:'))
end = int(sqrt(num))
end2 = int(sqrt(pow(2,num)-1))
is_prime = True
for x in range(2,end+1):
    if num % x ==0:
        is_prime = False
        break
if is_prime and num !=1:
    two_prime = True
    for x in range(2,end2 + 1):
        if (pow(2,num)-1) % x ==0:
            two_prime = False
            print('%d是素数,%d是素数'%(num,(pow(2,num)-1))) 
            N = num - (pow(2,num)-1) * (pow(2,num-1))
            if 0 == N:
                print('%d是完全数'%num)
            else:
                print('%d不是完全数'%num)
            break
else:
    print('%d不是素数'%num)