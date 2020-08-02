#条件语句：
#1.列出 5 种不同的食材，请输出它们可能组成的所有菜式名称。diets = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
#2.用一个条件语句实现猜数字的小程序。 输入一个数字 判断该数字是否是某个数字（该数字写死的程序中）
#3.同上 但是所猜的数字是随机生成的
#4.猜数字游戏 提示数字偏大 还是偏小
#5.显示输入次数，比如最多只能输入5次


#第五题：
import random

def game():
    a = random.randint(1,10)
    print (a)
    for i in range (5):
        print ("%d times:" %i)
        b = int(input("Please input the number:"))
        if (b==a):
            print("正确，该数字是这个数字")
            break
        elif(b<a):
            print("错误，该数字不是这个数字，猜小了")
        else:
            print("错误，该数字不是这个数字，猜大了")
        
if __name__ == '__main__':
    game()


#第四题：
#import random
#
#def game():
#    a = random.randint(1,10)
#    print (a)
#    while True:
#        b = int(input("Please input the number:"))
#        if (b==a):
#            print("正确，该数字是这个数字")
#            break
#        elif(b<a):
#            print("错误，该数字不是这个数字，猜小了")
#        else:
#            print("错误，该数字不是这个数字，猜大了")
#        
#if __name__ == '__main__':
#    game()


#第三题：
#import random
#
#def game():
#    a = random.randint(1,10)
#    print (a)
#    while True:
#        b = int(input("Please input the number:"))
#        if (a==b):
#            print("该数字是这个数字")
#            break
#        else:
#            print("该数字不是这个数字")
#        
#if __name__ == '__main__':
#    game()


#第二题：
#def game():
#    a = 6
#    while True:
#        b = int(input("Please input the number:"))
#        if (a==b):
#            print("该数字是这个数字")
#            break
#        else:
#            print("该数字不是这个数字")
#        
#if __name__ == '__main__':
#    game()


#第一题1：
#def food():
#    diets = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
#    for diet1 in diets:
#        #print (diet1)
#        for diet2 in diets:
#            #print (diet2)
#            if (diet1 != diet2):
#                print (diet1 + diet2)
#
#if __name__ == '__main__':
#    food()


#第一题2：
#def food():
#    diets = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
#    for i in range(0, len(diets)):
#        #print (i, diets[i])
#        for j in range(i, len(diets)):
#            if (diets[i] != diets[j]):
#                print (diets[i] + diets[j])
#
#if __name__ == '__main__':
#    food()