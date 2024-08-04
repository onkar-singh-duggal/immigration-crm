import sqlite3

# Create SQLite database and tables
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create user_roles table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_roles (
        role_id INTEGER PRIMARY KEY,
        role_name TEXT NOT NULL
    )
''')

# Insert initial user roles
initial_roles = [
    ('Reception'),
    ('Tele Caller'),
    ('Visa Counselor'),
    ('Visa Filer'),
    ('Manager'),
    ('Financer'),
    ('Owner Director')
]
cursor.executemany('INSERT INTO user_roles (role_name) VALUES (?)', initial_roles)

# Create navigation_links table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS navigation_links (
        link_id INTEGER PRIMARY KEY,
        link_url TEXT NOT NULL,
        link_text TEXT NOT NULL,
        roles_allowed TEXT NOT NULL
    )
''')

# Insert example navigation links
initial_links = [
    ('/dashboard', 'Dashboard', 'Reception,Tele Caller,Visa Counselor,Visa Filer,Financer,Manager,Owner Director'),
    ('/leads', 'Leads', 'Reception,Tele Caller,Visa Counselor,Visa Filer,Manager,Owner Director'),
    ('/visa_info', 'Visa Info', 'Visa Counselor,Visa Filer,Manager'),
    ('/detailed_report', 'Detailed Report', 'Reception,Tele Caller,Visa Counselor,Visa Filer,Financer,Manager,Owner Director'),
    ('/finance', 'Finance', 'Financer,Manager,Owner Director'),
    ('/annual_summary', 'Annual Summary', 'Reception,Tele Caller,Visa Counselor,Visa Filer,Financer,Manager,Owner Director'),
    ('/calendar', 'Calendar', 'Reception,Tele Caller,Visa Counselor,Visa Filer,Financer,Manager,Owner Director'),
    ('/user_management', 'User Management', 'Manager,Owner Director')
]
cursor.executemany('INSERT INTO navigation_links (link_url, link_text, roles_allowed) VALUES (?, ?, ?)', initial_links)

# Commit changes and close connection
conn.commit()
conn.close()
