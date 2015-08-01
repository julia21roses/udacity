import webbrowser

class Video():
    def __init__(self, video_title, video_storyline, poster_image, trailer_youtube):
        self.title = video_title
        self.storyline = video_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
