Вопросы:
## Homework Projects:

Homework 1. ToDo List Application

1. Define Task Class:
    - Create a Task class with attributes such as task title, description, due date, and status.
2. Define ToDoList Class:
    - Create a ToDoList class that manages a list of tasks.
    - Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
3. Create Main Program:
    - Develop a simple CLI to interact with the ToDoList.
    - Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
4. Test the Application:
    - Create instances of tasks and test the functionality of your ToDoList.

<br><br>
Homework 2. Simple Blog System

1. Define Post Class:
    - Create a Post class with attributes like title, content, and author.
2. Define Blog Class:
    - Create a Blog class that manages a list of posts.
    - Include methods to add a post, list all posts, and display posts by a specific author.
3. Create Main Program:
    - Develop a CLI to interact with the Blog system.
    - Include options to add posts, list all posts, and display posts by a specific author.
4. Enhance Blog System:
    - Add functionality to delete a post, edit a post, and display the latest posts.
5. Test the Application:
    - Create instances of posts and test the functionality of your Blog system.

<br><br>
Homework 3. Simple Banking System

1. Define Account Class:
    - Create an Account class with attributes like account number, account holder name, and balance.
2. Define Bank Class:
    - Create a Bank class that manages a list of accounts.
    - Include methods to add an account, check balance, deposit money, and withdraw money.
3. Create Main Program:
    - Develop a CLI to interact with the Banking system.
    - Include options to add accounts, check balance, deposit money, and withdraw money.
4. Enhance Banking System:
    - Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
5. Test the Application:
    - Create instances of accounts and test the functionality of your Banking system.

Ответы:
🧩 Homework 1 — ToDo List Application
# ===============================
# ToDo List Application
# ===============================

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅ Done" if self.completed else "❌ Not Done"
        return f"{self.title} ({status}) — Due: {self.due_date}\n   {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def incomplete_tasks(self):
        incompletes = [task for task in self.tasks if not task.completed]
        if not incompletes:
            print("All tasks are completed! 🎉")
        else:
            for task in incompletes:
                print(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("Task marked as complete ✅")
        else:
            print("Invalid task number!")


# CLI
def todo_cli():
    todo = ToDoList()
    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. Show Incomplete Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            desc = input("Task description: ")
            due = input("Due date (e.g. 2025-10-10): ")
            todo.add_task(Task(title, desc, due))
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            todo.incomplete_tasks()
        elif choice == "4":
            todo.list_tasks()
            idx = int(input("Enter task number to mark complete: ")) - 1
            todo.mark_task_complete(idx)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Uncomment to test:
# todo_cli()

📰 Homework 2 — Simple Blog System
# ===============================
# Blog System Application
# ===============================

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"📜 {self.title} by {self.author}\n{self.content}\n"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("No posts yet.")
        else:
            for post in self.posts:
                print(post)

    def posts_by_author(self, author):
        filtered = [p for p in self.posts if p.author.lower() == author.lower()]
        if not filtered:
            print(f"No posts found by {author}.")
        else:
            for p in filtered:
                print(p)

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title.lower() != title.lower()]
        print("Post deleted (if it existed).")

    def edit_post(self, title, new_content):
        for p in self.posts:
            if p.title.lower() == title.lower():
                p.content = new_content
                print("Post updated successfully.")
                return
        print("Post not found.")

# CLI
def blog_cli():
    blog = Blog()
    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Show Posts by Author")
        print("4. Edit Post")
        print("5. Delete Post")
        print("6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            t = input("Title: ")
            c = input("Content: ")
            a = input("Author: ")
            blog.add_post(Post(t, c, a))
        elif choice == "2":
            blog.list_posts()
        elif choice == "3":
            name = input("Author name: ")
            blog.posts_by_author(name)
        elif choice == "4":
            t = input("Title of post to edit: ")
            new_c = input("New content: ")
            blog.edit_post(t, new_c)
        elif choice == "5":
            t = input("Title of post to delete: ")
            blog.delete_post(t)
        elif choice == "6":
            print("Exiting Blog System.")
            break
        else:
            print("Invalid choice!")

# Uncomment to test:
# blog_cli()

💰 Homework 3 — Simple Banking System
# ===============================
# Simple Banking System
# ===============================

class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
        else:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"Account #{self.acc_number}: {self.holder_name} — Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_number] = account
        print("Account added successfully.")

    def find_account(self, acc_number):
        return self.accounts.get(acc_number)

    def transfer(self, from_acc, to_acc, amount):
        a1 = self.find_account(from_acc)
        a2 = self.find_account(to_acc)
        if not a1 or not a2:
            print("Invalid account number(s).")
            return
        if a1.balance < amount:
            print("Not enough funds for transfer.")
            return
        a1.withdraw(amount)
        a2.deposit(amount)
        print("Transfer complete ✅")

# CLI
def bank_cli():
    bank = Bank()
    while True:
        print("\n--- Bank Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer Money")
        print("6. Show All Accounts")
        print("7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            num = input("Account number: ")
            name = input("Holder name: ")
            bank.add_account(Account(num, name))
        elif choice == "2":
            num = input("Account number: ")
            acc = bank.find_account(num)
            print(acc if acc else "Account not found.")
        elif choice == "3":
            num = input("Account number: ")
            amt = float(input("Amount: "))
            acc = bank.find_account(num)
            if acc:
                acc.deposit(amt)
        elif choice == "4":
            num = input("Account number: ")
            amt = float(input("Amount: "))
            acc = bank.find_account(num)
            if acc:
                acc.withdraw(amt)
        elif choice == "5":
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amt = float(input("Amount: "))
            bank.transfer(from_acc, to_acc, amt)
        elif choice == "6":
            for acc in bank.accounts.values():
                print(acc)
        elif choice == "7":
            print("Exiting Bank System.")
            break
        else:
            print("Invalid choice!")

# Uncomment to test:
# bank_cli()
