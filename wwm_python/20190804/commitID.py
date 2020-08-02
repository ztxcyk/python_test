import subprocess
import os

os.chdir('E:\\Myworkplace\\PythonTest')

#log = systemcall('git log -1')
#print (log)
#commitlist = []
#ps = subprocess.Popen('git log -1', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#log = ps.stdout.readline()
#print (type(log))
#xx = bytes.decode(log)
#print (xx)
#print ('...............................')
#commitlist = xx.split('\n')
#commitlist = commitlist[0]
#commitlist = commitlist.split(' ')
#commitlist = commitlist[1]
#print(commitlist)

#git log --pretty=format:'%H' -1
# ps = subprocess.Popen("git log --pretty=format:'%H' -1", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
# log = ps.stdout.readline()
# xx = bytes.decode(log)
# #print (xx)
# #yy=xx.split('\'')
# print(xx[1:-1])

commid="'358feb2724ce4bf9f0ebaee4f7c3e46c59b90d9d'"
yy=commid.split('\'')

str1='123 34 vb 123'
ss=str1.split(' ')