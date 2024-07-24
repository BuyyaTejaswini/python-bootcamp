#find the sum of elements that is present in k+n index
'''N=[3,4,5,6,7,8]
k=3
n=4
for i in range(0,len(N)):
     if(i==k+n):
         print(N[i])'''

my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
b=len(my_list)
if(b<k+n):
    print("error")
else:
    print(my_list[k+n])  