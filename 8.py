#given in the interge list find the averag of elements present in the even index/
n=list(map(int,input().split(" ")))
even=0
sum=0
avg=0
for i in range(0,len(n)):
    if(i%2==0):
        sum+=n[i]
        avg=sum/2
print(avg)