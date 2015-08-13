__author__ = 'spotapov'
import movies
import fresh_tomatoes
toy_story = movies.Movie("Toy Story",
                        "The story about Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = movies.Movie("Avatar",
                        "The story about Avatar",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.show_trailer()
school = movies.Movie("School of Rock",
                        "The story about School of Rock",
                        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
movies_list = [toy_story, avatar, school]
#fresh_tomatoes.open_movies_page(movies_list)
#print(movies.Movie.VALID_RATINGS)
#print(movies.Movie.__doc__)
print(movies.Movie.__module__)
print(movies.Movie.__name__)