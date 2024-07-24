#check how many vowels are in a string
check=["a", "e", "i", "o", "u"]
count=0
input="akshita"
for i in input:
    if(i in check):
       count+=1
print(count)   
#check how many consonants in a string
check=["a", "e", "i", "o", "u"] 
consonents="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="akshita"
inp=i.lower()
for i in inp:
    if(i not in check):
       count+=1
print(count)                

