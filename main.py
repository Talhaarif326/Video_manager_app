from database import get_db_connection, init_database
from video_models import Video
from operation.list_videos import list_videos
from operation.add_video import add_video
from operation.update_video import update_video
from operation.delete_video import delete_video
from utils.validators import video_exist

def main():
    while True:
        print("\n 🪧🪧 Youtube Manager 🪧🪧 \n")
        print("Ξ Menu")
        print("1. List all videos in Database ")
        print("2. Add video to the Database")
        print("3. Update video in the Database")
        print("4. Delete video from the Database")
        print("5. Exit the App")
        
        choice = input("Enter Choice: ")
        
        match choice:
                case "1":
                    list_videos()
                case "2":
                    add_video()
                case "3":
                    update_video()
                case "4":
                    delete_video()
                case "5":
                    break
                case _:
                    print("Invalid Choice")
    
    
if __name__== "__main__":
    main()