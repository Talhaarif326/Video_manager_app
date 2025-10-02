from database import get_db_connection

def add_video():
    conn = get_db_connection()
    cursor = conn.cursor()
    video_name = input("Enter Video name: ")
    video_duration = input("Enter Video duration: ")
    video_category = input("Enter Video category: ")
    
    cursor.execute("INSERT INTO videos(NAME, DURATION, CATEGORY) VALUES(?, ?, ?)", (video_name, video_duration,video_category))
    print(f"Video added successfully ✅")
    
    conn.commit()
    conn.close()