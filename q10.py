#print the element in a particular index,condition is cycle,(find the element present in k index)
my_list=list(map(int,input().split()))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])

