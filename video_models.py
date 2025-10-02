class Video:
    def __init__(self,video_name,video_duration,video_category,video_id=None):
        self.video_name = video_name
        self.video_duration = video_duration
        self.video_id = video_id
        self.video_category = video_category
        
    def __str__(self):
        return f"Video ID: {self.video_id}, Video Name: {self.video_name}, Video Duration: {self.video_duration}, Category: {self.video_category} "