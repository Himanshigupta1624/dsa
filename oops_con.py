# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator.
#  Example: Myclass.Myattribute
class Dog:
    # Class Attribute
    species = "Canis familiaris"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog=Dog("Buddy",4) #object
print(dog.species)
print(dog.name)
print(dog.age)

# Self parameter is a reference to the current instance of the class. 
# It allows us to access the attributes and methods of the object.

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute initialized in a contructor
        self.age = age  # Instance attribute

dog1 = Dog("Buddy", 3)  # Create an instance of Dog
dog2 = Dog("Charlie", 5)  # Create another instance of Dog

print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly


class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)
# All objects of the class share the same value for a class variable 
# unless explicitly overridden in an object.

class Dog:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print(f"Dog's Name is {self.name}") 

class Labrador(Dog): #Single Inheritance
    def sound(self):
        print("Labrador woofs")

class GuideDog(Labrador): #multi level inheritance
    def guide(self):
        print(f"{self.name} Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("friendly!")
class GoldenRetriever(Dog,Friendly):
    def sound(self):
        print("Golden retriver Barks")

lab=Labrador("buddy")  
lab.display_name()
lab.sound()      

guide_dog=GuideDog("max")
guide_dog.display_name()
guide_dog.sound()
guide_dog.guide()


retriver=GoldenRetriever("charlie")
retriver.display_name()
retriver.sound()
retriver.greet()

# compile time polymorphism
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(5, 10))       # Two arguments
print(calc.add(5, 10, 15))   # Three arguments
print(calc.add(1, 2, 3, 4))  # Any number of arguments

# Method Overriding
# We start with a base class and then a subclass that "overrides" the speak method.
class Animal:
    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return "Woof!"
dog=Animal()
print(dog.speak())
print(Dog().speak())

# Duck Typing If an object implements the required method, it works regardless of its type.
class Cat:
    def speak(self):
        return "Meow!"
def make_animal_speak(animal):
    return animal.speak()  
print(make_animal_speak(Dog()))
print(make_animal_speak(Cat()))  
# Duck Typing: "make_animal_speak" function can accept both a Dog and a Cat object.
#  It doesn't care about their class hierarchy; it only checks if they have a speak method, 
# showcasing Python's flexible typing.

# 3 Operator Overloading
# We create a simple class that customizes the '+' operator.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # This special method defines the behavior of the '+' operator.
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v3)

class Dog:
    def __init__(self,name,breed,age):
        self.name=name
        self._breed=breed
        self.__age=age
    def get_info(self):
        return f"Name:{self.name},Breed:{self._breed},Age:{self.__age}"

    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Invalid Age!")
dog=Dog("Buddy","Labrador",3) 
print(dog.name)
print(dog._breed)
# Accessing private member using getter
print(dog.get_age())
#Modifying private member using setter
dog.set_age(5)
print(dog.get_info()) 

from abc import ABC, abstractmethod

class Dog(ABC):  # Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):  # Abstract Method
        pass

    def display_name(self):  # Concrete Method
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woof!")

class Beagle(Dog):  # Partial Abstraction
    def sound(self):
        print("Beagle Bark!")

# Example Usage
dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()  # Calls concrete method
    dog.sound()  # Calls implemented abstract method


def logger(func):
    def warpper():
        print("before call")
        func()
        print("after call")
    return warpper  
@logger
def say_hello():
    print("Hello!")
say_hello()

# Bank accounr class
class Bank:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amt)  :
        self.balance+=amt
    def withdraw(self,amt):
        if amt > self.balance:
            print("invalid funds")
        else:
            self.balance-=amt  

ice_cream_dict={'name':'vanilla','price':5,'size':'medium'}
for key, value in ice_cream_dict.items():
    print(f"{key} -> {value}")


# polymorphism example
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r

class Square(Shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        return self.a*self.a
    
# Infinite Fibonacci generator
# def inifinte_fibo():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b

# students=sorted(students ,key=lambda x:x.marks)

class Student:
    def __init__(self,marks):
        self.marks=marks

    def __lt__(self,other):
        return self.marks < other.marks   
        
# Lru cache
from collections import OrderedDict

class LRU:
    def __init__(self,cap):
        self.cap=cap
        self.cache=OrderedDict()

    def get(self,key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    def put(self,key,val):
        self.cache[key]=val
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)   

# Create cache: c = LRU(2) (capacity 2).
# c.put('a', 1) → cache order: ['a'].
# c.put('b', 2) → order: ['a','b'].
# c.get('a') → returns 1, moves 'a' to end → order: ['b','a'].
# c.put('c', 3) → insert 'c', now 3 items so pop oldest ('b') → final order: ['a','c']. 'b' evicted.

class Singleton:
    _instance=None

    def __new__(cls):
        if not cls._instance:
            cls._instance=super(Singleton,cls).__new__(cls)
        return cls._instance
        

           
        

        