#1
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Write a string: ")

    def printString(self):
        print(self.input_string.upper())

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5

#5
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

#6
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]

prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1, numbers))

print("Prime numbers:", prime_numbers)