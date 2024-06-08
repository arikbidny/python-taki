import sqlite3
import pickle

def init_db():
    conn = sqlite3.connect('taki_game.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS game_state (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        state BLOB)''')
    conn.commit()
    conn.close()

def save_game_state_to_db(game_state):
    conn = sqlite3.connect('taki_game.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO game_state (state) VALUES (?)', (pickle.dumps(game_state),))
    conn.commit()
    conn.close()

def load_game_state_from_db():
    conn = sqlite3.connect('taki_game.db')
    cursor = conn.cursor()
    cursor.execute('SELECT state FROM game_state ORDER BY id DESC LIMIT 1')
    state = cursor.fetchone()
    conn.close()
    return pickle.loads(state[0]) if state else None
