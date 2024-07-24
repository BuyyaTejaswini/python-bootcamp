#write a code to print all the capital letters in a given string
str="HELlo"
for i in str:
    if(ord(i)>=65 and ord(i)<=90): #97 to 122 lower case
      print(i,end="")
