class Eng:
    '''建立工程师类'''
    numbers=0
    def __init__(self,title,name,age,sex):
        self.title=title
        self.name=name
        self.age=age
        self.sex=sex
        print('新工程师{0}'.format(name))
        Eng.numbers += 1
    def tell(self):
         print('\n职位：{3}\n姓名：{0} \n年龄：{1} \n性别：{2}'.format(self.name,self.age,self.sex,self.title))

class PLC_Eng(Eng):
    def __init__(self,title,name,age,sex,skill):
        Eng.__init__(self,title,name,age,sex)
        self.skill=skill
    def tell(self):
         Eng.tell(self)
         print('技能：{}'.format(self.skill))
class Software_Eng(Eng):
    def __init__(self,title,name,age,sex,type):
        Eng.__init__(self,title,name,age,sex)
        self.type=type
    def tell(self):
        Eng.tell(self)
        print("类型：{}".format(self.type))

eng_1=PLC_Eng('PLC工程师','张三',30,'男','Siemens')
eng_2=Software_Eng('软件工程师','李四',33,'男',"C#")
PLC1=PLC_Eng('PLC工程师','王五',28,'男','Rockwell')
print ('共有{}个工程师'.format(Eng.numbers))

engs=[eng_1,eng_2,PLC1]
for eng in  engs:
    eng.tell()



#eng_1.tell()
#eng_2.tell()


