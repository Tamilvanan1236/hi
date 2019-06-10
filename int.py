a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a[1]
sum=0
for i in range(0,len(b)):
    if i<c:
        sum=sum+b[i]
    
print(sum)
