class Student(object):
    def __init__(self,name,score,id):
        self.name = name
        self.__score = score
        self.__id = id
    
    def Rescore(self, Score):
        self.__score = Score

    def GetScore(self):
        x = self.__score
        return x

    def ReID(self,ID):
        self.__id = ID
    
    def GetID(self):
        x = self.__id
        return x


if __name__ == '__main__':
    s1 = Student('xcyk', 90, 666)
    print(s1.name)
    print(s1.GetScore())
    print(s1.GetID())

    s1.Rescore(95)
    print(s1.GetScore())

    

