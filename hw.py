#find even or odd
#find greatest of three
#finf sum of element in the array
#find peak element in the array
#find maximumelement in the array
#find second max element in the arrya
#reverse an array without using building functions
#find the sum of square of given num
#check whether given num is palindrome or not
#find sum of squres of even and odd digits
#write a program to print first fibanoci series

n=10 #fibanocci series
num1 = 0
num2 = 1#fn=f(n-1)+f(n-2)
next_number = num2
count = 1
while count <= n:
   print(next_number, end="")
   count +=1
   num1, num2= num2, next_number
   next_number= num1 + num2
print()

a=int(input())      #even or odd
if (a%2==0):
   print("even")
else:
   print("odd")

   #greatest of 3 numbers 
   a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
  print("a is greatest",a)
elif(b>a and b>c):
   print("b is greatest",b)
else:
    print("c is the greatest", c)

arr=list(map(int, input().split())) #peak element (greater than neighbour)
max=arr[e]
for i in range(len(arr)):
  if(arr[i]>max):
   max=arr[i]
print(max) 

arr=list(map(int, input().split())) #second element in array
max=arr[1]
for i in range(len(arr)):
 if(arr[i]==max):
   print("second element is ",max)

num=121     #palindrome or not
temp=num
reverse=0
while temp>0:
       rem=temp%10
       reverse=reverse*10+rem
       temp=temp//10
if num==reverse:
   print("palindrome")
else:
    print("not palindrome") 
num-1221
reverse=int(str(num) [::-1])  #palindrome
if num==reverse:
    print("palindrome")
else:
   print("not palindrome")


n=246
sum=0
while n>0:
  r=n%10 
  sum=sum+r*r #r**2
  n=n//10
print(sum)

