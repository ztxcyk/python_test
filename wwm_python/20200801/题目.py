#输入一个三位数，求和：个位数+十位数+百位数
#x = 123
#sum =0
#a = x // 100
#b = x % 100 // 10
#c = x % 100 % 10
#sum = sum + a + b + c
#print(sum)



def sum(x):
    sum =0
    a = x // 100
    b = x % 100 // 10
    c = x % 100 % 10
    sum = sum + a + b + c
    return sum
    
if __name__ == "__main__":
    M = int(input('please input the 三位数：'))
    N = sum(M)
    print(N)

