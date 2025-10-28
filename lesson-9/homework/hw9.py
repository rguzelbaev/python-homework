Вопросы:
# Homework:

# Object-Oriented Programming (OOP) Exercises

## 1. Circle Class
Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

## 2. Person Class
Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

## 3. Calculator Class
Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

## 4. Shape and Subclasses
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

## 5. Binary Search Tree Class
Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

## 6. Stack Data Structure
Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

## 7. Linked List Data Structure
Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

## 8. Shopping Cart Class
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

## 9. Stack with Display
Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

## 10. Queue Data Structure
Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

## 11. Bank Class
Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.


Ответы:
🧮 1. Circle Class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Пример:
c = Circle(5)
print("Площадь:", c.area())
print("Периметр:", c.perimeter())

👤 2. Person Class
from datetime import date, datetime

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )


# Пример:
p = Person("Ali", "Uzbekistan", "2000-05-12")
print(f"{p.name} из {p.country}, возраст: {p.age()}")

➗ 3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")
        return a / b


# Пример:
calc = Calculator()
print(calc.add(5, 3))
print(calc.divide(10, 2))

🔷 4. Shape and Subclasses
import math

class Shape:
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределён")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() должен быть переопределён")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Пример:
shapes = [Circle(3), Square(4), Triangle(3, 4, 5)]
for s in shapes:
    print(type(s).__name__, "→ Площадь:", round(s.area(), 2), "| Периметр:", round(s.perimeter(), 2))

🌳 5. Binary Search Tree Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left:
                self._insert(root.left, key)
            else:
                root.left = Node(key)
        elif key > root.key:
            if root.right:
                self._insert(root.right, key)
            else:
                root.right = Node(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)


# Пример:
bst = BST()
for num in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bst.insert(num)

print(bst.search(7))  # True
print(bst.search(2))  # False

📦 6. Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Стек пуст!")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


# Пример:
s = Stack()
s.push(10)
s.push(20)
print(s.pop())  # 20

🔗 7. Linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")


# Пример:
ll = LinkedList()
ll.insert(3)
ll.insert(2)
ll.insert(1)
ll.display()
ll.delete(2)
ll.display()

🛒 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def display(self):
        for name, info in self.items.items():
            print(f"{name}: {info['quantity']} × {info['price']} = {info['quantity'] * info['price']}")
        print("Итого:", self.total_price())


# Пример:
cart = ShoppingCart()
cart.add_item("Apple", 2, 5)
cart.add_item("Banana", 3, 2)
cart.display()

🧱 9. Stack with Display
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            raise IndexError("Стек пуст!")
        return self.stack.pop()

    def display(self):
        print("Стек:", self.stack)


# Пример:
s = Stack()
s.push(10)
s.push(20)
s.display()
s.pop()
s.display()

⏩ 10. Queue Data Structure
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            raise IndexError("Очередь пуста!")
        return self.queue.pop(0)

    def display(self):
        print("Очередь:", self.queue)


# Пример:
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.display()
q.dequeue()
q.display()

🏦 11. Bank Class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount
        print(f"Внесено {amount}. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств!")
        self.balance -= amount
        print(f"Снято {amount}. Баланс: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, owner, balance=0):
        self.accounts[owner] = BankAccount(owner, balance)

    def transfer(self, from_owner, to_owner, amount):
        if from_owner not in self.accounts or to_owner not in self.accounts:
            raise ValueError("Один из счетов не найден!")
        self.accounts[from_owner].withdraw(amount)
        self.accounts[to_owner].deposit(amount)

    def show_accounts(self):
        for acc in self.accounts.values():
            print(f"{acc.owner}: {acc.balance}")


# Пример:
bank = Bank()
bank.add_account("Ali", 1000)
bank.add_account("Sara", 500)
bank.transfer("Ali", "Sara", 200)
bank.show_accounts()
