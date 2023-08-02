# Data types, strings, operators, and Chaining Comparison Operators with Logical Operators
num1 = 10
num2 = 20
if num1 > num2 and num1 % 2 == 0:
    print("num1 is greater than num2 and is even")
else:
    print("Condition not satisfied")

# Python Lists and Dictionaries, Sets, Tuples
my_list = [1, 2, 3, 4, 5]
my_dict = {'name': 'John', 'age': 30}
my_set = {1, 2, 3, 4, 5}
my_tuple = (1, 2, 3, 4, 5)

# Loops, Break and Continue Statements
for num in my_list:
    if num == 3:
        break
    print(num)

# Object-Oriented Programming - Class and attributes
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine started.")

my_car = Car("Toyota", "Corolla")
print(my_car.make)
print(my_car.model)
my_car.start_engine()

# Python strings in detail
my_string = "Hello, World!"
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.split(","))

# Python F-String
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Map, Classes, Functions and Arguments
def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# First Class functions, Private Variables, Global and Non Local Variables, __import__ function
def outer_func():
    x = 10
    def inner_func():
        nonlocal x
        x += 5
        print(x)
    inner_func()

outer_func()

# Magic Functions, Tuple Unpacking
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)

# Static Variables and Methods in Python
class MathUtils:
    PI = 3.14159

    @staticmethod
    def square(num):
        return num ** 2

print(MathUtils.PI)
print(MathUtils.square(5))

# Lambda Functions, Magic methods
add = lambda x, y: x + y
print(add(2, 3))

# Inheritance and Polymorphism, Errors and Exception Handling
class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement sound() method.")

class Cat(Animal):
    def sound(self):
        return "Meow"

my_cat = Cat()
print(my_cat.sound())

# User-defined functions, Python garbage collection, debugger in Python
def greet(name):
    print(f"Hello, {name}!")

greet("John")

# Iterators, Generators, and Decorators, Memoization using Decorators
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))

# Ordered and Defaultdict, Coroutine
from collections import OrderedDict, defaultdict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
print(ordered_dict)

default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict['c'])  # Output: 0

# Regular expression, Magic methods, Closures
import re

pattern = r'\b[A-Za-z]+\b'
text = "Hello, World! This is a sample text."
matches = re.findall(pattern, text)
print(matches)

# ChainMap
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map['a'])  # Output: 1
print(chain_map['c'])  # Output: 3

# Python Itertools
import itertools

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
combined = itertools.product(numbers, letters)
for item in combined:
    print(item)

# Advanced python constructs
result = [x if x % 2 == 0 else None for x in numbers]
print(result)

# Comprehensions, Named Tuple, Type hinting in Python
from typing import List, Tuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

def multiply(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    for num in numbers:
        product *= num
    return product, len(numbers)

print(multiply([1, 2, 3, 4, 5]))

# 13. User-defined functions, Python garbage collection, debugger in Python
def greet(name):
    print(f"Hello, {name}!")

greet("John")

# Python garbage collection - no specific code implementation required here
# Debugger in Python - can be done using the built-in pdb module or an IDE's debugging features

# 14. Iterators, Generators, and Decorators, Memoization using Decorators
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))

# Decorators
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def my_function():
    print("Inside decorated function")

my_function()

# Memoization using Decorators
def memoize(func):
    memo = {}
    def wrapper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# 15. Ordered and Defaultdict, Coroutine
from collections import OrderedDict, defaultdict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
print(ordered_dict)

default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict['c'])  # Output: 0

# Coroutine
def coroutine():
    while True:
        x = yield
        print(f"Received: {x}")

coro = coroutine()
next(coro)
coro.send(10)

# 16. Regular expression, Magic methods, Closures
import re

pattern = r'\b[A-Za-z]+\b'
text = "Hello, World! This is a sample text."
matches = re.findall(pattern, text)
print(matches)

# Closures
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure = outer_func(10)
print(closure(5))

# 17. ChainMap
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map['a'])  # Output: 1
print(chain_map['c'])  # Output: 3

# 18. Python Itertools
import itertools

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
combined = itertools.product(numbers, letters)
for item in combined:
    print(item)

# 19. Advanced python constructs
result = [x if x % 2 == 0 else None for x in numbers]
print(result)

# 20. Comprehensions, Named Tuple, Type hinting in Python
from typing import List, Tuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

def multiply(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    for num in numbers:
        product *= num
    return product, len(numbers)