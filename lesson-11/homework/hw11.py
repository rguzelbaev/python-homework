Вопросы:
Homework:
1. Create your own virtual environment and install some python packages.
2. Create custom modules.
    - Create math_operations.py module. Define `add`, `subtract`, `multiply` and `divide` functions in it. (All functions accept two arguments in this task)
    - Create string_utils.py module. Define `reverse_string` and `count_vowels` functions in it. (All functions accept one argument in this task)
3. Create custom packages.
    - Create `geometry` package. 
    <pre>
    geometry\
        __init__.py
        circle.py
    </pre>
    Define `calculate_area` and `calculate_circumference` functions in circle.py. These functions accept one argument(radius).
    - Create `file_operations` package.
    <pre>
    file_operations\
        __init__.py
        file_reader.py
        file_writer.py
    </pre>
    Define `read_file` function in file_reader.py. This function accepts one argument(file_path). Define `write_file` function in file_writer.py. This function accepts two arguments(file_path, content).
Ответы:
🧱 1. Создание виртуального окружения и установка пакетов
🔹 Шаг 1: Создай виртуальное окружение
python -m venv venv


(в некоторых системах: python3 -m venv venv)

🔹 Шаг 2: Активируй окружение

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

🔹 Шаг 3: Установи несколько пакетов
pip install requests numpy pandas


Проверить:

pip list

📘 2. Создание пользовательских модулей

Создаём файлы рядом с твоим основным проектом:

project/
│
├── math_operations.py
├── string_utils.py
└── main.py

🧮 Файл: math_operations.py
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division result of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

🔤 Файл: string_utils.py
def reverse_string(s):
    """Return the reversed version of the string."""
    return s[::-1]

def count_vowels(s):
    """Return the number of vowels in the string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

📦 3. Создание собственных пакетов

Создай такую структуру:

project/
│
├── geometry/
│   ├── __init__.py
│   └── circle.py
│
└── file_operations/
    ├── __init__.py
    ├── file_reader.py
    └── file_writer.py

⚙️ Файл: geometry/circle.py
import math

def calculate_area(radius):
    """Return the area of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)

def calculate_circumference(radius):
    """Return the circumference of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius

📂 Файл: file_operations/file_reader.py
def read_file(file_path):
    """Read contents of a file and return as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."

✍️ Файл: file_operations/file_writer.py
def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"Content written successfully to {file_path}"

🚀 4. Проверка всех модулей и пакетов

Создай файл main.py:

from math_operations import add, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file


# --- Math Operations ---
print("Add:", add(5, 3))
print("Divide:", divide(10, 2))

# --- String Utilities ---
print("Reversed:", reverse_string("hello"))
print("Vowels:", count_vowels("Python Programming"))

# --- Geometry Package ---
print("Circle Area:", calculate_area(5))
print("Circle Circumference:", calculate_circumference(5))

# --- File Operations ---
file_path = "sample.txt"
write_file(file_path, "Hello, Python packages!")
print("File content:", read_file(file_path))

✅ Вывод при запуске main.py:
Add: 8
Divide: 5.0
Reversed: olleh
Vowels: 4
Circle Area: 78.53981633974483
Circle Circumference: 31.41592653589793
File content: Hello, Python packages!
