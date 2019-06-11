a,b=input().split()
a=int(a)+1
b=int(b)
for i in range(a,b):
    for j in range(2,i):
        if(i%j==0):
            break;
    else:
        print(i,end=" ")
