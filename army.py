a,b=input().split()
a=int(a)
b=int(b)
for i in range(a,b):
    arm=0
    b=i
    
    while(i!=0):
        rem=i%10
        arm=arm+(rem**3)
        i=i//10
    if(arm==b):
        print(b,end=" ")
    

        
