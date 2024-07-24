#i/p==hello-----wor----ld
#o/p==---------helloworld
#"-"=30
inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)    