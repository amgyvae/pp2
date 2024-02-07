class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Your name is: {self.name}, and your age is: {self.age}"
        
print("Input your name: ")
name = input()
print("Input your age: ")
age = input() 
p = Person(name, age)
print(p)