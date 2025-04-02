from flask import Flask, request, render_template
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['user']
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']
        date = request.form['date']
        
        db_path = os.path.join(os.getcwd(), 'expenses.db')
        conn = sqlite3.connect(db_path)

        c = conn.cursor()
        c.execute("INSERT INTO expenses (user, category, amount, description, date) VALUES (?, ?, ?, ?, ?)",
                  (user, category, amount, description, date))
        conn.commit()
        conn.close()
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
