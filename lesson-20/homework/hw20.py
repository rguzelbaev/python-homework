вопросы:
Homework 1:

Using chinook.db write pandas code.

1. Customer Purchases Analysis:

- Find the total amount spent by each customer on purchases (considering invoices).
- Identify the top 5 customers with the highest total purchase amounts.
- Display the customer ID, name, and the total amount spent for the top 5 customers.

2. Album vs. Individual Track Purchases:

- Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
- A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
- Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).


Ответы:
Импорт библиотек и подключение к базе
import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

1. Customer Purchases Analysis
Задача

Посчитать сумму всех покупок каждого клиента (Invoices → Total).

Найти топ-5 клиентов по сумме покупок.

Вывести CustomerId, имя и сумму.

✔ Решение полностью с Pandas:
# Загружаем таблицы
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM customers", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId, Total FROM invoices", conn)

# Считаем сумму Total по каждому клиенту
total_by_customer = invoices.groupby("CustomerId")["Total"].sum().reset_index()

# Объединяем с таблицей customers
merged = total_by_customer.merge(customers, on="CustomerId")

# Находим топ 5 покупателей
top5 = merged.sort_values("Total", ascending=False).head(5)

print(top5)

Вывод будет такой:
CustomerId	FirstName	LastName	Total
…	…	…	…
2. Album vs Individual Track Purchases
Что требуется:

Определить, предпочитает ли клиент покупать:

полный альбом
или

отдельные треки

Чтобы понять, купил ли клиент весь альбом, нужно сравнить:

кол-во купленных им треков из альбома
с

общим числом треков в альбоме

Шаг 1. Загружаем необходимые таблицы
invoice_items = pd.read_sql("SELECT InvoiceId, TrackId FROM invoice_items", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM tracks", conn)
albums = pd.read_sql("SELECT AlbumId, Title FROM albums", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM invoices", conn)

Шаг 2. Соединяем invoice_items → tracks (какой трек из какого альбома)
purchases = invoice_items.merge(tracks, on="TrackId")
purchases = purchases.merge(invoices[["InvoiceId", "CustomerId"]], on="InvoiceId")


Теперь purchases содержит:
CustomerId, AlbumId, TrackId

Шаг 3. Считаем количество треков в каждом альбоме
tracks_per_album = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
tracks_per_album.rename(columns={"TrackId": "TotalTracks"}, inplace=True)

Шаг 4. Считаем, сколько треков из альбома купил каждый пользователь
user_tracks = purchases.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index()
user_tracks.rename(columns={"TrackId": "PurchasedTracks"}, inplace=True)

Шаг 5. Определяем тип покупателя
# Добавляем кол-во треков в альбоме
user_tracks = user_tracks.merge(tracks_per_album, on="AlbumId")

# Флаг: купил ЛИ полностью альбом
user_tracks["FullAlbum"] = user_tracks["PurchasedTracks"] == user_tracks["TotalTracks"]

Шаг 6. Определяем предпочтение каждого клиента
# Если клиент когда-либо покупал отдельные треки — это individual buyer
customer_pref = (
    user_tracks.groupby("CustomerId")["FullAlbum"]
    .apply(lambda x: "full album" if x.all() else "individual tracks")
    .reset_index()
)

Шаг 7. Считаем проценты
summary = customer_pref["FullAlbum"].value_counts(normalize=True) * 100
print(summary)

Пример результата:
individual tracks    78.4%
full album           21.6%

ИТОГ
1. TOP-5 клиентов по сумме:

✓ готовый код
✓ объединение invoices + customers
✓ сортировка

2. Предпочтение клиентов (альбомы vs треки):

✓ соединение invoice_items → tracks → invoices
✓ сравнение PurchasedTracks vs TotalTracks
✓ классификация клиента
✓ подсчёт процентов
