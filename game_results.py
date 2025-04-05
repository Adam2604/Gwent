import sqlite3

DB_NAME = 'game_results.db'


def initialize_results_db():
    conn = sqlite3.connect(DB_NAME)
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
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Sprawdzanie, czy gracz już istnieje
    c.execute('SELECT wins FROM players_results WHERE player_name = ?', (player_name,))
    result = c.fetchone()

    if result:
        # Gracz istnieje – zwiększ liczbę zwycięstw o 1
        new_wins = result[0] + 1
        c.execute('UPDATE players_results SET wins = ? WHERE player_name = ?', (new_wins, player_name))
    else:
        # Gracz nie istnieje – dodaj go do bazy z 1 zwycięstwem
        c.execute('INSERT INTO players_results (player_name, wins) VALUES (?, ?)', (player_name, 1))

    conn.commit()
    conn.close()


def get_player_wins(player_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT wins FROM players_results WHERE player_name = ?', (player_name,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return 0  # Jeśli gracza nie ma w bazie, zwracamy 0


def show_all_players_results():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT player_name, wins FROM players_results ORDER BY wins DESC')
    results = cursor.fetchall()

    conn.close()

    print("\n--- Ranking graczy ---")
    if results:
        for idx, (player_name, wins) in enumerate(results, start=1):
            print(f"{idx}. {player_name}: {wins} zwycięstw")
    else:
        print("Brak danych w bazie.")


def reset_results():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM players_results')
    conn.commit()
    conn.close()
    print("Wszystkie wyniki zostały zresetowane.")
