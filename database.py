import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            user TEXT,
            category TEXT,
            amount REAL,
            description TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_expense(user, category, amount, description, date):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO expenses (user, category, amount, description, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (user, category, amount, description, date))
    conn.commit()
    conn.close()
