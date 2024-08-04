from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuration
DATABASE = 'database.db'

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database
def init_db():
    with app.app_context():
        db = get_db_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        user_id = request.form['id']
        password = request.form['password']
        role = request.form['role']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the user into the database
        cursor.execute('INSERT INTO users (email, phone, user_id, password, role) VALUES (?, ?, ?, ?, ?)',
                       (email, phone, user_id, password, role))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

# Route to handle login (dummy authentication for demonstration)
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Dummy authentication logic (replace with actual authentication)
        if username == 'admin' and password == 'password':
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
