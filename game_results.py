import sqlite3


def initialize_results_db():
    conn = sqlite3.connect('game_results.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS players_results (
            player_name TEXT PRIMARY KEY,
            wins INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


def add_or_update_winner(player_name):
    conn = sqlite3.connect('game_results.db')
    c = conn.cursor()

    # Sprawdzenie czy gracz już istnieje
    c.execute('SELECT wins FROM players_results WHERE player_name = ?', (player_name,))
    result = c.fetchone()

    if result:
        # Jeśli istnieje, zwiększ liczbę zwycięstw
        new_wins = result[0] + 1
        c.execute('UPDATE players_results SET wins = ? WHERE player_name = ?', (new_wins, player_name))
    else:
        # Jeśli nie istnieje, dodaj nowego gracza
        c.execute('INSERT INTO players_results (player_name, wins) VALUES (?, ?)', (player_name, 1))

    conn.commit()
    conn.close()
