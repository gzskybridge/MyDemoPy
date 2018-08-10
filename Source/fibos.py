import sys

n=int(input('输入斐波那契数列的最大项数:'))
def fibos(n):
    a,b,counter=0,1,0
    while True:
        if (counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibos(n)

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()


