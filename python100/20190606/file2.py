import time

#def Readfile():
#    f = open(r'E:\wwm_python\20190606\wwm.txt', 'r', encoding='utf-8')
#    print(f.read())
#    f.close()
#
#
#if __name__ == '__main__':
#    Readfile()

    


#def Readfile(path):
#    f = open( path, 'r', encoding='utf-8')
#    print(f.read())
#    f.close()
#
#
#if __name__ == '__main__':
#    x = input('Please input the path:')
#    Readfile(x)




#def Readfile():
#    f = None
#    try:
#       f = open(r'E:\wwm_python\20190606\wwm.txt', 'r', encoding='utf-8')
#       print(f.read()) 
#    except:
#        print('读取文件错误!')
#    finally:
#        if f:
#            f.close()
#
#
#if __name__ == '__main__':
#    Readfile()



#def Readfile():
#    try:
#        with open(r'E:\wwm_python\20190606\wwm.txt', 'r', encoding= 'utf-8') as f:
#            print(f.read())
#    except:
#        print('文件错误')
#
#if __name__ == '__main__':
#    Readfile()




def Readfile():
    with open(r'E:\wwm_python\20190606\wwm.txt', 'r', encoding= 'utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(1)

if __name__ == '__main__':
    Readfile()


