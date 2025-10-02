import sqlite3

def get_db_connection():
    """
    Create and return database connection
    """
    conn = sqlite3.connect("Youtube_manager.db")
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn


def init_database():
    """
    Initializes the database with the required table
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
    ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    DURATION TEXT NOT NULL,
    CATEGORY TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()
    
    print("✅ Database initialized successfully!")