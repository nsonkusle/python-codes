def inpt():
    num = int(input("enter a number: "))
    temp = num
    if temp<0:
        print("number")
    else:
     mul= 1
     while(temp>0):
        mul*=temp
        temp-=1
     print('mul =',mul)
    if num<0:
        print("number")
    else:
     sum= 0
     while(num>0):
        sum+=num
        num-=1
     print('add = ',sum) 

    
    if  mul%sum==0:
        print('yes')
    else:
        print('no')     
inpt()
