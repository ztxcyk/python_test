
def avg(dict1):
    sum = 0 
    num = 0
    for value in dict1.values():
        print(value)
        sum = sum + value
        num = num +1
    aaa = sum / num
    return aaa

if __name__ == '__main__':
    Phone =  {"苹果":3450, "三星":3210, "华为":2360, "小米":1800,"中兴": 2800}
    VVV = avg(Phone)
    print(VVV)




#if __name__ == '__main__':
#    Phone =  {"苹果":3450, "三星":3210, "华为":2360, "小米":1800,"中兴": 2800}
#    sum = 0 
#    num = 0
#    for value in Phone.values():
#        print(value)
#        sum = sum + value
#        num = num +1
#    avg = sum / num
#    print(avg)




#def get_Value (dict, keyword):
#    if keyword in dict.keys():
#        return dict[keyword]
#    else:
#        return 'Not Found'
#
#if __name__ == '__main__':
#    ipdict ={"百度":"www.baidu.com", "hao123":"www.hao123.com", "160":"www.160.com", "360":"www.360.com","126": "www.126.com"}
#    # for item in ipdict.items():
#    #     print(item)
#    while True:
#        key1 = input("Please input the key:")
#        vvv=get_Value(ipdict,key1)
#        print(vvv)