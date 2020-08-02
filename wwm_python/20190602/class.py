class student(object):
    def __init__(self,name,id):
        self.Name=name
        self.ID=id
        self.Age=0

    def Write(self):
        zy='sdfsdfasdfasdf'
        return zy

    def SetAge(self,age):
        self.Age=age

    def GetAge(self):
        x = self.Age
        return x

    def study(self, course_name):
        print('%s正在学习%s.' % (self.Name, course_name))
    
if __name__ == "__main__":
    s1=student('wwm',1)
    s1.SetAge(10)

    print(s1.Name)
    print(s1.ID)
    print(s1.Write())
    print(s1.GetAge())
    s1.study('English')

    