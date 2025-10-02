from database import get_db_connection

def video_exist(video_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ID FROM videos WHERE ID = ?", (video_id,))
        conn.close()
        return cursor.fetchone() is not None
        
    except Exception as e:
        print(f"Database Error: {e}")