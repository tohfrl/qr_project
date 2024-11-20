from flask import Flask, redirect
import sqlite3

app = Flask(__name__)

@app.route('/<short_code>')
def redirect_to_target(short_code):
    """Zoek de URL op in de database en leid door."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT target_url FROM urls WHERE short_code=?", (short_code,))
    result = cursor.fetchone()
    conn.close()

    if result:
        # Als de URL bestaat, doorsturen
        return redirect(result[0])
    else:
        # Toon een foutmelding als de code niet bestaat
        return "URL niet gevonden", 404

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Gebruik de "PORT" omgeving of standaard 5000
    app.run(host="0.0.0.0", port=port, debug=True)
