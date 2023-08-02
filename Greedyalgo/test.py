class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __lt__(self, other):
        print(self.age,other.age)
        return self.age < other.age
        
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
print(p1 < p2)
#if p1 < p2:
    #print("Alice is younger than Bob")
#else:
    #print("Bob is younger than Alice")
