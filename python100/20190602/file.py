#import os
#
#x=[d for d in os.listdir('.')] 
#print(x)

#输出任意目录下的文件(例如 C:\)
import os

#def fun():
#    return [d for d in os.listdir('.')] 


#def fun(x,y):
#    L=[]
#    for d in os.listdir(x):
#        if d != y:
#            L.append(d)
#    return L
#
#
#if __name__ == '__main__':
#    path=input('Please input a path:')
#    file=input('Please input a file:')
#    x=fun(path,file)
#    print(x)



#def fun(*Args):
#    L=[]
#    for i in Args:
#        print(i)
#    return L
#
#
#if __name__ == '__main__':
#    a=0
#    fun(1, 2, 3, 'wwm', 'xcyk',a)



#def fun(*Args):
#    L=[]
#    for i in Args:
#        L.append(i)
#    return L
#
#
#if __name__ == '__main__':
#    a=0
#    x = fun(1, 2, 3, 'wwm', 'xcyk',a)
#    print(x)



def Add(x, y=0, z=0):
    sum = x + y + z
    return sum


if __name__ == '__main__':
    x1 = Add(1, 2, 3)
    x2 = Add(1)
    print(x1, x2)