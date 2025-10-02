# YouTube Manager App 🎬

A Python-based command-line application for managing YouTube video collections with full CRUD operations and SQLite database integration.

## 🚀 Features

- **Add Videos** - Store video details (name, duration, category)
- **List Videos** - View all videos in a formatted table
- **Update Videos** - Modify existing video information
- **Delete Videos** - Remove videos from collection
- **Persistent Storage** - SQLite database for data persistence

## 🛠️ Tech Stack

- **Python 3** - Core programming language
- **SQLite** - Database for data storage
- **Tabulate** - Beautiful table formatting
- **OOP Principles** - Clean object-oriented design

## 📁 Project Structure
youtube_manager/
├── main.py               # Application entry point
├── database.py           # Database connection & setup
├── video_models.py       # Video class (OOP model)
├── operations/           # CRUD operations
│   ├── add_video.py
│   ├── list_videos.py
│   ├── update_video.py
│   └── delete_video.py
└── utils/                # Helper functions



- **Modular Design** - Separated concerns for maintainability
- **OOP Implementation** - Video class with proper encapsulation
- **Database Layer** - Abstracted SQL operations
- **CRUD Operations** - Complete Create, Read, Update, Delete functionality

## 🚦 Getting Started

1. **Clone the repository**
   git clone https://github.com/yourusername/youtube-manager.git

2. **Install dependencies**
    pip install tabulate

3. **Run the application**
    python main.py


**💡 Usage**
1. **Choose from the menu options:**
    List all videos    
    Add new video    
    Update existing video   
    Delete video    
    Exit application
   
**💡 Usage Example**
===== YouTube Manager =====
1. List all videos
2. Add new video
3. Update existing video
4. Delete video
5. Exit

Enter your choice: 1

+----+----------------------+----------+-------------+
| ID | Name                 | Duration | Category    |
+----+----------------------+----------+-------------+
|  1 | Python Crash Course  | 15:00    | Education   |
+----+----------------------+----------+-------------+


**🎯 Learning Outcomes**
This project demonstrates:

Python OOP concepts
SQLite database integration
Modular application architecture
CRUD operations implementation
Professional project structure
