import sqlite3


# Funkcja do łączenia z bazą danych
def connect_db():
    return sqlite3.connect("gwint.db")

# Inicjalizacja tabel
def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()

    # Tabela graczy
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """)

    # Tabela kart gracza
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS player_cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id INTEGER,
        card_name TEXT,
        strength INTEGER,
        fraction TEXT,
        unit_type TEXT,
        effect TEXT,
        FOREIGN KEY (player_id) REFERENCES players(id)
    )
    """)

    conn.commit()
    conn.close()

# Funkcja do dodania nowego gracza
def add_player(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO players (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

# Funkcja do dodania kart gracza do bazy danych
def save_player_deck(player_name, cards):
    conn = connect_db()
    cursor = conn.cursor()

    # Pobranie ID gracza
    cursor.execute("SELECT id FROM players WHERE name = ?", (player_name,))
    player_id = cursor.fetchone()

    if player_id:
        player_id = player_id[0]
        # Usunięcie starych kart gracza
        cursor.execute("DELETE FROM player_cards WHERE player_id = ?", (player_id,))

        # Dodanie nowych kart
        for card in cards:
            cursor.execute("""
            INSERT INTO player_cards (player_id, card_name, strength, fraction, unit_type, effect)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (player_id, card.name, card.strength, card.fraction, card.type, card.effect))

        conn.commit()

    conn.close()


# Funkcja do pobrania talii gracza
def load_player_deck(player_name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM players WHERE name = ?", (player_name,))
    player_id = cursor.fetchone()

    if not player_id:
        conn.close()
        return []

    player_id = player_id[0]

    cursor.execute("""
    SELECT card_name, strength, fraction, unit_type, effect FROM player_cards WHERE player_id = ?
    """, (player_id,))

    deck = cursor.fetchall()
    conn.close()

    return deck
