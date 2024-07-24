#replace the element in an array with avg of max and min element
n=[13,2,67,20,68]
max=n[0]
for i in range(len(n)):
    if (n[i]>max):
        max=n[i]
min=n[0]
for i in range(len(n)):
    if(n[i]<min):
        min=n[i]
avg=(max+min)/2
for i in range(len(n)):
    n[i]=avg
print(n)