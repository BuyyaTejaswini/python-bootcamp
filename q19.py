#find the missing number in an array

m=list(map(int,input().split()))
n=len(m)+1
a=n*(n+1)//2
b=sum(m)
c=a-b
print(c)

