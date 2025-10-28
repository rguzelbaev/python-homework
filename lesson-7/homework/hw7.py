Вопросы:
# Homework

## Task
Learn about `map` and `filter` functions, and be prepared to explain them in class. Provide examples using these functions with `lambda` expressions.

---

# Problems

## 1. is_prime(n) funksiyasi
`is_prime(n)` funksiyasini hosil qiling (`n > 0`). Agar `n` soni tub bo'lsa `True`, aks holda `False` qiymat qaytarsin.

### Misollar:
- **Kiritish:**  
  4  
  **Natija:**  
  False  
  _(Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)_

- **Kiritish:**  
  7  
  **Natija:**  
  True  
  _(Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)_

---

## 2. digit_sum(k) funksiyasi
`digit_sum(k)` funksiyasini yozing, u `k` sonining raqamlari yig'indisini hisoblaydi.

### Misollar:
- **Kiritish:**  
  24  
  **Natija:**  
  6  
  _(Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)_

- **Kiritish:**  
  502  
  **Natija:**  
  7  
  _(Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)_

---

## 3. Ikki sonning darajalari
Berilgan `N` sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, `2**k` shaklidagi sonlarni) chop etuvchi funksiyani yozing.

### Misol:
- **Kiritish:**  
  10  
  **Natija:**  
  2 4 8  
  _(Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)_

    Ответы:
  # =======================================
# 🧠 Lesson: map(), filter(), lambda
# =======================================

# 🔹 map(function, iterable)
# Применяет функцию ко всем элементам последовательности

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("map() пример — квадраты чисел:", squares)

# 🔹 filter(function, iterable)
# Оставляет только те элементы, для которых функция возвращает True

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("filter() пример — чётные числа:", even_numbers)

print("-" * 50)


# =======================================
# 🧩 Problem 1: is_prime(n)
# =======================================

def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 🔸 Проверка
print("Problem 1:")
print(is_prime(4))   # False
print(is_prime(7))   # True

# 🔸 Пример с filter — выбрать только простые числа
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = list(filter(is_prime, nums))
print("Простые числа в списке:", primes)
print("-" * 50)


# =======================================
# 🧩 Problem 2: digit_sum(k)
# =======================================

def digit_sum(k):
    """Возвращает сумму цифр числа k."""
    return sum(map(int, str(abs(k))))  # через map() преобразуем цифры в int


# 🔸 Проверка
print("Problem 2:")
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7
print(digit_sum(-321)) # 6
print("-" * 50)


# =======================================
# 🧩 Problem 3: Powers of 2 up to N
# =======================================

def powers_of_two(N):
    """Выводит все степени двойки, не превышающие N."""
    result = []
    power = 1
    while True:
        power *= 2
        if power > N:
            break
        result.append(power)
    return result


# 🔸 Проверка
print("Problem 3:")
print(powers_of_two(10))  # [2, 4, 8]

# 🔸 Пример с map() — возвести в квадрат все степени 2
print("Квадраты этих степеней:", list(map(lambda x: x**2, powers_of_two(10))))

