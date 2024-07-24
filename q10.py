#print the pattern
#*******
#******* 
#*******
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()'''

    #patterns
'''row=3
column=5
for i in range(row):
    for j in range(column):
        print("*",end="")
    print()'''

'''row=3
column=5
for i in range(row):
    for j in range(column):
        print("*",end="")
    print()'''

row=10
column=10
for i in range(row):
    for j in range(column):
        if(i==j):
            print(" ",end="")
        else:
           print("*",end="")    
    print()
