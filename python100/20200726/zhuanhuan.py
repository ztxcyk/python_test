#value = float (input('please input the 长度:'))
#unit = input('please input the 单位:')
#
#if unit == 'in' or unit == '英寸':
#    print('%f英寸 = %f厘米' % (value, value *2.54))
#elif unit == 'cm'or unit == '厘米':
#    print('%f厘米 = %f英寸' % (value, value / 2.54))
#else:
#    print('请输入有效单位')


#from random import randint
#face = randint(1,6)
#if face == 1:
#    result = '111'
#elif face == 2:
#    result = '222'
#elif face == 3:
#    result = '333'
#else:
#    result = '11111111111111111111'
#print(result)


from random import randint

answer = randint(1,20)
count = 0
while True:
    number = int(input('please input the number:'))
    count += 1
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('答对了')
        if count>5:
            print("ruozhi")
        break
