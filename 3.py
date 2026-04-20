class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Alice", 20)
s1.display_info()
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

r1 = Rectangle(5, 3)
print(f"Area: {r1.area()}")
print(f"Perimeter: {r1.perimeter()}")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
owner = input("Enter your name: ")
balance = float(input("Enter your initial balance: "))
a1 = BankAccount(owner, balance)
while True:
    action = input("Do you want to deposit or withdraw? (d/w), or 'q' to quit: ")
    if action == 'd':
        amount = float(input("Enter amount to deposit: "))
        a1.deposit(amount)
    elif action == 'w':
        amount = float(input("Enter amount to withdraw: "))
        a1.withdraw(amount)
    elif action == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid action. Please enter 'd' for deposit or 'w' for withdraw.")