#Вопросы:
### Review Exercises

1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.

2.  Populate your new table with the following values:

| Name            | Species      | Age |
|-----------------|--------------|-----|
| Benjamin Sisko  | Human        |  40 |
| Jadzia Dax      | Trill        | 300 |
| Kira Nerys      | Bajoran      |  29 |



3. Update the Name of Jadzia Dax to be Ezri Dax

4.  Display the Name and Age of everyone in the table classified as Bajoran.



#Ответы:
import sqlite3

# Создаем и подключаемся к базе данных
conn = sqlite3.connect("starfleet.db")
cursor = conn.cursor()

# 1. Создаем таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Добавляем записи
cursor.execute("DELETE FROM Roster")  # очищаем, если таблица уже была

cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# 3. Обновляем имя Jadzia -> Ezri
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# 4. Показываем всех Bajoran
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")

rows = cursor.fetchall()
print("Bajoran crew members:")
for row in rows:
    print(row)

conn.commit()
conn.close()
