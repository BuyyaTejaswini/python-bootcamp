#method over writting
class Animal:
    def Speak():
        return "Speaking...."
class Dog(Animal):
    def Speak():
        return "Dog is speaking..."
class puppy(Dog):
    def Speak():
        return "Puppy is speaking..."
obj1=puppy
print(obj1.Speak())

def run():
    return "running"
def run():
   return "hello"
print(run()) #print the most recent call for the method.previous call will be lost

