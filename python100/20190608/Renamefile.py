import os
import shutil

def findfile(filepath):
    files = os.listdir(filepath)  
    for fi in files:    
        fi_d = os.path.join(filepath,fi)    
        if os.path.isdir(fi_d):
            findfile(fi_d)
        else:
            index=filepath.rfind('\\')
            filename=filepath[index+1:]
            shutil.copyfile(os.path.join(filepath,fi_d),r'C:\Users\xcyk\Desktop\doc\文档'+'\\'+ filename + '.rtf')      

    print('copy:'+filepath)

if __name__ =='__main__':
    path=r"C:\Users\W26361\Desktop\文档"
    findfile(path)
    print('over')