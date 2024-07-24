#find the maximum element in a given list
''''my_list=list(map(int,input().split()))
print(max(my_list))'''

my_list=list(map(int,input().split()))
maxi=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
print(maxi)