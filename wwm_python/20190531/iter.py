from collections.abc import Iterable

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key, type(key))


# def fun(xc):
#     if isinstance(xc, Iterable):
#         for item in xc:
#             print(item)
#     else:
#         print('Failed')

# def listfun():
#     l=['o','p']
#     for x, y ,z ,v in [(1, 1,'a',l), (2, 4,'b',l), (3, 9,'c',l)]:
#         print(x, y,z,v)


def Addlist(L):
    L.append(3)     

def addnum(x):
    x=x+2       

if __name__ == "__main__":
    # s='adbdfs'
    # a=123
    # l=[1,2,3,4,5]
    # fun(a)
    #listfun()
   # mylist=[1,2]
   # Addlist(mylist)
    #print('Main: ', mylist)  
    num=1
    addnum(num)
    print(num)