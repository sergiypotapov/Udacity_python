__author__ = 'spotapov'
import webbrowser
class Movie():
    """ Good class"""
    VALID_RATINGS = ["A", "B", "C", "D"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)
