x = float(input('please input the number:'))

if x > 1:
    y = 3 * x - 1
elif -1 < x < 1:
    y = 5 * x
#else x < -1:
else:
    y = x
print('f(%.2f) = %.2f' % (x,y))