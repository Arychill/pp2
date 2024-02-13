class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())


manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
print(f"Shape area: {shape.area()}")

square = Square(5)
print(f"Square area: {square.area()}")




class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")



import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


point1 = Point(1, 2)
point1.show()

point2 = Point(4, 6)
point2.show()

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")

point1.move(3, 5)
point1.show()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal not allowed.")

account = BankAccount(owner="John Doe", balance=1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(900)
account.withdraw(500)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1, numbers))
print(prime_numbers)
