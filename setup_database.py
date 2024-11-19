import sqlite3

# Maak verbinding met (of maak) de database
conn = sqlite3.connect('database.db')  # Dit maakt een databasebestand genaamd 'database.db'
cursor = conn.cursor()

# Maak de tabel voor URL's en korte codes
cursor.execute('''
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_code TEXT UNIQUE,
    target_url TEXT
)
''')
print("Database en tabel zijn aangemaakt!")

# Sluit de verbinding
conn.close()
