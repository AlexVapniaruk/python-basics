from enum import Enum

name = "Alex"
age = 30
#comment
if type(name) == str and isinstance(float(age), float):
    print(age)

1+1#2
2-1#1
2*2#4
4/2#2
4%3#1
4**2#16
5//2#2 (floor div)

#concat
"First string" + "Second string"
name += " is my name"
age += 8
print(age)
print(name)
1 or 2

print("""dsadsa
dadasd
dsad
dsadsa""")#multiline string

print(name.upper())
print(name.lower())
print("DSAdsjkdasjafbakFHJSADKas".title())
print(len(name))
print("name\\ name\"")
print(name[1])
print(name[-2])#second from end
print(name[1:7])#from 1 index to 7
print(name[:8])#to 8
print(name[5:])#after 5
True or False #Booleans
""#False
print(type(True))
test = ["test", False]
print(any(test))#one of array true = True
print(all(test))#all should be true = False

#Complex
num1 = 2+3j
num2 = complex(2,3)

print(num1.real, num1.imag)
print(num2)

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)
print(State(1))

dogs = ["R", 1, "S", True]
print("R" in dogs)
print(dogs[2:4])#slice list
dogs.append("M")
print(dogs)
dogs.extend(["L", "J"])
print(dogs)
dogs += ["O", "B"]#same as extend
print(dogs)
dogs.remove("O")
print(dogs)
print(dogs.pop())#remove last
print(dogs)
dogs.insert(2, "T")
print(dogs)
dogs[3:5] = ["K", "Y"]#replace
print(dogs)
dogs[1] = "Q"
dogs.sort()
print(dogs)
dogscopy = dogs[:]
print(dogscopy)

#Tuples(immutable)
names = ("R", "M")

#Dictionaries

dog = {"name": "Roger"}#key:value

print(dog["name"])
print(dog.get("name"))
print(dog.get("age"))#return "None"
print(dog.get("color", "green"))#return "green"
print("color" in dog)
print(dog.keys())
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))
dog["age"] = 18

del dog["name"]
print(dog)

#Sets
set1 = {"A", "B"}
set2 = {"B"}

intersect = set1 & set2
union = set1 | set2
difference = set1 - set2
hasset1 = set1 > set2 #is set1 has set2 (all)
hasset2 = set1 < set2 #is set2 has set1 (all)
print(intersect)
print(union)
print(difference)
print(hasset1)
print(hasset2)

#functions
def hello(name="my friend"):
    print("Hello " + name)

hello("R")
hello("T")
hello()

def hello2(name):
    if not name:
        print("No name")
        return
    return "Hello " + name, 10, "other"#('Hello Alex', 10, 'other')

hello2(False)
print(hello2("Alex"))

#Objects(evething in python is object)

#Loops
condition = True
while condition == True:
    print(condition)
    condition = False

items = [1,2,3,4]
    
for index,item in enumerate(items):
    if index == 2:
        continue
    if index == 3:
        break
    print(index, item)

#classes

#inheretence
class Animal():
    def walk(self):
        print("walking...")

class Dog(Animal):
    #constractor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)

print(roger.name)
print(roger.age)
roger.bark()
roger.walk()

#Modules
import dog#full import
dog.bark()

from dog import bark#specific import
bark()

from lib import cat#import from folder
cat.say()

#standart libraries
import math

print(math.sqrt(4))

import sys

print(sys.argv)#python main.py someString 39 (from command line to get arguments)

#Lambda functions

lambda num : num * 2

mulpiply = lambda a, b : a * b

print(mulpiply(2, 4))

##map(), filter(), reduce()

numbers = [1, 2, 3]

double = lambda a : a * 2

result = map(double, numbers)#or map(lambda a : a * 2, numbers)

print(list(result))

#filter()
def isEven(n):
    return n % 2 == 0

result = filter(isEven, numbers)

print(list(result))

#reduce()
from functools import reduce

expences = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum = reduce(lambda a, b: a[1] + b[1], expences)

print(sum)

#Recursion

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

#Decorators

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello")

hello()

#Docstrings (multiline comment that will be described when function will used)

def increment(n):
    """Increment a number"""
    return n + 1

print(increment(2))


#annotations

def increment2(n: int) -> int:
    return n+1

count: int = 0


#Exceptions

try:
    raise("An ERROR!")
except ZeroDivisionError:
    #handle error1
    print('zero')
except BaseException:
    print('Error happened')
else:
    #no exceptions
    print('heelooo')
finally:
    #do something in the end
    print('finally')

#pip (package manager)
#pypi.org

#pip install requests
#pip unistall requests
#pip show requests

#List Compressions (single lines loops)

numbers = [1, 2, 3, 4, 5, 6]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

#Polymorphism
class Dog:
    def eat(self):
        print("Eatings dog food")

class Cat:
    def eat(self):
        print("Easting cat food")

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

#Operator Overloading
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
    
roger = Dog('Roger', 8)
sid = Dog('Sid', 9)

print(roger > sid)