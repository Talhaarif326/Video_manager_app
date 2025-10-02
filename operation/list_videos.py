from database import get_db_connection
from tabulate import tabulate

def list_videos():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    print(tabulate(rows, headers=["ID","Name","Duration","Category"], tablefmt = "grid"))
    
    conn.close()