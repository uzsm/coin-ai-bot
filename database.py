import sqlite3
from pathlib import Path
from datetime import datetime

# database papkasini yaratadi
DB_DIR = Path("database")
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "coin_ai.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    username TEXT,
    register_date TEXT,
    last_seen TEXT,

    plan TEXT DEFAULT 'FREE',
    expire_date TEXT,

    selected_coin TEXT,
    selected_timeframe TEXT,

    state TEXT DEFAULT 'WAIT_COIN',

    language TEXT DEFAULT 'uz',

    status INTEGER DEFAULT 1
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
    user_id INTEGER PRIMARY KEY,
    name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT
    )
    """)
    conn.commit()
    conn.close()


# ↓↓↓ SHU YERDAN BOSHLAB QO'SHAMIZ ↓↓↓

def add_or_update_user(user):
    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "SELECT user_id FROM users WHERE user_id=?",
        (user.id,)
    )

    result = cursor.fetchone()

    if result is None:
        cursor.execute("""
            INSERT INTO users (
                user_id,
                first_name,
                username,
                register_date,
                last_seen
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            user.id,
            user.first_name or "",
            user.username or "",
            now,
            now
        ))
        print(f"Yangi foydalanuvchi: {user.id}")

    else:
        cursor.execute("""
            UPDATE users
            SET
                first_name=?,
                username=?,
                last_seen=?
            WHERE user_id=?
        """, (
            user.first_name or "",
            user.username or "",
            now,
            user.id
        ))

    conn.commit()
    conn.close()
def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user

def set_state(user_id, state):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET state=? WHERE user_id=?",
        (state, user_id)
    )

    conn.commit()
    conn.close() 
       
def set_coin(user_id, coin):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET selected_coin=? WHERE user_id=?",
        (coin, user_id)
    )

    conn.commit()
    conn.close()
    
def set_timeframe(user_id, timeframe):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET selected_timeframe=? WHERE user_id=?",
        (timeframe, user_id)
    )

    conn.commit()
    conn.close()



