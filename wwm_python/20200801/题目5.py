#a = int(input('please input the number_a:'))
#b = int(input('please input the number_b:'))
#c = int(input('please input the number_c:'))
#L = []
#L.append(a)
#L.append(b)
#L.append(c)
#L.sort()
#print(L)


#输入一个数字列表，当列表中出现字母时，停止


if __name__ == "__main__":
    L = []
    while True:
        a = input('please input the list:')
        if a.isdigit():
            L.append(int(a))
            #print(L)
        else:
            break
    L.sort()    
    print(L)    