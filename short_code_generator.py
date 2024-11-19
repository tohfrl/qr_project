import sqlite3
import random
import string

def generate_short_code(length=6):
    """Genereer een unieke korte code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def add_url_to_database(target_url):
    """Voeg een korte code en de URL toe aan de database."""
    short_code = generate_short_code()  # Genereer een korte code
    conn = sqlite3.connect('database.db')  # Verbind met de database
    cursor = conn.cursor()
    
    try:
        # Voeg de korte code en URL toe aan de tabel
        cursor.execute("INSERT INTO urls (short_code, target_url) VALUES (?, ?)", (short_code, target_url))
        conn.commit()
        print(f"Korte code: {short_code}, Doel-URL: {target_url}")
    except sqlite3.IntegrityError:
        print("Fout: Korte code bestaat al. Probeer opnieuw.")
    finally:
        conn.close()

if __name__ == "__main__":
    # Vraag de gebruiker om een URL
    target_url = input("Voer een URL in die je wilt koppelen aan een korte code: ")
    add_url_to_database(target_url)
