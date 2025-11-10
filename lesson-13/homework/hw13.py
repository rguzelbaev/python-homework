
Homework:
Вопросы:
Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

Ответы:
from datetime import datetime, date, timedelta
import pytz
import re
import time


# 1 AGE CALCULATOR

def age_calculator():
    birth_str = input("Введите дату рождения (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += (date(today.year, today.month, 1) - timedelta(days=1)).day
    if months < 0:
        years -= 1
        months += 12

    print(f"Ваш возраст: {years} лет, {months} месяцев, {days} дней")


#2 DAYS UNTIL NEXT BIRTHDAY

def days_until_birthday():
    birth_str = input("Введите дату рождения (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = date.today()
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_left = (next_birthday - today).days
    print(f"До следующего дня рождения осталось: {days_left} дней")


#3 MEETING SCHEDULER
def meeting_scheduler():
    current_str = input("Введите текущие дату и время (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Введите длительность встречи (часы): "))
    duration_minutes = int(input("Введите длительность встречи (минуты): "))
    current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
    end_time = current_dt + timedelta(hours=duration_hours, minutes=duration_minutes)
    print("Встреча закончится в:", end_time.strftime("%Y-%m-%d %H:%M"))


# 4 TIMEZONE CONVERTER

def timezone_converter():
    dt_str = input("Введите дату и время (YYYY-MM-DD HH:MM): ")
    from_zone = input("Введите ваш текущий timezone (например, Asia/Tashkent): ")
    to_zone = input("Введите timezone, в который хотите перевести (например, Europe/London): ")

    local = pytz.timezone(from_zone)
    target = pytz.timezone(to_zone)

    naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    local_dt = local.localize(naive_dt)
    target_dt = local_dt.astimezone(target)

    print("Время в выбранной зоне:", target_dt.strftime("%Y-%m-%d %H:%M (%Z)"))


# 5 COUNTDOWN TIMER

def countdown_timer():
    future_str = input("Введите будущее время (YYYY-MM-DD HH:MM:SS): ")
    future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        diff = future_time - now
        if diff.total_seconds() <= 0:
            print("\n⏰ Время вышло!")
            break
        print(f"\rОсталось: {diff}", end="")
        time.sleep(1)


# 6 EMAIL VALIDATOR

def email_validator():
    email = input("Введите email: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("✅ Email корректен")
    else:
        print("❌ Некорректный email")


# 7 PHONE NUMBER FORMATTER

def phone_formatter():
    phone = input("Введите номер (только цифры): ")
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print("Форматированный номер:", formatted)
    else:
        print("❌ Номер должен содержать 10 цифр")


# 8 PASSWORD STRENGTH CHECKER

def password_checker():
    pwd = input("Введите пароль: ")
    strong = True
    if len(pwd) < 8:
        print("❌ Пароль слишком короткий (минимум 8 символов)")
        strong = False
    if not re.search(r"[A-Z]", pwd):
        print("❌ Нет заглавной буквы")
        strong = False
    if not re.search(r"[a-z]", pwd):
        print("❌ Нет строчной буквы")
        strong = False
    if not re.search(r"\d", pwd):
        print("❌ Нет цифры")
        strong = False
    if strong:
        print("✅ Пароль надёжный")


# 9 WORD FINDER

def word_finder():
    text = """Python is great. Python is powerful and easy to learn. I love Python!"""
    word = input("Введите слово для поиска: ")
    matches = re.findall(word, text, re.IGNORECASE)
    print(f"Слово '{word}' встречается {len(matches)} раз(а).")


# 10 DATE EXTRACTOR

def date_extractor():
    text = input("Введите текст, содержащий даты: ")
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    dates = re.findall(pattern, text)
    if dates:
        print("Найденные даты:", dates)
    else:
        print("Даты не найдены.")


# Меню выбора задачи

def main():
    tasks = {
        "1": age_calculator,
        "2": days_until_birthday,
        "3": meeting_scheduler,
        "4": timezone_converter,
        "5": countdown_timer,
        "6": email_validator,
        "7": phone_formatter,
        "8": password_checker,
        "9": word_finder,
        "10": date_extractor
    }

    print("\n=== PYTHON DATE & STRING PRACTICE ===")
    for k in tasks:
        print(f"{k}. {tasks[k].__name__.replace('_', ' ').title()}")
    choice = input("\nВыберите задачу (1-10): ")
    if choice in tasks:
        tasks[choice]()
    else:
        print("Неверный выбор!")

if __name__ == "__main__":
    main()
