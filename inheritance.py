class animal:
    def speak():
        return"animal is speaking"
    #single inheritance
class dog(animal):
    def bark():
         return"bow..."
obj1=animal
obj2=dog
print(obj1.speak())
print(obj2.bark())
#multi level inheritance
class puppy(dog):
   def puppy_speak():
    return"im puppy"
obj3=puppy
print(obj3.puppy_speak())
   