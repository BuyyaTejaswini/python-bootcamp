#input hello 1234 then op 6
vowel="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
check="0123456789"
ans=0
i="hello 123rld"
inp=i.lower()
for i in inp:
  if(i in check):
    ans+=int(i)
print(ans)