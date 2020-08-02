#value = float(input('请输入长度'))
#unit = float(input('请输入单位'))
#if unit == 'in' or unit == '尺寸':
#    print('%f英寸 = %f厘米'% (vaule, value * 2.54))
#elif unit == 'cm' or unit == '厘米':
#    print('%f厘米 = %f英寸'% (value, value / 2.54))
#else:
#    print('请输入有效的单位')


#from random import randint
#import random
#face = random.randint(1,6)
#if face==1:
#    result='A'
#elif face==2:
#    result='B'
#elif face==3:
#    result='C'
#elif face==4:
#    result='D'
#elif face==5:
#    result='E'
#else:
#    result='F'
#print(result)


#scope = float(input('请输入分数：'))
#if scope > 90:
#    result = 'A'
#elif scope > 80:
#    result = 'B'
#elif scope > 70:
#    result = 'C'
#else:
#    result = 'D'
#print(result)


#import math
#a = float(input('a='))
#b = float(input('b='))
#c = float(input('c='))
#if a+b>c and a+c>b and b+c>a:
#    print('周长是：%.2f'%(a+b+c))
#    p = (a + b + c) / 2
#    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
#    print('面积是%.2f'%(area))
#else:
#    print('不能成立三角形')



salary = float(input('本月收入：'))
insurance = float(input('五险一金'))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 3000:
    rate = 0.06
    deduction =0
else:
    rate = 0.08
    deduction = 0.03
print('工资是：%.2f'%(diff))