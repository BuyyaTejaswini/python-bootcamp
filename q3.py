##print the non-repeating char or unique char in a str
vowel="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
ans=""
i="akshiiiiii"
inp=i.lower()
for i in inp:
  if(i not in ans):
    ans+=i
print(ans)