# initialize_db.py

from database import init_db

if __name__ == "__main__":
    try:
        init_db()
        print("Database initialized successfully!", flush=True)
    except Exception as e:
        print(f"Error initializing database: {e}", flush=True)
