#you are given a , separated natural numbers 1 to 10
#print only the even numbers

#=[1,2,3,4,5,6,7,8,9,10]
n=list(map(int,input().split(",")))
#for i in range(len(n)):
 #   if(i%2==0):
  #      print(i)

count=0
for i in range(1,len(n),2):
 count+=1
print(count)