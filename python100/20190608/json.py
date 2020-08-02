import time
#def Readfile(path):
#    f = open(path, 'r', encoding='utf-8')
#    print(f.read())
#    f.close()
#
#if __name__ == '__main__':
#    x = input('Please input the path:')
#    Readfile(x)



#def Readfile(path):
#    f = open(path, mode='a+', encoding='utf-8')
#    f.write('\nwwm love xcyk')
#    position = f.seek(0)
#    print(f.read())
#    f.close()
#
#if __name__ == '__main__':
#    #x = input('Please input the path:')
#    Readfile(r'E:\wwm_python\20190606\wwm.txt')


#def Readfile(path):
#    with open(path, 'r', encoding='utf-8') as f:
#        for line in f:
#            time.sleep(1)
#            print(line, end='')
#
#if __name__ == '__main__':
#    x = input('Please input the path:')
#    Readfile(x)
    


#def Readfile(path):
#    try:
#        with open(path, 'r', encoding='utf-8') as f:
#            for line in f:
#                time.sleep(1)
#                print(line, end='')
#    except:
#        print('文件错误')
#
#if __name__ == '__main__':
#    x = input('Please input the path:')
#    Readfile(x)



#def Writefile():
#    file= ('number.txt')
#    f = open(file, 'w+', encoding='utf-8')
#    for number in range(1,101):
#        f.write(str(number)+"\n")
#        number += 1
#    f.seek(0)
#    print(f.read())
#    f.close()
#
#if __name__ == '__main__':
#    Writefile()


def main():
    try:
        with open(r'C:\Users\xcyk\Desktop\IMG_3580.JPG', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
    except:
        print('指定的文件无法打开.')


if __name__ == '__main__':
    main()