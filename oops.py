# create a class and object using oops
class myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def mod(a,b):
        return a%b
obj1=myclass
print(obj1.add(2,5))
print(obj1.mul(2,5))
print(obj1.mod(2,5))
print(obj1.sub(2,5))
obj2=myclass
print(obj2.div(2,7))
