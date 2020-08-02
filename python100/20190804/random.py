import random

def Sieves():
    n1=random.randint(1, 6)
    n2=random.randint(1, 6)
    return n1,n2

def run():
    sum1=0
    sum2=0
    for i in range(10):
        s1,s2=Sieves()
        print("(第%d次)玩家1：筛子A：%d  筛子B：%d 总分：%d"%(i+1,s1,s2,sum1+s1+s2))
        sum1=sum1++s1+s2

        c1,c2=Sieves()
        print("(第%d次)玩家2：筛子A：%d  筛子B：%d 总分：%d"%(i+1,c1,c2,sum2+c1+c2))
        sum2=sum2+c1+c2

    if sum1>sum2:
        print('玩家1赢了')
    elif sum1 == sum2:
        print("平局")
    else:
        print('玩家2赢了')


if __name__ == '__main__':
    run()
