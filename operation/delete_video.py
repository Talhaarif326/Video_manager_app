from database import get_db_connection
from utils.validators import video_exist



def delete_video():
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    video_id = int(input("Enter video ID to be Deleted: "))
    
    if video_exist(video_id):
        cursor.execute("DELETE FROM videos WHERE ID = ?", (video_id,))
        print(f"Video Deleted successfully ✅")
    
    conn.commit()
    conn.close()
