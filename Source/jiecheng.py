import math
n=int(input('输入自然数n的值:'))
sum=0
counter=1
while counter<=n:
    sum=sum+counter
    counter=counter+1

print('1到%d之和为：%d'%(n,sum))
