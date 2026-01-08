import sqlite3
DB_NAME = "expense.db"
def connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
def table():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT,
        payment_mode TEXT,
        merchant_name TEXT,
        location TEXT,
        notes TEXT,
        created_by TEXT
    )
    """)
    conn.commit()
    conn.close()
