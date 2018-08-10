Max=int(input('输入斐波那契数列的最大项数：'))

def fab(Max):
    n,a,b=0,0,1
    while n<Max:
        yield b #使用yield
        a,b=b,a+b
        n=n+1

for i in fab(Max):
    print(i)
    

