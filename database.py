# database.py

import sqlite3
import os

def init_db():
    try:
        conn = sqlite3.connect('expenses.db')
        c = conn.cursor()
        
        # Check the connection
        if conn:
            print("Database connection established.", flush=True)
        
        # Create table if it doesn't exist
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
        
        # Check if the database file is created
        if os.path.exists('expenses.db'):
            print("Database file created successfully!", flush=True)
        else:
            print("Database file was NOT created.", flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)
