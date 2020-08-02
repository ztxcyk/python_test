#import os
#
#def ping(test):
#    dd = "ping " + test
#    ver = os.system(dd)
#    print (ver)
#
#if __name__ == '__main__':
#    iplist =["www.baidu.com", "www.hao123.com", "www.160.com", "www.360.com", "www.126.com"]
#    list1 = []
#    for item in iplist:
#        #ping(item)
#        print(item)
#        result = item.split('.')
#        #print(result[0])
#        #print(result[1])
#        #print(result[2])
#        for item in result:
#            print(item)
            




#import os
#
#def ping(test):
#    dd = "ping " + test
#    ver = os.system(dd)
#    print (ver)
#
#if __name__ == '__main__':
#    iplist =["www.baidu.com", "www.hao123.com", "www.160.com", "www.360.com", "www.126.com"]
#    list1 = []
#    for item in iplist:
#        #ping(item)
#        #print(item)
#        result = item.split('.')
#        #print(result[0])
#        #print(result[1])
#        #print(result[2])
#        for item in result:
#            #print(item)
#            list1.append(item)
#    print(list1)



#import os
#
#def ping(test):
#    dd = "ping " + test
#    ver = os.system(dd)
#    print (ver)
#
#if __name__ == '__main__':
#    iplist =["www.baidu.com", "www.hao123.com", "www.160.com", "www.360.com", "www.126.com"]
#    list1 = []
#    for item in iplist:
#        #print(item)
#        result = item.split('.')
#        for item in result:
#            print(item)
#            if item not in list1:
#                list1.append(item)
#    print(list1)





#def IsInList(item,list):
#    for key in list:
#        if key == item:
#            return True
#    return False
#        
#
#if __name__ == '__main__':
#    iplist =["www.baidu.com", "www.hao123.com", "www.160.com", "www.360.com", "www.126.com"]
#    list1 = []
#    for item in iplist:
#        #print(item)
#        result = item.split('.')
#        for item in result:
#            print(item)
#            if not IsInList(item,list1):
#                list1.append(item)
#            #if item not in list1:
#            #list1.append(item)
#    print(list1)




#def get_Value (dict, keyword):
#    if keyword in dict.keys():
#        return dict[keyword]
#    else:
#        return 'Not Found'
#
#        
#
#if __name__ == '__main__':
#    ipdict ={"百度":"www.baidu.com", "hao123":"www.hao123.com", "160":"www.160.com", "360":"www.360.com","126": "www.126.com"}
#    # for item in ipdict.items():
#    #     print(item)
#    while True:
#        key1 = input("Please input the key:")
#        vvv=get_Value(ipdict,key1)
#        print(vvv)
#

import os
root = os.getcwd()

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print ("-----------")
        print (root)   #os.walk()所在目录
        print (dirs)   #os.walk()所在目录的所有目录名
        print (files)   #os.walk()所在目录的所有非目录文件名
        print (" ")

if __name__ == '__main__':
    file_name(root)