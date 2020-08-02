import os
import random

def ping(test):
    dd = "ping " + test
    ver = os.system(dd)
    print (ver)

if __name__ == '__main__':
    iplist =["www.baidu.com", "www.hao123.com", "www.160.com", "www.360.com", "www.126.com"]
    #Single = random.randint(0,6)
    Single = 5
    if Single == 5:
        Single = 0
    strq = iplist[Single]
    ping(strq)
        

#import os
#import random
#
#def ping(test):
#    dd = "ping " + test
#    ver = os.system(dd)
#    print (ver)
#
#if __name__ == '__main__':
#    iplist =["www.baidu.com", "www.hao123.com", "www.160.com", "www.360.com", "www.126.com"]
#    iplist.append("www.baidu.com")
#    print (iplist)
#    Single = random.randint(0,6)
#    strq = iplist[Single]
#    ping(strq)



#import os
#import random
#
#def ping(test):
#    dd = "ping " + test
#    ver = os.system(dd)
#    print (ver)
#
#if __name__ == '__main__':
#    iplist =["www.baidu.com", "www.hao123.com", "www.160.com", "www.360.com", "www.126.com"]
#    #print ("www.baidu.com索引位置: ", iplist.index( 'www.baidu.com' ))
#    #num = iplist.index(item)
#    Single = random.randint(0,5)
#    strq = iplist[Single]
#    ping(strq)
        




#import os
#
#def ping(test):
#    dd = "ping " + test
#    ver = os.system(dd)
#    print (ver)
#
#if __name__ == '__main__':
#    iplist =["www.baidu.com", "www.hao123.com", "www.160.com", "www.360.com", "www.126.com"]
#    for item in iplist:
#        ping(item)



#import os
#
#def ping(test):
#    dd = "ping " + test
#    ver = os.system(dd)
#    print (ver)
#
#if __name__ == '__main__':
#    ipadd = input("please input the IPaddress:")
#    ping(ipadd)


#import os
#
#def ping():
#    ver = os.system("ping baidu.com")
#    print (ver)
#
#if __name__ == '__main__':
#    ping()
#


#import os
#ver = os.system("ping baidu.com")
#print (ver)