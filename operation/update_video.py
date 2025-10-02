from database import get_db_connection
from utils.validators import video_exist

def update_video():
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    video_id = int(input("Enter video ID to be updated: "))
    if video_exist(video_id):
        new_name = input("Enter New Name: ")
        new_duration = input("Enter New Duration: ")
        
        cursor.execute("UPDATE videos SET name = ? , duration = ? WHERE ID = ?",(new_name, new_duration, video_id))
        
        print("Video Updated Successfully ✅")

        conn.commit()
        conn.close()