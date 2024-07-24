#print all the vowels followed by consonants
check=["a","e", "1", "o", "u"]
consonents="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="akshita"
inp=i.lower()
for i in inp:
  if(i in check): 
    count+=1
print("no. of vowels are:",count)
for i in inp:
   if(i not in check):
     count+=1
print("no. of consonants:",count)