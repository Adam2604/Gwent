import sqlite3

DB_NAME = 'game_results.db'


def initialize_results_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Tabela na sumę zwycięstw graczy
    c.execute('''
        CREATE TABLE IF NOT EXISTS players_results (
            player_name TEXT PRIMARY KEY,
            wins INTEGER DEFAULT 0
        )
    ''')

    # Nowa tabela na wyniki pojedynków
    c.execute('''
        CREATE TABLE IF NOT EXISTS matches_results (
            player1 TEXT,
            player2 TEXT,
            player1_wins INTEGER DEFAULT 0,
            player2_wins INTEGER DEFAULT 0,
            PRIMARY KEY (player1, player2)
        )
    ''')

    conn.commit()
    conn.close()


def add_or_update_winner(player_name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('SELECT wins FROM players_results WHERE player_name = ?', (player_name,))
    result = c.fetchone()

    if result:
        new_wins = result[0] + 1
        c.execute('UPDATE players_results SET wins = ? WHERE player_name = ?', (new_wins, player_name))
    else:
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
        return 0


def update_match_result(winner, loser):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Sprawdzamy, czy taki mecz już istnieje
    c.execute('SELECT player1_wins, player2_wins FROM matches_results WHERE player1 = ? AND player2 = ?', (winner, loser))
    result = c.fetchone()

    if result:
        # Jeśli istnieje, zwiększamy liczbę zwycięstw wygranego
        new_player1_wins = result[0] + 1
        c.execute('UPDATE matches_results SET player1_wins = ? WHERE player1 = ? AND player2 = ?', (new_player1_wins, winner, loser))
    else:
        # Jeśli nie istnieje, tworzymy nowy wpis
        c.execute('SELECT player1_wins, player2_wins FROM matches_results WHERE player1 = ? AND player2 = ?', (loser, winner))
        result_reversed = c.fetchone()

        if result_reversed:
            # Jeśli istnieje zapis odwrotny (loser-winner), zwiększamy liczbę wygranych player2
            new_player2_wins = result_reversed[1] + 1
            c.execute('UPDATE matches_results SET player2_wins = ? WHERE player1 = ? AND player2 = ?', (new_player2_wins, loser, winner))
        else:
            # Tworzymy nowy mecz
            c.execute('INSERT INTO matches_results (player1, player2, player1_wins, player2_wins) VALUES (?, ?, ?, ?)', (winner, loser, 1, 0))

    conn.commit()
    conn.close()


def get_match_results(player1, player2):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Szukamy wpisu player1 vs player2
    c.execute('SELECT player1_wins, player2_wins FROM matches_results WHERE player1 = ? AND player2 = ?', (player1, player2))
    result = c.fetchone()

    if result:
        wins_player1, wins_player2 = result
    else:
        # Szukamy odwrotnego meczu
        c.execute('SELECT player2_wins, player1_wins FROM matches_results WHERE player1 = ? AND player2 = ?', (player2, player1))
        result_reversed = c.fetchone()
        if result_reversed:
            wins_player1, wins_player2 = result_reversed
        else:
            wins_player1, wins_player2 = 0, 0  # Jeszcze nie było meczu

    conn.close()
    return wins_player1, wins_player2


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
    cursor.execute('DELETE FROM matches_results')
    conn.commit()
    conn.close()
    print("Wszystkie wyniki zostały zresetowane.")
