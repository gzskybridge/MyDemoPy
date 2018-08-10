#Fibonacci series:斐波那契数列
#两个元素的总和确定下一个数
#
#
def fibo_s():
    a,b=0,1
    fs_top=int(input('请输入一个自然数，作为数列最后一项的上限:'))
    while b<fs_top:
        print(b)
        a,b=b,a+b

#fibo_s()

def fibos_l():
    """用递归方法求一个n项的斐波那契数列，结果存储在一个列表中"""
    n=int(input('请输入一个正整数：'))
    result=[]  
    def fab(n):
        if n<1:
            print('输入有误!')
            return -1
        if n==1:
            return 1
            result=[1]
        elif n==2:
            return 2
            result=[1,2]
        else:
            temp=fab(n-1)+fab(n-2)
            result.append(temp)
            return temp
    for i in range(n):
        print(fab(i))
            

#
def fibos_d():
    """用递归算法求一个n项的斐波那契数列，结果存储在一个字典中"""
    n=int(input('请输入一个正整数：'))
    dic={0:0,1:1}
    def fib(n):
        if n in dic:
            return dic[n]
        else:
            temp=fib(n-1)+fib(n-2)
            dic[n]=temp
            return temp
    for i in range(n):
        print(fib(i))


#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
    #调用父类的构函
       people.__init__(self,n,a,w)
       self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
    
#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
                                                                                                                  
#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

