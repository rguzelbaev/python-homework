
## Homework
#Вопросы
1. Task: JSON Parsing
    - write a Python script that reads the students.jon JSON file and prints details of each student.
2. Task: Weather API
   1. Use this url : https://openweathermap.org/
   2. Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
3. Task: JSON Modification
   1. Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
4. Task: Movie Recommendation System
   1. Use this url http://www.omdbapi.com/ to fetch information about movies.
   2. Create a program that asks users for a movie genre and recommends a random movie from that genre.


#Ответы
1. JSON Parsing — чтение students.json
students.json (пример файла)

 пример:

[
    {"name": "Ali", "age": 20, "major": "Computer Science"},
    {"name": "Laylo", "age": 22, "major": "Mathematics"},
    {"name": "John", "age": 19, "major": "Physics"}
]

Python решение
import json

def read_students():
    with open("students.json", "r", encoding="utf-8") as file:
        students = json.load(file)

    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}, Major: {s['major']}")

read_students()

2. Weather API — OpenWeatherMap

Для использования API нужен API KEY.
Получить бесплатно → https://openweathermap.org/api

Пусть ключ будет:

API_KEY = "YOUR_API_KEY"

Python решение
import requests

API_KEY = "YOUR_API_KEY"
CITY = "Tashkent"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])

get_weather(CITY)

3. JSON Modification — books.json
books.json (пример)
[
    {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"}
]


import json

FILE = "books.json"

def load_books():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def add_book():
    books = load_books()
    new_id = max(book["id"] for book in books) + 1 if books else 1

    title = input("Enter book title: ")
    author = input("Enter author: ")

    books.append({"id": new_id, "title": title, "author": author})
    save_books(books)
    print("Book added!")

def update_book():
    books = load_books()
    book_id = int(input("Enter book ID to update: "))

    for book in books:
        if book["id"] == book_id:
            book["title"] = input("New title: ")
            book["author"] = input("New author: ")
            save_books(books)
            print("Book updated!")
            return

    print("Book not found!")

def delete_book():
    books = load_books()
    book_id = int(input("Enter book ID to delete: "))

    books = [b for b in books if b["id"] != book_id]
    save_books(books)
    print("Book deleted!")

def menu():
    while True:
        print("\n1. Add book\n2. Update book\n3. Delete book\n4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

menu()

4. Movie Recommendation System — OMDb API
API KEY required

Получить бесплатно: https://www.omdbapi.com/apikey.aspx

Пусть ключ будет:

API_KEY = "YOUR_API_KEY"

Рабочая программа

Рекомендация случайного фильма по жанру.

import requests
import random

API_KEY = "YOUR_API_KEY"

def get_movies_by_genre(genre):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie"
    response = requests.get(url).json()

    if response.get("Search"):
        return response["Search"]
    else:
        return []

def recommend_movie(genre):
    movies = get_movies_by_genre(genre)

    if not movies:
        print("No movies found for this genre.")
        return

    movie = random.choice(movies)

    print("\n Recommended Movie:")
    print("Title:", movie["Title"])
    print("Year:", movie["Year"])
    print("IMDb ID:", movie["imdbID"])

genre = input("Enter movie genre (e.g., Action, Comedy, Drama): ")
recommend_movie(genre)
