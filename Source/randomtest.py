import random
def print_random():                  
    r1=random.random()+random.randrange(0,120,1)        
    list1=[r1]                       
    for x in range(1,1000):            
        r1=random.random()+random.randrange(0,120,1)
        list1.append(r1)
        print(list1[x]) 
    print('列表最小值：'+str(min(list1)))
    print('列表最大值：'+str(max(list1)))

print_random()
